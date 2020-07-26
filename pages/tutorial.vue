<template>
  <section
    class="relative flex items-start justify-center mb-12 md:items-center"
  >
    <div class="description-block">
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
              <p
                v-for="(paragraph, i) in $t('paragraphs')"
                :key="`p-${i}`"
                class="my-4"
              >
                {{ paragraph }}
              </p>
            </div>
            <div class="inline-block w-8/12 mx-0 mb-6 lg:my-3 lg:ml-4 btn-tuto">
              <button
                class="flex items-center w-full px-4 py-2 font-medium duration-200 bg-white rounded-full shadow xl:w-9/12 xl:ml-10 transition-color group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none"
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
  head() {
    return { title: this.$t('pages.code-of-conduct.title') }
  },
})
</script>
<style scoped>
.overview-area {
  background-color: #ffd8a1;
}

.attend-icon {
  border-color: #404a6b;
  background-color: #404a6b;
}

.attend-content {
  border-style: solid;
  border-color: #404a6b;
  border-width: 8px;
}
</style>

<i18n>
{
"en": {
    "title": "How to attend",
    "paragraphs": {
      "p-1": "本年度のチュートリアルには2種類の参加方法があります",
      "p-2": "・講師に質問できるZoom参加",
      "p-3": "また、以下のものは含まれません"
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
      "p-2": "・講師に質問できるZoom参加(限定20名、抽選)・YouTube Live視聴のみの参加Zoom参加の場合は環境構築の他、コミュニケーションツールとしてZoomの用意が必要です。Zoomのアドレスについては後ほど参加者情報の蘭でお伝えします。",
      "p-3": "また、以下のものは含まれません。・カンファレンス（8/28~29）のZoom参加権チュートリアルの詳細は<a></a>をご覧下さい。"
    },
    "tutorial": {
      "youtube": "Youtube Live参加",
      "zoom": "Zoom参加"
    }
  }
}
</i18n>
