<template>
  <div class="min-h-screen flex flex-col">
    <pycon-header />
    <main class="flex-1 container mx-auto">
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
