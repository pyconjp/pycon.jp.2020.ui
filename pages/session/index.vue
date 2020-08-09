<template>
  <div>
    <div class="flex flex-col items-center justify-center h-32 md:h-56">
      <h1
        class="flex items-center justify-center w-screen text-2xl font-semibold text-center text-py-black sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >
        Sponsors
      </h1>
      <h3
        class="flex items-center justify-center w-screen mb-8 text-lg font-semibold text-center text-py-black sm:text-xl md:text-2xl lg:text-3xl m-screen"
      >
        {{ $t('pages["event-list"]["content-list"][0].title') }}
      </h3>
    </div>
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
    // const sessions = require('~/mocks/session.json')
    // return { sessions }
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
