<template>
  <div>
    <div class="flex flex-col items-center justify-center h-32 md:h-56">
      <h1
        class="flex items-center justify-center w-screen text-2xl font-semibold text-center text-py-black sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >
        Special Booth
      </h1>
      <h3
        class="flex items-center justify-center w-screen mb-8 text-lg font-semibold text-center text-py-black sm:text-xl md:text-2xl lg:text-3xl m-screen"
      >
        {{ $t('pages["event-list"]["content-list"][1].title') }}
      </h3>
    </div>
    <div>
      <p>
        タイムテーブル よろしくお願いします
      </p>
    </div>
    <div>
      <div class="flex flex-wrap items-start justify-center mt-8 mb-16">
        <Sponsor
          v-for="sponsor in $t('special-booth-company-list')"
          :key="sponsor.companyName"
          sponsor-type="gold"
          :url="sponsor.url"
          class="w-full mt-10 lg:w-1/4 lg:mx-8"
          color="#3D40CB"
        >
          <template #image>
            <img
              :src="require(`~/assets/img/sponsor/${sponsor.imagePath}`)"
              class="w-3/4"
            />
          </template>
          <template #companyName class="text-lg">
            {{ sponsor.companyName }}
          </template>
          <!-- <template #companyInformation>
          {{ tutorial.description }}
        </template> -->
        </Sponsor>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import Sponsor from '~/components/Domains/SpecialBooth/sponsor'

export default Vue.extend({
  components: { Sponsor },
  data() {
    return {}
  },
})
</script>

<style></style>

<i18n>
{
  "en": {
    "special-booth-company-list": [
      {
        "companyName": "Leading Edge Co.,Ltd",
        "url": "https://startlab.jp/",
        "imagePath": "platinum1.jpg"
      },
      {
        "companyName": "HENNGE K.K.",
        "url": "https://hennge.com/jp/",
        "imagePath": "platinum2.jpg"
      },
      {
        "companyName": "Microsoft Japan Co., Ltd.",
        "url": "https://azure.microsoft.com/ja-jp/",
        "imagePath": "platinum3.png"
      },
      {
        "companyName": "Python Engineer Development Association",
        "url": "https://www.pythonic-exam.com/",
        "imagePath": "gold1.png"
      },
      {
        "companyName": "iRidge, Inc.",
        "url": "https://iridge.jp/",
        "imagePath": "gold2.jpg"
      },
      {
        "companyName": "BrainPad Inc.",
        "url": "https://www.brainpad.co.jp/",
        "imagePath": "gold3.png"
      },
      {
        "companyName": "e-Seikatsu Co., Ltd.",
        "url": "https://www.e-seikatsu.info/",
        "imagePath": "gold4.png"
      },
      {
        "companyName": "VisasQ Inc.",
        "url": "https://visasq.co.jp/",
        "imagePath": "gold5.png"
      },
      {
        "companyName": "JSL",
        "url": "https://jsl.co.jp",
        "imagePath": "gold6.png"
      },
      {
        "companyName": "LegalForce, Inc.",
        "url": "https://www.legalforce.co.jp/",
        "imagePath": "gold7.png"
      },
      {
        "companyName": "Johnson & Johnson K.K.",
        "url": "https://www.jnj.co.jp/",
        "imagePath": "gold8.png"
      },
      {
        "companyName": "Cheerio Corporation Co., LTD",
        "url": "https://www.cheerio.co.jp/",
        "imagePath": "special1.jpg"
      },
      {
        "companyName": "SHOEISHA Co.,Ltd.",
        "url": "https://codezine.jp/",
        "imagePath": "media5.png"
      }
    ]
  },
  "ja": {
    "special-booth-company-list": [
      {
        "companyName": "株式会社リーディング・エッジ社（Python Start Lab Online）",
        "url": "https://startlab.jp/",
        "imagePath": "platinum1.jpg"
      },
      {
        "companyName": "HENNGE株式会社",
        "url": "https://hennge.com/jp/",
        "imagePath": "platinum2.jpg"
      },
      {
        "companyName": "日本マイクロソフト株式会社",
        "url": "https://azure.microsoft.com/ja-jp/",
        "imagePath": "platinum3.png"
      },
      {
        "companyName": "一般社団法人Pythonエンジニア育成推進協会",
        "url": "https://www.pythonic-exam.com/",
        "imagePath": "gold1.png"
      },
      {
        "companyName": "株式会社アイリッジ",
        "url": "https://iridge.jp/",
        "imagePath": "gold2.jpg"
      },
      {
        "companyName": "株式会社ブレインパッド",
        "url": "https://www.brainpad.co.jp/",
        "imagePath": "gold3.png"
      },
      {
        "companyName": "株式会社いい生活",
        "url": "https://www.e-seikatsu.info/",
        "imagePath": "gold4.png"
      },
      {
        "companyName": "株式会社ビザスク",
        "url": "https://visasq.co.jp/",
        "imagePath": "gold5.png"
      },
      {
        "companyName": "株式会社日本システム技研",
        "url": "https://jsl.co.jp",
        "imagePath": "gold6.png"
      },
      {
        "companyName": "株式会社LegalForce",
        "url": "https://www.legalforce.co.jp/",
        "imagePath": "gold7.png"
      },
      {
        "companyName": "ジョンソン・エンド・ジョンソン 日本法人グループ",
        "url": "https://www.jnj.co.jp/",
        "imagePath": "gold8.png"
      },
      {
        "companyName": "株式会社チェリオコーポレーション",
        "url": "https://www.cheerio.co.jp/",
        "imagePath": "special1.jpg"
      },
      {
        "companyName": "株式会社翔泳社",
        "url": "https://codezine.jp/",
        "imagePath": "media5.png"
      }
    ]
  }
}

</i18n>
