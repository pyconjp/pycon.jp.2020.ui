<template>
  <div class="flex flex-col min-h-screen">
    <pycon-header />
    <main class="container flex-1 mx-auto">
      <nuxt />
    </main>
    <PyconFooter />
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
