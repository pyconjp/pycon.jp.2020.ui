<template>
  <div class="flex flex-col items-center justify-center">
    <div class="flex flex-col items-center justify-center h-32 md:h-56">
      <h1
        class="flex items-center justify-center w-screen text-2xl font-semibold text-center text-py-black sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >
        Sponsors
      </h1>
      <h3
        class="flex items-center justify-center w-screen mb-8 text-lg font-semibold text-center text-py-black sm:text-xl md:text-2xl lg:text-3xl m-screen"
      >
        {{ $t('pages.sponsor.title') }}
      </h3>
    </div>

    <python-banner
      direction="right"
      back-ground-color="#71A4F1"
      size="small"
      length="long"
    >
      <template #title>
        PLATINUM
      </template>
    </python-banner>

    <div class="flex flex-wrap items-start justify-center mt-8">
      <platinum-and-gold-sponsor
        v-for="platinum in $t('sponsor.platinum')"
        :key="platinum.companyName"
        sponsor-type="platinum"
        :url="platinum.url"
        class="w-full mt-10 lg:w-2/5 lg:mx-8"
        :recruit-exist="
          judgeRecruitInformationExist(platinum.recruitInformation)
        "
      >
        <template #image>
          <img
            :src="require(`~/assets/img/sponsor/${platinum.imagePath}`)"
            class="w-3/4"
          />
        </template>
        <template #companyName>
          {{ platinum.companyName }}
        </template>
        <template #companyInformation>
          {{ platinum.description }}
        </template>
        <template #recruitInformation>
          {{ platinum.recruitInformation }}
        </template>
      </platinum-and-gold-sponsor>
    </div>

    <python-banner
      direction="right"
      back-ground-color="#E3AB4A"
      size="small"
      length="mid"
      class="mt-16"
    >
      <template #title>
        GOLD
      </template>
    </python-banner>
    <div class="flex flex-wrap items-start justify-center mt-8">
      <platinum-and-gold-sponsor
        v-for="gold in $t('sponsor.gold')"
        :key="gold.companyName"
        sponsor-type="gold"
        :url="gold.url"
        :recruit-exist="judgeRecruitInformationExist(gold.recruitInformation)"
        class="w-full mt-10 lg:w-1/3 lg:mx-8"
        color="#E3AB4A"
      >
        <template #image>
          <img
            :src="require(`~/assets/img/sponsor/${gold.imagePath}`)"
            class="w-3/4"
          />
        </template>
        <template #companyName>
          {{ gold.companyName }}
        </template>
        <template #companyInformation>
          {{ gold.description }}
        </template>
        <template #recruitInformation>
          {{ gold.companyName }}
        </template>
      </platinum-and-gold-sponsor>
    </div>

    <python-banner
      direction="right"
      back-ground-color="#818181"
      size="small"
      length="small"
      class="mt-16"
    >
      <template #title>
        SILVER
      </template>
    </python-banner>

    <div class="grid grid-cols-1 gap-4 mt-8 md:grid-cols-2">
      <a
        v-for="silver in $t('sponsor.silver')"
        :key="silver.companyName"
        :href="silver.url"
        target="_blank"
        rel="noopener noreferrer"
      >
        <div class="flex">
          <p class="inline text-2xl break-all">
            {{ silver.companyName }}
          </p>
          <i class="ml-2 text-3xl material-icons">link</i>
        </div>
      </a>
    </div>

    <python-banner
      direction="right"
      back-ground-color="#3D40CB"
      size="small"
      length="small"
      class="mt-16"
    >
      <template #title>
        SPECIAL
      </template>
    </python-banner>
    <h3 class="mt-6 text-4xl font-medium text-py-black">
      {{ $t('sponsor.message.specialSponsor') }}
    </h3>
    <div class="flex flex-wrap items-start justify-center mt-8">
      <platinum-and-gold-sponsor
        v-for="cooperation in $t('sponsor.special.cooperation')"
        :key="cooperation.companyName"
        sponsor-type="gold"
        :url="cooperation.url"
        class="w-full mt-10 lg:w-1/3 lg:mx-8"
        color="#3D40CB"
      >
        <template #image>
          <img
            :src="require(`~/assets/img/sponsor/${cooperation.imagePath}`)"
            class="w-3/4"
          />
        </template>
        <template #companyName>
          {{ cooperation.companyName }}
        </template>
        <template #companyInformation>
          {{ cooperation.description }}
        </template>
      </platinum-and-gold-sponsor>
    </div>
    <h3 class="mt-16 text-4xl font-medium text-py-black">
      {{ $t('sponsor.message.tutorial') }}
    </h3>
    <div class="flex flex-wrap items-start justify-center mt-8 mb-16">
      <platinum-and-gold-sponsor
        v-for="tutorial in $t('sponsor.special.tutorial')"
        :key="tutorial.groupName"
        sponsor-type="gold"
        :url="tutorial.url"
        class="w-full mt-10 lg:w-1/3 lg:mx-8"
        color="#3D40CB"
      >
        <template #image>
          <img
            :src="require(`~/assets/img/sponsor/${tutorial.imagePath}`)"
            class="w-3/4"
          />
        </template>
        <template #companyName>
          {{ tutorial.groupName }}
        </template>
        <template #companyInformation>
          {{ tutorial.description }}
        </template>
      </platinum-and-gold-sponsor>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import PythonBanner from '~/components/Elements/PythonBanner'
import PlatinumAndGoldSponsor from '~/components/Domains/Sponsor/PlatinumAndGoldSponsor'

export default Vue.extend({
  components: { PythonBanner, PlatinumAndGoldSponsor },
  data() {
    return {}
  },
  methods: {
    judgeRecruitInformationExist(message) {
      return message !== ''
    },
  },
  head() {
    return { title: this.$t('pages.sponsor.title') }
  },
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
