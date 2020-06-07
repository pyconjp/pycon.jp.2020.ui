<template>
  <div>
    {{ session }}
  </div>
</template>

<script>
export default {
  asyncData({ params }) {
    const sessionData = require('~/mocks/session.json')
    const session = sessionData.find((session) => session.id === params.id)
    return { session }
  },
  validate({ params }) {
    // params.idの存在チェックをしとかないと、正規表現マッチ時にstring変換されてtestを通ってしまう場合がある
    return params.id && /^\w+$/.test(params.id)
  },
}
</script>

<style></style>
