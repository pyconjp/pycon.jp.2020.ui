// pyconjpのブログ記事から `.nuxt/dist/news.json' を生成する

module.exports = function apiModule() {
  this.nuxt.hook('build:before', async () => {
    const axios = require('axios')
    const { parseString } = require('xml2js')

    const resp = await axios.get(
      'http://pyconjp.blogspot.com/feeds/posts/default/-/pyconjp2020?alt=rss&max-results=5'
    )

    let items = []

    parseString(resp.data, (err, result) => {
      if (err) console.error(err)
      items = JSON.stringify(result.rss.channel[0].item)
    })

    this.options.build.plugins.push({
      apply(compiler) {
        compiler.plugin('emit', (compilation, cb) => {
          compilation.assets['news.json'] = {
            source: () => items,
            size: () => {},
          }
          cb()
        })
      },
    })

    this.options.head.link = [
      ...this.options.head.link,
      {
        rel: 'prefetch',
        href: `${this.options.build.publicPath}news.json`,
        as: 'fetch',
      },
    ]

    if (this.options.dev) return

    // generate時にexpressを立てて、json取得できるようにする
    this.nuxt.hook('build:done', () => {
      console.log('**[generate]** opening server connection')
      const express = require('express')
      const app = express()

      app.use(express.static(this.options.generate.dir))

      const server = app.listen(process.env.PORT || 3000)

      this.nuxt.hook('generate:done', () => {
        console.log('**[generate]** closing server connection')
        server.close()
      })
    })
  })
}
