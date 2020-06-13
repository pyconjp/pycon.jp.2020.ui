<template>
  <div
    class="flex flex-col min-h-screen px-6 font-sans sm:px-8 md:px-10 lg:px-12"
  >
    <pycon-header class="w-full text-gray-800" />
    <main class="container flex flex-col flex-1 mx-auto">
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
    PyconFooter,
  },
  head() {
    return this.$nuxtI18nSeo()
  },
}
</script>

<style></style>
