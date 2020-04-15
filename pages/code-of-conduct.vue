vue<template>
  <div class="flex items-center justify-center h-120">
    <h1 class="text-5xl">
      {{ $t('pages.code-of-conduct.title') }}
    </h1>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  components: {},
  head() {
    return { title: this.$t('pages.code-of-conduct.title') }
  }
})
</script>

<style></style>

<i18n>
{
  "en": {
    "hello": "hello world!"
  },
  "ja": {
    "hello": "こんにちは、世界!"
  }
}
</i18n>
