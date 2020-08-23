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
    <div class="w-screen pt-24 pb-24 way-to-join-block m-screen text-py-black">
      <div
        class="relative flex items-start justify-center md:items-center way-to-join-block"
      >
        <div class="relative flex flex-col items-center justify-center">
          <div class="relative z-10 flex justify-center w-screen m-screen">
            <div
              class="flex flex-col items-center w-11/12 px-6 border-8 border-solid sm:px-8 md:px-10 lg:px-12 lg:flex-row md:w-4/5 border-py-black rounded-xl way-to-join-content"
            >
              <div class="w-10/12 mx-8 my-6 md:ml-10">
                <h2 class="inline mb-2 text-2xl font-semibold md:text-4xl">
                  {{ $t('stamp-rally.title') }}
                </h2>
                <div>
                  <p class="my-4">
                    {{ $t('stamp-rally.paragraphs.p-1') }}
                  </p>
                  <p class="my-4">
                    {{ $t('stamp-rally.paragraphs.p-2') }}
                  </p>
                  <p class="my-4">
                    {{ $t('stamp-rally.paragraphs.p-3') }}
                  </p>
                  <p class="my-4">
                    {{ $t('stamp-rally.paragraphs.p-4') }}
                    <a
                      href="https://docs.google.com/document/d/1iqGOJiB6QrFPZdIQn4baSGTtm9bHsO2JO7ZCs2d7qfE/edit?usp=sharing"
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {{ $t('stamp-rally.paragraphs.p-5') }}</a
                    >
                    {{ $t('stamp-rally.paragraphs.p-6') }}
                  </p>
                </div>
                <p class="my-4">
                  {{ $t('stamp-rally.paragraphs.p-7') }}
                </p>
              </div>
            </div>
          </div>
        </div>
        <div
          class="absolute top-0 w-20 h-20 -mt-8 border-4 border-solid border-py-black bg-py-black rounded-card-head"
        >
          <div class="relative">
            <div class="absolute w-2 h-2 mt-2 ml-6 bg-white rounded-full"></div>
            <div
              class="absolute w-2 h-2 mt-2 ml-10 bg-white rounded-full"
            ></div>
          </div>
        </div>
      </div>
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

<style scoped>
section {
  color: #404a6b;
}
a:link,
a:visited {
  color: #006edb;
  text-decoration: underline;
  cursor: pointer;
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
.balloon-1 {
  height: 110px;
  left: 340px;
  top: -620px;
  width: 110px;
  z-index: -1;
}
.balloon-2 {
  bottom: 130px;
  height: 110px;
  right: 100px;
  width: 110px;
  z-index: -1;
}
.way-to-join-block {
  background-color: #ffd8a1;
}
.way-to-join-content {
  background-color: #ffffff;
}
.date-block .date-text span {
  color: #3d40cb;
}
.text-indent-one {
  text-indent: -1em;
  padding-left: 2em;
}
.text-indent-two {
  text-indent: -2em;
  padding-left: 4em;
}
</style>

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
    ],
    "stamp-rally":{
      "title": "Online Stamp Rally",
      "paragraphs": {
        "p-1": "We will be holding an online stamp rally with prizes for participating in a special booth to collect words and great prizes donated by our sponsors!",
        "p-2": "All you have to do is visit the special booth, collect words, and apply for the contest using the special application form.The more words you submit, you may more likely get premiums.",
        "p-3": "As a award for participation, you will receive a limited edition PyConJP2020 virtual background and a coupon to be used at the SHOEISYA online store.",
        "p-4":"Check",
        "p-5": "Here（Google Documents）",
        "p-6": "for more information on events and great prizes!",
        "p-7":"※ Only those who have purchased tickets on PyConJP2020 Connpass will be able to attend this event."
      }
    }
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
    ],
    "stamp-rally":{
      "title": "オンラインスタンプラリー",
      "paragraphs": {
        "p-1": "スペシャルブースであいことばを集めて、参加賞とスポンサーの方からご提供頂いた豪華景品が抽選であたるオンラインスタンプラリーを開催します！",
        "p-2": "参加方法はスペシャルブースを訪問し、あいことばを集めて、専用の応募フォームにて応募するだけ。あいことばが合っている企業が多ければ多いほど、抽選の当選確率が上がります。",
        "p-3": "参加賞として、PyConJP2020限定バーチャル背景と翔泳社のオンラインストアで利用できるクーポンをプレゼントいたします。",
        "p-4":"イベントや豪華景品の詳細ついては",
        "p-5": "こちら（Googleドキュメント）",
        "p-6": "をご確認ください。",
        "p-7":"※本イベントの参加者は、PyConJP2020のConnpass にてチケット購入をされている方に限ります"
      }
    }
  }
}

</i18n>
