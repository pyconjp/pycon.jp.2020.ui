import ja from './locales/ja.json'
import en from './locales/en.json'

export default {
  mode: 'spa',
  /*
   ** Headers of the page
   */
  head: {
    titleTemplate: '%s - PyCon JP 2020',
    title: 'PyCon JP 2020',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: 'PyCon JP 2020 Python'
      },
      {
        hid: 'og:site_name',
        property: 'og:site_name',
        content: 'PyCon JP 2020'
      },
      { hid: 'og:type', property: 'og:type', content: 'website' },
      { hid: 'og:url', property: 'og:url', content: 'https://pycon.jp/2020' },
      { hid: 'og:title', property: 'og:title', content: 'PyCon JP 2020' },
      {
        hid: 'og:description',
        property: 'og:description',
        content:
          'PyCon JPは、Pythonユーザが集まり、PythonやPythonを使ったソフトウェアについて情報交換、交流をするためのカンファレンスです。'
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: 'https://pycon.jp/2020/logo.png'
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ['~/plugins/vue-svg-transition'],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    '@nuxt/typescript-build',
    // Doc: https://github.com/nuxt-community/stylelint-module
    '@nuxtjs/stylelint-module',
    // Doc: https://github.com/nuxt-community/nuxt-tailwindcss
    '@nuxtjs/tailwindcss'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    // Doc: https://github.com/nuxt-community/dotenv-module
    '@nuxtjs/dotenv',
    'nuxt-i18n',
    '@nuxtjs/sitemap'
  ],
  i18n: {
    vueI18nLoader: true,
    baseUrl: 'https://pycon.jp/2020',
    seo: false,
    locales: [
      {
        code: 'ja',
        iso: 'ja',
        name: '日本語'
      },
      {
        code: 'en',
        iso: 'en',
        name: 'English'
      }
    ],
    defaultLocale: 'ja',
    detectBrowserLanguage: {
      useCookie: true,
      alwaysRedirect: true
    },
    vueI18n: {
      fallbackLocale: 'ja',
      messages: {
        ja,
        en
      }
    }
  },
  sitemap: {
    hostname: 'https://pycon.jp/2020'
  },
  purgeCSS: {
    whitelist: ['hidden']
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {},
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    // extend(config, ctx) {}
  }
}
