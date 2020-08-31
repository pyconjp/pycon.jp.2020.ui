<template>
  <div class="flex flex-col items-center justify-center my-10">
    <h1 class="mb-4 text-xl md:text-4xl">PyCon JP 2020 配信ページ一覧</h1>
    <div
      class="flex flex-col flex-wrap items-center justify-center w-11/12 md:flex-row"
    >
      <div
        v-for="sessionData in sessionDataList"
        :key="sessionData.message"
        class="relative flex w-full border border-gray-700 md:w-1/2"
      >
        <div class="flex items-end w-1/4">
          <p class="ml-2">{{ sessionData.message }}</p>
        </div>
        <div class="youtube">
          <iframe
            id="player"
            class="iframe"
            type="text/html"
            width="420"
            height="360"
            :src="sessionData.url"
            frameborder="0"
          ></iframe>
        </div>

        <!-- <img
          :src="require(`~/assets/img/${sessionData.image}`)"
          class="relative w-3/4"
        /> -->
        <p class="float_message">イベントは終了しました</p>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
export default Vue.extend({
  components: {},
  data() {
    return {
      sessionDataList: [
        {
          message: 'Keynote',
          url: 'https://www.youtube.com/embed/-ewM4Wz50wA',
        },
        {
          message: 'Session 1',
          url: 'https://www.youtube.com/embed/7HCJD4oxfuo',
        },
        {
          message: 'Session 2',
          url: 'https://www.youtube.com/embed/qbsJY3M7eIo',
        },
        {
          message: 'Session 3',
          url: 'https://www.youtube.com/embed/-IxP81W4D24',
        },
        {
          message: 'Session 4',
          url: 'https://www.youtube.com/embed/1hw6AIzqehk',
        },
        {
          message: 'Session 5',
          url: 'https://www.youtube.com/embed/krnaOxKRhoQ',
        },
      ],
    }
  },
  methods: {},
  head() {
    return { title: 'PyCon JP 2020', titleTemplate: null }
  },
})
</script>

<style>
.float_message {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  background-color: white;
  border: 0.5rem;
  color: red;
  font-weight: 800;
  border-color: red;
  font-size: 1.5rem;
}

.youtube {
  position: relative;
  width: 100%;
  overflow: hidden;
  padding-bottom: 56.25%;
}

.youtube iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none; /*境界線の打ち消し*/
}
</style>
