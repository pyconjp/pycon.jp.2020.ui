<template>
  <div>
    <iframe
      id="iframeid"
      src="https://dev7367.d2hce9hbdo38af.amplifyapp.com/"
      frameborder="0"
      class="w-full frame"
    ></iframe>
  </div>
</template>
<script>
export default {
  asyncData() {
    const sessions = require('~/mocks/session.json')
    return { sessions }
  },
  mounted() {
    window.addEventListener(
      'message',
      function (element) {
        const iframe = document.getElementById('iframeid')
        iframe.style.height = element.data + 'px'
      },
      false
    )
  },
}
</script>

<style scoped></style>
