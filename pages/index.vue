<template>
  <div>
    <div class="flex flex-col items-center justify-center h-80 md:h-120">
      <div
        class="flex md:items-center items-start justify-center h-full w-screen relative"
      >
        <div class="mr-2 z-10 mt-16 md:m-0">
          <h1 class="text-4xl  md:text-6xl font-bold leading-tight">
            PyCon JP <br />2020
          </h1>
          <h2 class="text-2xl md:text-3xl mt-6">
            <i class="material-icons text-red-400">location_on</i> Online
            Conference
          </h2>
          <h2 class="text-2xl md:text-3xl">
            <i class="material-icons text-red-400">event</i> August 28(Fri.) /
            29(Sat.)
          </h2>
        </div>
        <div
          class="main-visual main-visual-width md:opacity-50 opacity-25  h-full w-screen absolute md:relative"
          rel="https://www.ac-illust.com/main/detail.php?id=496603&word=%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E9%87%91%E9%AD%9A%E5%A4%8F%E7%A5%AD%E3%82%8A%E7%B8%81%E6%97%A5%E9%A3%BE%E3%82%8A%E5%92%8C%E9%A2%A8%E6%89%8B%E6%9B%B8%E3%81%8D%E5%8B%95%E7%89%A9"
        ></div>
      </div>
    </div>

    <!-- <div class="flex flex-col items-center justify-center">
      <div
        class=" border-double border-8 border-blue-600 my-16 w-3/4 rounded-lg py-4"
      >
        <div class="flex">
          <div class="w-1/4 flex items-center justify-center">
            <font-awesome-icon
              :icon="['far', 'handshake']"
              class="text-5xl opacity-50"
            />
          </div>
          <div
            class="w-2/3 flex  flex-col items-center justify-center border-l-2 border-blue-500"
          >
            <h2 class="text-xl md:text-3xl">スポンサー募集中</h2>
            <p>詳しくはこちら</p>
          </div>
        </div>
      </div>
    </div> -->

    <div
      class="w-screen top-news bg-blue-500 m-screen h-48  md:h-48 p-6 my-8 md:ml-auto"
    >
      <h1
        class="text-white text-2xl md:text-4xl border-b-2 border-white inline"
      >
        企業スポンサー様募集中
      </h1>
      <p class="text-white mt-6 text-lg md:text-xl">
        PyCon JP 2020を応援して下さるスポンサー様を募集しております<br />
        <span class=" hover:underline">> 詳細はこちらから</span>
      </p>
    </div>
    <div
      class="w-screen flex flex-col items-end top-news bg-green-500 m-screen  h-48  md:h-48 p-6 my-8 "
    >
      <h1
        class="text-white text-2xl md:text-4xl border-b-2 border-white inline"
      >
        チケット販売開始
      </h1>
      <p class="text-white mt-6 text-lg md:text-xl">
        PyCon JP 2020のチケット販売を開始しました！<br />
        <span class=" hover:underline">> 詳細はこちらから</span>
      </p>
    </div>

    <div
      class="flex flex-col items-center justify-center md:items-start md:justify-start mt-112 mb-8"
    >
      <h1
        class="text-3xl md:text-5xl border-solid border-b-8 border-blue-600 inline"
      >
        NEWS
      </h1>
    </div>
    <div
      v-for="item in [1, 2, 3]"
      :key="item"
      class="flex border-solid border-b-2 border-gray-200 w-full mt-4 w-full md:w-4/5"
    >
      <div class="w-1/5 text-left">2020.5.3</div>
      <div class="w-3/5 md:w-full ml-4 md:m-0 hover:underline">
        CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始>CFP募集開始
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
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

@media screen and (min-width: 768px) {
  .main-visual-width {
    width: calc(100vw / 2);
  }
}

@media screen and (min-width: 768px) {
  .top-news {
    width: 80vw;
  }
}
</style>
