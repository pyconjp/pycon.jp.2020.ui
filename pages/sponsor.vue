<template>
  <div class="flex flex-col items-center justify-center">
    <div class="w-3/4">
      <div class="flex items-center justify-center">
        <h1
          class="flex items-center justify-center w-screen h-32 text-2xl text-center bg-gray-200 md:h-56 sm:text-3xl md:text-4xl lg:text-5xl m-screen"
        >{{ $t('pages.sponsor.title') }}</h1>
      </div>

      <div class="flex flex-row items-center justify-center">
        <hr class="w-2/3" />
        <h2 class="my-12 text-4xl">Platinum</h2>
        <hr class="w-2/3" />
      </div>
      <div class="flex flex-col items-center justify-center">
        <PlatinumAndGoldSponsor class="mt-4">
          <template #companyName>
            <p class="text-2xl">Pythonダミー株式会社</p>
          </template>
          <template #companyInformation>
            <p>
              弊社はPythonコミュニティの繁栄を目指して活動しています。
              たくさんの人が楽しみながらPythonを学ぶことができるように日々活動しています。
            </p>
          </template>
          <template #recruitInformation>
            <p>
              Python愛にあふれる人を募集します。
              経験者、初心者を問わず何事にも積極的にチャレンジする、
              失敗を恐れずに前向きに取り組む人を歓迎します。
            </p>
          </template>
        </PlatinumAndGoldSponsor>
        <PlatinumAndGoldSponsor class="mt-20"></PlatinumAndGoldSponsor>
        <PlatinumAndGoldSponsor class="mt-20"></PlatinumAndGoldSponsor>
      </div>

      <div class="flex flex-row items-center justify-center">
        <hr class="w-2/3" />
        <h2 class="my-12 text-4xl">Gold</h2>
        <hr class="w-2/3" />
      </div>
      <div class="flex items-center justify-center">
        <div class="flex flex-wrap items-center justify-center">
          <PlatinumAndGoldSponsor class="p-4 w-full md:w-1/2"></PlatinumAndGoldSponsor>
          <PlatinumAndGoldSponsor class="p-4 w-full md:w-1/2"></PlatinumAndGoldSponsor>
          <PlatinumAndGoldSponsor class="p-4 w-full md:w-1/2"></PlatinumAndGoldSponsor>
        </div>
      </div>

      <div class="flex flex-row items-center justify-center">
        <hr class="w-2/3" />
        <h2 class="my-12 text-4xl">Silver</h2>
        <hr class="w-2/3" />
      </div>

      <div class="flex flex-wrap justify-center">
        <div v-for="value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" :key="value" class="w-1/2 md:w-1/3">
          <div class="flex justify-center items-center px-2 my-2">
            <div class="silver-sponsor-list-item"></div>
            <div>株式会社 Pythonコミュニティ運営企画 {{ value }}</div>
          </div>
        </div>
        <!-- <ul>
          <li
            v-for="value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
            :key="value"
            class="w-1/3 inline-block"
          >
            <div></div>
            株式会社 {{ value }}
          </li>
        </ul>-->
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

<style scoped>
.silver-sponsor-list-item {
  width: 8px;
  height: 1px;
  background-color: #666;
  margin-right: 0.5rem;
}
</style>
