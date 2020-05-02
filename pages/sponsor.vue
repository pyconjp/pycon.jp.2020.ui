<template>
  <div>
    <div class="flex items-center justify-center">
      <h1
        class="flex items-center justify-center w-screen h-32 text-2xl text-center bg-gray-200 md:h-56 sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >{{ $t('pages.sponsor.title') }}</h1>
    </div>
    <div class="flex flex-row items-center justify-center">
      <hr class="w-1/3" />
      <h2 class="my-12 text-4xl">Platinum</h2>
      <hr class="w-1/3" />
    </div>
    <div class="flex flex-col items-center justify-center">
      <PlatinumAndGoldSponsor class="mt-4 w-3/4"></PlatinumAndGoldSponsor>
      <PlatinumAndGoldSponsor class="mt-20 w-3/4"></PlatinumAndGoldSponsor>
      <PlatinumAndGoldSponsor class="mt-20 w-3/4"></PlatinumAndGoldSponsor>
    </div>
    <div class="flex flex-row items-center justify-center">
      <hr class="w-1/3" />
      <h2 class="my-12 text-4xl">Gold</h2>
      <hr class="w-1/3" />
    </div>
    <div class="flex items-center justify-center">
      <div class="w-3/4">
        <div class="flex flex-wrap items-center justify-center">
          <PlatinumAndGoldSponsor class="p-4 w-1/2"></PlatinumAndGoldSponsor>
          <PlatinumAndGoldSponsor class="p-4 w-1/2"></PlatinumAndGoldSponsor>
          <PlatinumAndGoldSponsor class="p-4 w-1/2"></PlatinumAndGoldSponsor>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import PlatinumAndGoldSponsor from '~/components/Domains/sponsor/platinumAndGoldSponsor'

export default Vue.extend({
  components: { PlatinumAndGoldSponsor },
  data() {
    return {}
  },
  head() {
    return { title: this.$t('pages.sponsor.title') }
  }
})
</script>

<style></style>
