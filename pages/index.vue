<template>
  <div class="main-color">
    <section
      class="relative flex items-start justify-center mb-12 h-80 md:h-120 md:items-center"
    >
      <div class="relative z-50 mt-16 mr-2 md:m-0">
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
          <a
            class="ml-2 text-xl text-blue-500"
            href="https://twitter.com/search?q=%23pyconjp&src=typed_query"
            target="_blank"
            rel="noopener noreferrer"
            >#pyconjp</a
          >
        </div>
      </div>
      <div
        class="absolute w-screen h-full opacity-25 md:opacity-100 main-visual md:w-50vw md:relative"
      >
        <div
          class="absolute hidden rounded-full balloon-1 bg-py-blue-light md:block"
        ></div>
        <div
          class="absolute hidden rounded-full balloon-2 bg-py-orange-light md:block"
        ></div>
        <div
          class="absolute hidden rounded-full balloon-3 bg-py-orange-light md:block"
        ></div>
      </div>
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
        {{ $t('sponsor.title') }}
      </template>
      <template #content>
        {{ $t('sponsor.content') }}
      </template>
      <template #button>
        <a
          class="mt-6"
          href="https://pyconjp.blogspot.com/2020/06/2nd-period-of-sponsorship-application.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          <button
            class="flex items-center px-4 py-2 font-medium bg-white rounded-full shadow group md:px-6 md:py-6 text-py-black hover:bg-py-blue-dark focus:outline-none"
          >
            <p
              class="w-6 h-6 rounded-full bg-py-blue-dark group-hover:bg-white"
            />
            <span
              class="ml-2 md:text-xl md:ml-6 md:mr-4 group-hover:text-white"
            >
              {{ $t('sponsor.button') }}
            </span>
          </button>
        </a>
      </template>
    </python-banner>

    <python-banner direction="right" back-ground-color="#EE9D2C" size="big">
      <template #title>
        {{ $t('ticket.title') }}
      </template>
      <template #content>
        {{ $t('ticket.content') }}
      </template>
      <template #button>
        <button
          class="relative flex items-center px-4 py-2 mt-6 font-medium bg-white rounded-full shadow pointer-events-none md:px-6 md:py-6 text-py-black focus:outline-none"
        >
          <p class="w-6 h-6 rounded-full bg-py-orange-dark" />
          <span class="ml-2 md:text-xl md:ml-6 md:mr-4">
            {{ $t('ticket.button') }}
          </span>

          <img
            class="absolute left-0 w-full"
            :src="require('~/assets/img/comming-soon.png')"
            alt="commingSoon"
          />
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
        <p class="mb-8 text-xl md:text-2xl">{{ $t('news.subtitle') }}</p>
      </div>
      <div
        class="relative flex flex-col items-center justify-center w-full mt-6 bg-white md:w-3/4 rounded-py news-overview-content"
      >
        <div
          class="relative z-10 flex flex-col justify-center w-4/5 py-8 space-y-6 bg-white rounded-py"
        >
          <div
            v-for="(item, i) in newsContents"
            :key="i"
            class="flex flex-col justify-between md:flex-row"
          >
            <h3
              class="mb-2 text-lg font-medium text-left text-gray-700 md:text-xl md:mb-0"
            >
              {{ item.date }}
            </h3>
            <a
              class="w-full font-light md:ml-12 hover:underline"
              :href="item.link"
              target="_blank"
              rel="noopener noreferrer"
            >
              {{ item.title }}
            </a>
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
            <div class="absolute text-5xl font-bold emotion-mark">
              !
            </div>
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
        <p class="mb-8 text-xl md:text-2xl">{{ $t('overview.subtitle') }}</p>
      </div>
      <div class="relative flex justify-center w-full mt-6 md:w-3/4">
        <div
          class="absolute top-0 w-20 h-20 mx-auto -mt-8 border-4 border-solid rounded-card-head news-overview-icon"
        >
          <div class="relative">
            <div class="absolute w-2 h-2 mt-2 ml-4 bg-white rounded-full"></div>
            <div
              class="absolute w-2 h-2 mt-0 ml-10 bg-white rounded-full"
            ></div>
            <div class="absolute text-5xl font-bold emotion-mark">
              ?
            </div>
          </div>
        </div>
        <div
          class="flex flex-col items-center justify-center w-full overflow-hidden bg-white rounded-py news-overview-content"
        >
          <div
            class="relative z-10 flex flex-col justify-between w-full bg-white lg:flex-row rounded-py"
          >
            <div class="flex flex-col flex-1 p-6 mx-2 md:mx-12">
              <h2 class="inline mb-2 text-2xl font-semibold md:text-4xl">
                What is PyConJP?
              </h2>
              <h3 class="mb-8 text-xl font-medium md:text-2xl">
                {{ $t('overview.contentTitle') }}
              </h3>
              <p>
                {{ $t('overview.content') }}
              </p>
              <nuxt-link to="/code-of-conduct" class="self-center">
                <button
                  class="flex items-center self-center justify-center w-40 px-2 py-2 mt-6 font-medium bg-white rounded-full shadow group md:w-64 md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none"
                >
                  <p
                    class="w-6 h-6 mr-auto rounded-full bg-py-black group-hover:bg-white"
                  />
                  <span class="-ml-4 md:text-xl group-hover:text-white">
                    {{ $t('overview.button') }}
                  </span>
                  <p class="mr-auto" />
                </button>
              </nuxt-link>
            </div>
            <img
              :src="require('~/assets/img/overview.jpg')"
              class="box-border object-cover object-left w-full h-64 md:h-auto lg:w-2/5"
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
  data() {
    return {
      newsContents: [
        {
          date: '2020.06.10',
          title:
            'PyCon JP 2020 スタッフ全体オンラインミーティング(6月)を開催しました！',
          link: 'https://pyconjp.blogspot.com/2020/06/pycon-jp-2020-6.html',
        },
        {
          date: '2020.06.08',
          title:
            'PyCon JP 2020 スポンサー募集 2次募集期間開始のお知らせ / Sponsorship Application 2nd-Period starts',
          link:
            'https://pyconjp.blogspot.com/2020/06/2nd-period-of-sponsorship-application.html',
        },
        {
          date: '2020.06.05',
          title:
            'PyCon JP 2020 Sponsorship Application FAQ / PyCon JP 2020の良くある問い合わせ/スポンサーシップ1次募集は本日まで!',
          link:
            'https://pyconjp.blogspot.com/2020/06/pycon-jp-2020-sponsorship-faq.html',
        },
        {
          date: '2020.06.02',
          title:
            'PyCon JP 2020: 2日目のキーノートスピーカー決定のお知らせ/ Announcement of Keynote Speaker on Day 2',
          link:
            'https://pyconjp.blogspot.com/2020/06/pycon-jp-2020-2-announcement-of-keynote.html',
        },
      ],
    }
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

.emotion-mark {
  top: -2.5rem;
  left: 5rem;
}

.balloon-1 {
  height: 110px;
  left: -520px;
  top: 24px;
  width: 110px;
}

.balloon-2 {
  bottom: -100px;
  height: 184px;
  left: -240px;
  width: 184px;
}

.balloon-3 {
  bottom: 0;
  height: 110px;
  right: -100px;
  width: 110px;
}
</style>

<i18n>
{
  "en": {
    "sponsor": {
      "title": "Looking for corporate sponsors",
      "content": "We are looking for sponsors to support PyCon JP 2020.",
      "button": "Apply for Sponsor"
    },
    "ticket": {
      "title": "Ticket sales start",
      "content": "Ticket sales for PyCon JP 2020 have started!",
      "button": "Buy a ticket"
    },
    "news": {
      "subtitle": "-news-"
    },
    "overview": {
      "subtitle": "-overview-",
      "contentTitle": "-What is PyConJP?-",
      "content": "PyCon is a conference for Python users to gather, exchange information and interact with Python and software using Python. Through PyCon JP, the goal is to gather Python users together, exchange knowledge and information on various fields related to Python, connect with new friends and communities, and increase work and business opportunities.",
      "button": "Code of conduct"
    }
  },
  "ja": {
    "sponsor": {
      "title": "企業スポンサー様募集中",
      "content": "PyCon JP 2020を応援して下さるスポンサー様を募集しております",
      "button": "スポンサーに申し込む"
    },
    "ticket": {
      "title": "チケット販売開始",
      "content": "PyCon JP 2020のチケット販売を開始しました！.",
      "button": "チケットを購入する"
    },
    "news": {
      "subtitle": "-お知らせ-"
    },
    "overview": {
      "subtitle": "-概要-",
      "contentTitle": "-PyConJpとは？-",
      "content": "PyConは、Pythonユーザが集まり、PythonやPythonを使ったソフトウェアについて情報交換、交流をするためのカンファレンスです。PyConJPの開催を通じて、Pythonの使い手が一堂に集まり、Pythonにまつわる様々な分野の知識や情報を交換し、新たな友達やコミュニティとのつながり、仕事やビジネスチャンスを増やせる場所とすることが目標です。",
      "button": "行動規範"
    }
  }
}
</i18n>
