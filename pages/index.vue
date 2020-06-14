<template>
  <div class="main-color">
    <section
      class="relative flex items-start justify-center mb-24 h-80 md:h-120 md:items-center"
    >
      <div class="z-50 mt-16 mr-2 md:m-0">
        <h1 class="text-4xl font-extrabold leading-tight md:text-6xl">
          PyCon JP <br />2020 <span class="font-semibold">Online</span>
        </h1>
        <h2 class="mt-6 text-2xl md:text-3xl">
          <i class="material-icons">location_on</i>
          Online Conference
        </h2>
        <h2 class="text-2xl md:text-3xl">
          <i class="text-gray-700 material-icons">event</i>
          <span class="font-semibold">2020 08/28 </span>(Fri.) /
          <span class="font-semibold">29 </span>(Sat.)
        </h2>
        <div class="flex">
          <img :src="require('~/assets/img/twitter.png')" class="h-8" />
          <a class="ml-2 text-xl text-blue-500">#pyconjp</a>
        </div>
      </div>
      <div
        class="absolute w-screen h-full opacity-25 md:opacity-100 main-visual md:w-50vw md:relative"
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

    <python-banner
      class="mb-24"
      direction="left"
      back-ground-color="#3D40CB"
      size="big"
    >
      <template #title>
        企業スポンサー様募集中
      </template>
      <template #content>
        PyCon JP 2020を応援して下さるスポンサー様を募集しております
      </template>
      <template #button>
        <button
          class="flex items-center px-4 py-2 mt-6 font-medium bg-white rounded-full shadow md:px-6 md:py-6 text-py-black"
        >
          <p class="w-6 h-6 rounded-full bg-py-blue-dark" />
          <span class="ml-2 md:text-xl md:ml-6 md:mr-4">
            スポンサーに申し込む
          </span>
        </button>
      </template>
    </python-banner>

    <python-banner direction="right" back-ground-color="#EE9D2C" size="big">
      <template #title>
        チケット販売開始
      </template>
      <template #content>
        PyCon JP 2020のチケット販売を開始しました！
      </template>
      <template #button>
        <button
          class="flex items-center px-4 py-2 mt-6 font-medium bg-white rounded-full shadow md:px-6 md:py-6 text-py-black"
        >
          <p class="w-6 h-6 rounded-full bg-py-orange-dark" />
          <span class="ml-2 md:text-xl md:ml-6 md:mr-4">
            チケットを購入する
          </span>
        </button>
      </template>
    </python-banner>

    <section
      class="flex flex-col items-center justify-center px-4 pt-12 pb-24 mt-24 m-screen news-area"
    >
      <div class="flex flex-col items-center">
        <h2 class="inline mb-2 text-4xl font-semibold md:text-6xl">
          NEWS
        </h2>
        <p class="mb-8 text-xl md:text-2xl">-お知らせ-</p>
      </div>
      <div
        class="relative flex flex-col items-center justify-center w-full mt-6 bg-white rounded-py news-overview-content"
      >
        <div
          class="relative z-10 flex flex-col justify-center w-4/5 py-8 space-y-6 bg-white rounded-py"
        >
          <div
            v-for="item in [1, 2, 3]"
            :key="item"
            class="flex flex-col justify-between md:flex-row"
          >
            <h3
              class="mb-2 text-lg font-medium text-left text-gray-700 md:text-xl md:mb-0"
            >
              2020.5.3
            </h3>
            <div class="w-full font-light md:ml-12 hover:underline">
              CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始
            </div>
          </div>
        </div>

        <div
          class="absolute top-0 w-20 h-20 -mt-8 border-4 border-solid rounded-card-head news-overview-icon"
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
      class="flex flex-col items-center justify-center px-4 pt-12 pb-24 m-screen overview-area"
    >
      <div class="flex flex-col items-center">
        <h2 class="inline mb-2 text-4xl font-semibold md:text-6xl">
          Overview
        </h2>
        <p class="mb-8 text-xl md:text-2xl">-概要-</p>
      </div>
      <div class="relative flex justify-center mt-6">
        <div
          class="absolute top-0 w-20 h-20 mx-auto -mt-8 border-4 border-solid rounded-card-head news-overview-icon"
        >
          <div class="relative">
            <div class="absolute w-2 h-2 mt-2 ml-4 bg-white rounded-full"></div>
            <div
              class="absolute w-2 h-2 mt-0 ml-10 bg-white rounded-full"
            ></div>
          </div>
        </div>
        <div
          class="flex flex-col items-center justify-center w-full overflow-hidden bg-white rounded-py news-overview-content"
        >
          <div
            class="relative z-10 flex flex-col justify-between w-full bg-white md:flex-row rounded-py"
          >
            <div class="flex flex-col flex-1 p-6 mx-2 md:mx-12">
              <h2 class="inline mb-2 text-2xl font-semibold md:text-4xl">
                What is PyConJP?
              </h2>
              <h3 class="mb-8 text-xl font-medium md:text-2xl">
                -PyConJpとは？-
              </h3>
              <p>
                PyConは、Pythonユーザが集まり、PythonやPythonを使ったソフトウェアについて情報交換、交流をするためのカンファレンスです。
                PyConJPの開催を通じて、Pythonの使い手が一堂に集まり、Pythonにまつわる様々な分野の知識や情報を交換し、新たな友達やコミュニティとのつながり、仕事やビジネスチャンスを増やせる場所とすることが目標です。
              </p>
              <button
                class="flex items-center self-center justify-center w-40 px-2 py-2 mt-6 font-medium bg-white rounded-full shadow md:w-64 md:px-6 md:py-6 text-py-black"
              >
                <p class="w-6 h-6 mr-auto rounded-full bg-py-blue-dark" />
                <span class="-ml-4 md:text-xl">
                  行動規範
                </span>
                <p class="mr-auto" />
              </button>
            </div>
            <img
              :src="require('~/assets/img/overview.png')"
              class="box-border object-cover object-left w-full h-64 md:h-auto md:w-2/5"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- <section class="flex flex-col items-center justify-center space-y-12">
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
          class="w-full mt-10 md:w-2/5 md:mt-0"
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
          class="w-full mt-10 md:w-2/5 md:mt-0"
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
    -->
  </div>
</template>

<script>
import Vue from 'vue'
import PythonBanner from '~/components/Elements/PythonBanner'
// import TalkContent from '~/components/Elements/TalkContent'

// const { parseString } = require('xml2js')

export default Vue.extend({
  components: {
    PythonBanner,
    // TalkContent,
  },
  async created() {
    // TODO: ブログの最新情報をAPIで取得する
    // const resp = await this.$axios.$get('/news')
    // parseString(resp, (err, result) => {
    //   console.log(result)
    //   console.error(err)
    // })
  },
  head() {
    return { title: 'PyCon JP 2020', titleTemplate: null }
  },
})
</script>

<style scoped>
.main-color {
  color: #404a6b;
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
