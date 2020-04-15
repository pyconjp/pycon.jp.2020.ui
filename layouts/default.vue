<template>
  <div class="flex flex-col min-h-screen font-sans antialiased">
    <pycon-header class="w-full text-gray-800" />
    <main class="container flex flex-col flex-1 max-w-5xl mx-auto">
      <nuxt />
    </main>
    <pycon-footer class="text-gray-800" />
  </div>
</template>

<script>
import PyconHeader from '~/components/Domains/Header'
import PyconFooter from '~/components/Domains/Footer'

export default {
  components: {
    PyconHeader,
    PyconFooter
  },
  head() {
    return this.$nuxtI18nSeo()
  }
}
</script>

<style></style>
