<template>
  <div class="space-y-24">
    <section
      class="relative flex items-start justify-center h-80 md:h-120 md:items-center"
    >
      <div class="mt-16 mr-2 md:m-0">
        <h1 class="text-4xl font-bold leading-tight md:text-6xl">
          PyCon JP <br />2020
        </h1>
        <h2 class="mt-6 text-2xl md:text-3xl">
          <i class="text-red-400 material-icons">location_on</i> Online
          Conference
        </h2>
        <h2 class="text-2xl md:text-3xl">
          <i class="text-red-400 material-icons">event</i> August 28(Fri.) /
          29(Sat.)
        </h2>
      </div>
      <div
        class="absolute w-screen h-full opacity-25 main-visual md:w-50vw md:opacity-50 md:relative"
        rel="https://www.ac-illust.com/main/detail.php?id=496603&word=%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E9%87%91%E9%AD%9A%E5%A4%8F%E7%A5%AD%E3%82%8A%E7%B8%81%E6%97%A5%E9%A3%BE%E3%82%8A%E5%92%8C%E9%A2%A8%E6%89%8B%E6%9B%B8%E3%81%8D%E5%8B%95%E7%89%A9"
      ></div>
    </section>

    <!-- <div class="flex flex-col items-center justify-center">
      <div
        class="w-3/4 py-4 my-16 border-8 border-blue-600 border-double rounded-lg "
      >
        <div class="flex">
          <div class="flex items-center justify-center w-1/4">
            <font-awesome-icon
              :icon="['far', 'handshake']"
              class="text-5xl opacity-50"
            />
          </div>
          <div
            class="flex flex-col items-center justify-center w-2/3 border-l-2 border-blue-500"
          >
            <h2 class="text-xl md:text-3xl">スタッフ募集中！</h2>
            <p>詳しくはこちら</p>
          </div>
        </div>
      </div>
    </div> -->

    <python-banner direction="left" back-ground-color="bg-blue-500" size="big">
      <template #title>
        企業スポンサー様募集中
      </template>
      <template #content>
        PyCon JP 2020を応援して下さるスポンサー様を募集しております<br />
        <span class=" hover:underline">> 詳細はこちらから</span>
      </template>
    </python-banner>

    <python-banner
      direction="right"
      back-ground-color="bg-orange-400"
      size="big"
    >
      <template #title>
        チケット販売開始
      </template>
      <template #content>
        PyCon JP 2020のチケット販売を開始しました！<br />
        <span class="hover:underline">> 詳細はこちらから</span>
      </template>
    </python-banner>

    <section class="flex flex-col items-center justify-center space-y-12">
      <h2
        class="inline text-3xl border-b-8 border-blue-600 border-solid md:text-5xl"
      >
        NEWS
      </h2>
      <div
        class="flex flex-col justify-center w-full mx-auto space-y-4 md:w-4/5"
      >
        <div v-for="item in [1, 2, 3]" :key="item" class="flex justify-between">
          <h3 class="text-lg text-left text-gray-700 md:text-xl">2020.5.3</h3>
          <div class="w-full ml-6 md:ml-12 hover:underline">
            CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始
          </div>
        </div>
      </div>
    </section>

    <section class="flex flex-col items-center justify-center space-y-12">
      <div class="flex flex-col items-center justify-center my-24">
        <h2
          class="inline text-3xl border-b-8 border-blue-600 border-solid md:text-5xl"
        >
          Session
        </h2>
      </div>
      <python-banner
        direction="right"
        back-ground-color="bg-blue-500"
        size="small"
      >
        <template #title>
          Keynote
        </template>
      </python-banner>

      <div class="flex flex-wrap justify-around">
        <talk-content class="w-full md:w-2/5" talk-type="talk"></talk-content>
        <talk-content
          class="w-full md:w-2/5 mt-10  md:mt-0"
          talk-type="talk"
        ></talk-content>
      </div>

      <python-banner
        direction="right"
        back-ground-color="bg-orange-400"
        size="small"
      >
        <template #title>
          Invided talk
        </template>
      </python-banner>

      <talk-content
        class="w-1/2"
        talk-type="talk"
        main-color="orange"
      ></talk-content>

      <python-banner
        direction="right"
        back-ground-color="bg-blue-500"
        size="small"
      >
        <template #title>
          Sessions
        </template>
      </python-banner>
    </section>

    <section class="flex flex-col items-center justify-center space-y-12">
      <h2
        class="inline text-3xl border-b-8 border-blue-600 border-solid md:text-5xl"
      >
        Sponsor
      </h2>

      <python-banner
        direction="right"
        back-ground-color="bg-indigo-500"
        size="small"
      >
        <template #title>
          Platinum
        </template>
      </python-banner>

      <python-banner
        direction="right"
        back-ground-color="bg-yellow-600"
        size="small"
      >
        <template #title>
          Gold
        </template>
      </python-banner>

      <python-banner
        direction="right"
        back-ground-color="bg-gray-600"
        size="small"
      >
        <template #title>
          Silver
        </template>
      </python-banner>
    </section>

    <section class="flex flex-col items-center justify-center space-y-12">
      <h2
        class="inline text-3xl border-b-8 border-blue-600 border-solid md:text-5xl"
      >
        Contact
      </h2>

      <python-banner
        direction="left"
        back-ground-color="bg-gray-600"
        size="big"
        :has-title="false"
      >
        <template #content>
          <p class="text-center">
            事前にFAQをご確認いただけますようにお願いします。 <br />
            ボランティアによる運営ですので、回答には1週間程度を要します。 <br />
            何卒お待ちいただけますようにお願いします。 <br />
          </p>
        </template>
      </python-banner>
    </section>
  </div>
</template>

<script>
import Vue from 'vue'
import PythonBanner from '~/components/Elements/PythonBanner'
import TalkContent from '~/components/Elements/TalkContent'

export default Vue.extend({
  components: {
    PythonBanner,
    TalkContent
  },
  head() {
    return { title: 'PyCon JP 2020', titleTemplate: null }
  }
})
</script>

<style scoped>
.main-visual {
  /* background: linear-gradient(to bottom, #a6d900 0%, #ff4454 100%); */
  background-image: url('../assets/img/top-background.png');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center center;
}
</style>
