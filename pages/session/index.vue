<template>
  <div>
    <div class="flex flex-col items-center justify-center h-32 md:h-56">
      <h1
        class="flex items-center justify-center w-screen text-2xl font-semibold text-center text-py-black sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >
        Timetable
      </h1>
      <h3
        class="flex items-center justify-center w-screen mb-8 text-lg font-semibold text-center text-py-black sm:text-xl md:text-2xl lg:text-3xl m-screen"
      >
        {{ $t('pages["event-list"]["content-list"][0].title') }}
      </h3>
    </div>
    <div class="flex flex-row items-center justify-around w-full">
      <a
        v-for="platinum in $t('sponsor.platinum')"
        :key="platinum.companyName"
        :href="platinum.url"
        target="_blank"
        rel="noopener noreferrer"
        class="w-1/5"
      >
        <img :src="require(`~/assets/img/sponsor/${platinum.imagePath}`)"
      /></a>
    </div>
    <iframe
      id="iframeid"
      src="https://dev7367.d2hce9hbdo38af.amplifyapp.com/"
      frameborder="0"
      class="w-full mt-4 frame"
    ></iframe>
  </div>
</template>
<script>
export default {
  created() {
    this.$router.push(this.localePath('timetable'))
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
