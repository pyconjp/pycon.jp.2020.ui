<template>
  <div class="flex items-center justify-center h-120">
    <h1 class="text-5xl text-center">
      {{ $t('pages.index.title') }}
    </h1>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  head() {
    return { title: 'PyCon JP 2020', titleTemplate: null }
  }
})
</script>

<style scoped>
.main-visual {
  /* background: linear-gradient(to bottom, #a6d900 0%, #ff4454 100%); */
  background-image: url('../assets/img/top-background.png');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center center;
}

@media screen and (min-width: 768px) {
  .main-visual-width {
    width: calc(100vw / 2);
  }
}

@media screen and (min-width: 768px) {
  .top-news {
    width: 80vw;
  }
}
</style>
