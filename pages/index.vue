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

<style></style>
