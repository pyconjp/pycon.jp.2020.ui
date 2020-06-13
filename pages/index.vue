<template>
  <div class="main-color">
    <section
      class="relative flex items-start justify-center h-80 md:h-120 md:items-center"
    >
      <div class="mt-16 mr-2 md:m-0">
        <h1 class="text-4xl font-extrabold leading-tight md:text-6xl">
          PyCon JP <br />2020 Online
        </h1>
        <h2 class="mt-6 text-2xl md:text-3xl">
          <i class="text-gray-700 material-icons">location_on</i> Online
          Conference
        </h2>
        <h2 class="text-2xl md:text-3xl">
          <i class="text-gray-700 material-icons">event</i> 2020 08/28(Fri.) /
          29(Sat.)
        </h2>
        <div class="flex">
          <img :src="require('~/assets/img/twitter.png')" class="h-8" />
          <a class="text-xl text-blue-500 ml-2">#pyconjp</a>
        </div>
      </div>
      <div
        class="absolute w-screen h-full main-visual md:w-50vw md:relative"
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

    <python-banner direction="left" back-ground-color="#3D40CB" size="big">
      <template #title>
        企業スポンサー様募集中
      </template>
      <template #content>
        PyCon JP 2020を応援して下さるスポンサー様を募集しております<br />
        <span class="hover:underline">スポンサーに申し込む</span>
      </template>
    </python-banner>

    <python-banner
      class="mt-8"
      direction="right"
      back-ground-color="#EE9D2C"
      size="big"
    >
      <template #title>
        チケット販売開始
      </template>
      <template #content>
        PyCon JP 2020のチケット販売を開始しました！<br />
        <span class="hover:underline">チケットを購入する</span>
      </template>
    </python-banner>

    <section
      class="flex flex-col items-center justify-center m-screen news-area mt-24 pt-12 pb-24 px-4"
    >
      <div class="flex flex-col items-center">
        <h2 class="inline text-3xl md:text-5xl mb-2">
          NEWS
        </h2>
        <p class="text-xl md:text-2xl mb-8">-お知らせ-</p>
      </div>
      <div
        class="relative flex flex-col justify-center items-center w-full container news-overview-content mt-6 bg-white"
      >
        <div
          class="relative w-4/5 flex justify-center flex-col z-10 bg-white space-y-6 py-8"
        >
          <div
            v-for="item in [1, 2, 3]"
            :key="item"
            class="flex flex-col md:flex-row justify-between"
          >
            <h3 class="text-lg text-left text-gray-700 md:text-xl mb-2 md:mb-0">
              2020.5.3
            </h3>
            <div class="w-full md:ml-12 hover:underline">
              CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始
            </div>
          </div>
        </div>

        <div
          class="absolute top-0 w-20 h-20 border-4 border-solid rounded-card-head news-overview-icon -mt-8"
        >
          <div class="relative">
            <div class="absolute w-2 h-2 mt-0 ml-6 bg-white rounded-full"></div>
            <div
              class="absolute w-2 h-2 mt-2 ml-12 bg-white rounded-full"
            ></div>
          </div>
        </div>
      </div>
    </section>

    <section
      class="flex flex-col items-center justify-center m-screen overview-area pt-12 pb-24 px-4"
    >
      <div class="flex flex-col items-center">
        <h2 class="inline text-3xl md:text-5xl mb-2">
          Overview
        </h2>
        <p class="text-xl md:text-2xl mb-8">-概要-</p>
      </div>
      <div
        class="relative flex flex-col justify-center items-center w-full container news-overview-content mt-6 bg-white"
      >
        <div
          class="relative w-4/5 flex justify-center flex-col z-10 bg-white space-y-6 py-8"
        >
          <div
            v-for="item in [1, 2, 3]"
            :key="item"
            class="flex flex-col md:flex-row justify-between"
          >
            <h3 class="text-lg text-left text-gray-700 md:text-xl mb-2 md:mb-0">
              2020.5.3
            </h3>
            <div class="w-full md:ml-12 hover:underline">
              CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始
            </div>
          </div>
        </div>
        <div
          class="absolute top-0 w-20 h-20 border-4 border-solid rounded-card-head news-overview-icon -mt-8"
        >
          <div class="relative">
            <div class="absolute w-2 h-2 mt-2 ml-4 bg-white rounded-full"></div>
            <div
              class="absolute w-2 h-2 mt-0 ml-10 bg-white rounded-full"
            ></div>
          </div>
        </div>
      </div>
    </section>

    <section class="flex flex-col items-center justify-center space-y-12">
      <div class="flex flex-col items-center justify-center my-24">
        <h2 class="inline text-3xl md:text-5xl">
          Session
        </h2>
      </div>
      <python-banner direction="right" back-ground-color="#3D40CB" size="small">
        <template #title>
          Keynote
        </template>
      </python-banner>

      <div class="flex flex-wrap justify-around">
        <talk-content class="w-full md:w-2/5" talk-type="talk"></talk-content>
        <talk-content
          class="w-full md:w-2/5 mt-10 md:mt-0"
          talk-type="talk"
        ></talk-content>
      </div>

      <python-banner direction="right" back-ground-color="#EE9D2C" size="small">
        <template #title>
          Invided talk
        </template>
      </python-banner>

      <div class="flex flex-wrap justify-around">
        <talk-content
          class="w-full md:w-2/5"
          talk-type="talk"
          main-color="orange"
        ></talk-content>
        <talk-content
          class="w-full md:w-2/5 mt-10 md:mt-0"
          talk-type="talk"
          main-color="orange"
        ></talk-content>
      </div>

      <python-banner direction="right" back-ground-color="#3F496A" size="small">
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

      <python-banner direction="right" back-ground-color="#71A4F1" size="small">
        <template #title>
          Platinum
        </template>
      </python-banner>

      <python-banner direction="right" back-ground-color="#E3AB4A" size="small">
        <template #title>
          Gold
        </template>
      </python-banner>

      <python-banner direction="right" back-ground-color="#818181" size="small">
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

      <p class="text-center">
        事前にFAQをご確認いただけますようにお願いします。 <br />
        ボランティアによる運営ですので、回答には1週間程度を要します。 <br />
        何卒お待ちいただけますようにお願いします。 <br />
      </p>
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
    TalkContent,
  },
  head() {
    return { title: 'PyCon JP 2020', titleTemplate: null }
  },
})
</script>

<style scoped>
.main-color {
  color: #404a6b;
  font-family: 'Rounded Mplus 1c';
}

.main-visual {
  /* background: linear-gradient(to bottom, #a6d900 0%, #ff4454 100%); */
  background-image: url('../assets/img/top-visual-icon.png');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center center;
}

.news-area {
  background-color: #d4d4ff;
}

.news-overview-content {
  border-style: solid;
  border-color: #404a6b;
  border-width: 8px;
  border-radius: 3rem;
}

.news-overview-icon {
  border-color: #404a6b;
  background-color: #404a6b;
}

.overview-area {
  background-color: #ffd8a1;
}

@media screen and (min-width: 768px) {
  .main-visual {
    width: 30vw;
  }
}
</style>
