<template>
  <section
    class="relative flex items-start justify-center mb-12 md:items-center"
  >
    <div class="way-to-join-block">
      <div class="relative flex flex-col items-center justify-center">
        <div
          class="relative z-10 flex justify-center w-screen bg-white m-screen"
        >
          <div
            class="flex flex-col items-center w-11/12 px-6 border-8 border-solid sm:px-8 md:px-10 lg:px-12 lg:flex-row md:w-4/5 border-py-black rounded-xl"
          >
            <div class="w-10/12 mx-8 my-6 md:ml-10 text-tuto">
              <h2 class="inline mb-2 text-2xl font-semibold md:text-4xl">
                {{ $t('title') }}
              </h2>
              <div v-for="(paragraph, i) in $t('paragraphs')" :key="`p-${i}`">
                <p v-if="i != 'p-9'" class="my-4">
                  {{ paragraph }}
                </p>
                <a v-if="i === 'p-9'" :href="paragraph['link']">{{
                  paragraph['content']
                }}</a>
              </div>
            </div>
            <div class="inline-block w-8/12 mx-0 mb-6 lg:my-3 lg:ml-4 btn-tuto">
              <button
                class="flex items-center w-full px-4 py-2 font-medium duration-200 bg-white rounded-full shadow xl:w-9/12 xl:ml-10 transition-color group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none"
                @click="openConnpass('zoom')"
              >
                <p
                  class="w-6 h-6 rounded-full bg-py-black group-hover:bg-white"
                />
                <span
                  class="ml-2 md:text-xl md:ml-6 md:mr-4 group-hover:text-white"
                  >{{ $t('tutorial.zoom') }}</span
                >
              </button>
              <button
                class="flex items-center w-full px-4 py-2 mt-4 font-medium transition-colors duration-200 bg-white rounded-full shadow lg:mt-8 xl:w-9/12 xl:ml-10 group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none"
                @click="openConnpass('youtube')"
              >
                <p
                  class="w-6 h-6 rounded-full bg-py-black group-hover:bg-white"
                />
                <span
                  class="ml-2 md:text-xl md:ml-6 md:mr-4 group-hover:text-white"
                  >{{ $t('tutorial.youtube') }}</span
                >
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="absolute top-0 w-20 h-20 -mt-8 border-4 border-solid border-py-black bg-py-black rounded-card-head"
    >
      <div class="relative">
        <div class="absolute w-2 h-2 mt-2 ml-6 bg-white rounded-full"></div>
        <div class="absolute w-2 h-2 mt-2 ml-10 bg-white rounded-full"></div>
      </div>
    </div>
  </section>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  components: {},
  computed: {
    isEnglish() {
      return this.$i18n.locale === 'en'
    },
  },
  methods: {
    openConnpass(type) {
      if (type === 'youtube') {
        window.open('https://pyconjp.connpass.com/event/182390/', '_blank')
      } else {
        window.open('https://pyconjp.connpass.com/event/181065/', '_blank')
      }
    },
  },
  head() {
    return { title: 'チュートリアル' }
  },
})
</script>

<style scoped>
.attend-icon {
  border-color: #404a6b;
  background-color: #404a6b;
}

.attend-content {
  border-style: solid;
  border-color: #404a6b;
  border-width: 8px;
}

a {
  text-decoration: underline;
}
</style>

<i18n>
{
"en": {
    "title": "How to attend",
    "paragraphs": {
      "p-1": "You have 2 options to join tutorial.",
      "p-2": "・Join Zoom(including chance to ask questions to tutors. Limited for 20 people lottery selected)",
      "p-3": "・Join YouTube Live(you can only watch the tutorial.)",
      "p-4": "If you join Zoom, you need to prepare Zoom application.",
      "p-5": "We will tell you the Zoom link to join via connpass limeted section for participants.",
      "p-6": "Tutorial ticket does not include:",
      "p-7": "・Tickets for PyCon JP 2020 Conference(Aug. 28-29(JST))",
      "p-8": "For more details please check:",
      "p-9": {
        "link": "https://pyconjp.blogspot.com/2020/07/2020-tutorial.html",
        "content": "PyCon JP 2020 Blog post about the tutorial"
      },
      "p-10": "Tutorial classes will be held only in Japanese. We kindly ask for your understanding."
    },
    "tutorial": {
      "youtube": "Join Youtube Live",
      "zoom": "Join Zoom"
    }
  },
  "ja": {
    "title": "参加方法",
    "paragraphs": {
      "p-1": "本年度のチュートリアルには2種類の参加方法があります",
      "p-2": "・講師に質問できるZoom参加(限定20名、抽選)",
      "p-3": "・YouTube Live視聴のみの参加",
      "p-4": "Zoom参加の場合は環境構築の他、コミュニケーションツールとしてZoomの用意が必要です。",
      "p-5": "Zoomのアドレスについては後ほどconnpassの参加者情報欄でお伝えします。",
      "p-6": "また、以下のものは含まれません。",
      "p-7": "・カンファレンス（8/28~29）のZoom参加権",
      "p-8": "チュートリアルの詳細は",
      "p-9": {
        "link": "https://pyconjp.blogspot.com/2020/07/2020-tutorial.html",
        "content": "PyCon JP 2020 Blogのチュートリアル募集に関する記事"
      },
      "p-10": "をご覧下さい。"
    },
    "tutorial": {
      "youtube": "Youtube Live参加",
      "zoom": "Zoom参加"
    }
  }
}
</i18n>
