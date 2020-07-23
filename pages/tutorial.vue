<template>
  <section
    class="relative flex items-start justify-center mb-12 h-80 md:h-120 md:items-center"
  >
    <div class="hero-block"></div>
    <div class="way-to-join-block">
      <section
        class="flex flex-col items-center justify-center px-4 pt-12 pb-24 m-screen"
      >
        <div class="relative flex justify-center w-full mt-6 md:w-3/4">
          <div
            class="absolute top-0 w-20 h-20 mx-auto -mt-8 border-4 border-solid rounded-card-head attend-icon"
          >
            <div class="relative">
              <div
                class="absolute w-2 h-2 mt-2 ml-4 bg-white rounded-full"
              ></div>
              <div
                class="absolute w-2 h-2 mt-2 ml-10 bg-white rounded-full"
              ></div>
            </div>
          </div>
          <div
            class="flex flex-col items-center justify-center w-full overflow-hidden bg-white rounded-py attend-content"
          >
            <div
              class="relative z-10 flex flex-col justify-between w-full bg-white lg:flex-row rounded-py"
            >
              <div class="flex flex-col flex-1 px-6 py-12 sm:px-10 md:px-16">
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
                <button
                  class="flex items-center self-center justify-center px-2 py-2 mt-6 font-medium duration-200 bg-white rounded-full shadow group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none transition-color"
                >
                  <p
                    class="w-6 h-6 rounded-full bg-py-black group-hover:bg-white"
                  />
                  <span class="mx-4 md:text-xl group-hover:text-white">
                    {{ $t('tutorial.zoom') }}
                  </span>
                </button>
                <button
                  class="flex items-center self-center justify-center px-2 py-2 mt-6 font-medium duration-200 bg-white rounded-full shadow group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none transition-color"
                >
                  <p
                    class="w-6 h-6 rounded-full bg-py-black group-hover:bg-white"
                  />
                  <span class="mx-4 md:text-xl group-hover:text-white">
                    {{ $t('tutorial.youtube') }}
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <div class="description-block">
      <div class="event-one"></div>
      <div class="event-two"></div>
    </div>
  </section>
</template>
<script>
import Vue from 'vue'

export default Vue.extend({
  components: {},
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
      "p-2": "・講師に質問できるZoom参加(限定20名、抽選)・",
      "p-3": "また、以下のものは含まれません"
    },
    "tutorial": {
      "youtube": "Youtube Live参加",
      "zoom": "Zoom参加"
    }
  }
}
</i18n>
