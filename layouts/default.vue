<template>
  <div class="flex flex-col min-h-screen">
    <pycon-header class="w-full px-6 text-gray-800 sm:px-8 md:px-10 lg:px-12" />
    <main
      class="container flex flex-col flex-1 px-6 mx-auto sm:px-8 md:px-10 lg:px-12"
    >
      <nuxt />
    </main>
    <pycon-footer
      class="px-6 text-gray-800 bg-py-blue-light sm:px-8 md:px-10 lg:px-12"
    />
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
