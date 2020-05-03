<template>
  <div class="flex flex-col items-center justify-center">
    <div class="flex items-center justify-center">
      <h1
        class="flex items-center justify-center w-screen h-32 text-2xl text-center bg-gray-200 md:h-56 sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >
        {{ $t('pages.sponsor.title') }}
      </h1>
    </div>
    <div class="w-3/4">
      <div class="flex flex-row items-center justify-center my-12">
        <hr class="w-full" />
        <h2 class="mx-2 text-4xl">Platinum</h2>
        <hr class="w-full" />
      </div>
      <div
        class="flex flex-col items-center justify-center space-y-12 md:space-y-20"
      >
        <PlatinumAndGoldSponsor>
          <template #companyName>
            Pythonダミー株式会社
          </template>
          <template #companyInformation>
            弊社はPythonコミュニティの繁栄を目指して活動しています。
            たくさんの人が楽しみながらPythonを学ぶことができるように日々活動しています。
          </template>
          <template #recruitInformation>
            <p>
              Python愛にあふれる人を募集します。
              経験者、初心者を問わず何事にも積極的にチャレンジする、
              失敗を恐れずに前向きに取り組む人を歓迎します。
            </p>
          </template>
        </PlatinumAndGoldSponsor>
        <PlatinumAndGoldSponsor></PlatinumAndGoldSponsor>
        <PlatinumAndGoldSponsor></PlatinumAndGoldSponsor>
      </div>

      <div class="flex flex-row items-center justify-center mt-12 mb-6">
        <hr class="w-full" />
        <h2 class="mx-2 text-4xl">Gold</h2>
        <hr class="w-full" />
      </div>
      <div class="flex items-center justify-center">
        <div class="flex flex-wrap items-center justify-start">
          <PlatinumAndGoldSponsor
            class="w-full p-4 md:w-1/2"
          ></PlatinumAndGoldSponsor>
          <PlatinumAndGoldSponsor
            class="w-full p-4 md:w-1/2"
          ></PlatinumAndGoldSponsor>
          <PlatinumAndGoldSponsor
            class="w-full p-4 md:w-1/2"
          ></PlatinumAndGoldSponsor>
        </div>
      </div>

      <div class="flex flex-row items-center justify-center mt-12 mb-6">
        <hr class="w-full" />
        <h2 class="mx-4 text-4xl">Silver</h2>
        <hr class="w-full" />
      </div>

      <div class="flex flex-wrap justify-center">
        <div
          v-for="value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
          :key="value"
          class="w-full sm:w-1/2 md:w-1/3"
        >
          <div class="flex items-center justify-center px-2 my-2">
            <div class="silver-sponsor-list-item"></div>
            <div>株式会社 Pythonコミュニティ運営企画 {{ value }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import PlatinumAndGoldSponsor from '~/components/Domains/Sponsor/PlatinumAndGoldSponsor'

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

<style scoped>
.silver-sponsor-list-item {
  width: 8px;
  height: 1px;
  background-color: #666;
  margin-right: 0.5rem;
}
</style>
