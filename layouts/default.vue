<template>
  <div class="flex flex-col min-h-screen">
    <pycon-header class="w-full text-gray-800" />
    <main class="container flex-1 mx-auto">
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
  }
}
</script>

<style></style>
