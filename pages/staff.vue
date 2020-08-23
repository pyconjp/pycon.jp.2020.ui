<template>
  <div>
    <div class="flex flex-col items-center justify-center h-32 md:h-56">
      <h1
        class="flex items-center justify-center w-screen text-2xl font-semibold text-center text-py-black sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >
        Staff
      </h1>
      <h3
        class="flex items-center justify-center w-screen mb-8 text-lg font-semibold text-center text-py-black sm:text-xl md:text-2xl lg:text-3xl m-screen"
      >
        {{ $t('pages["staff"].title') }}
      </h3>
    </div>
    <div>
      <python-banner direction="right" back-ground-color="#3D40CB" size="small">
        <template #title>
          Core Staff
        </template>
      </python-banner>
      <div class="grid grid-flow-row grid-cols-1 mt-4 md:grid-cols-3">
        <div
          v-for="staff in $t('core-staff-list')"
          :key="staff.name"
          class="p-3 m-4 rounded-lg staff-box-shawow"
        >
          <div class="flex items-center">
            <img
              v-if="staff.photo !== ''"
              :src="staff.photo"
              class="object-fill w-12 h-12 mr-3 rounded-full"
              alt=""
            />
            <i
              v-if="staff.photo === ''"
              class="mr-3 text-5xl text-gray-700 material-icons"
              >account_circle</i
            >
            <p class="text-xl">{{ staff.name }}</p>
          </div>
          <div class="flex items-center space-x-2">
            <div class="mr-auto">{{ staff.title }}</div>
            <a
              v-if="staff.twitter"
              rel="noopener noreferrer"
              target="_blank"
              :href="`https://twitter.com/${staff.twitter}`"
              class="text-3xl titter-color"
            >
              <fa :icon="faTwitter" />
            </a>
            <a
              v-if="staff.facebook"
              rel="noopener noreferrer"
              target="_blank"
              :href="`https://facebook.com/${staff.facebook}`"
              class="text-3xl facebook-color"
            >
              <fa :icon="faFacebook" />
            </a>
          </div>
        </div>
      </div>
      <python-banner direction="right" back-ground-color="#EE9D2C" size="small">
        <template #title>
          Support Staff
        </template>
      </python-banner>
      <div class="grid grid-flow-row grid-cols-1 mt-4 md:grid-cols-3">
        <div
          v-for="staff in $t('support-staff-list')"
          :key="staff.name"
          class="p-3 m-4 rounded-lg staff-box-shawow"
        >
          <div class="flex items-center">
            <img
              v-if="staff.photo !== ''"
              :src="staff.photo"
              class="w-12 h-12 mr-3 rounded-full"
              alt=""
            />
            <i
              v-if="staff.photo === ''"
              class="mr-3 text-5xl text-gray-700 material-icons"
              >account_circle</i
            >
            <p class="text-xl">{{ staff.name }}</p>
          </div>
          <div class="flex items-center space-x-2">
            <div class="mr-auto">{{ staff.title }}</div>
            <a
              v-if="staff.twitter"
              rel="noopener noreferrer"
              target="_blank"
              :href="`https://twitter.com/${staff.twitter}`"
              class="text-3xl titter-color"
            >
              <fa :icon="faTwitter" />
            </a>
            <a
              v-if="staff.facebook"
              rel="noopener noreferrer"
              target="_blank"
              :href="`https://facebook.com/${staff.facebook}`"
              class="text-3xl facebook-color"
            >
              <fa :icon="faFacebook" />
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import { faTwitter, faFacebook } from '@fortawesome/free-brands-svg-icons'
import PythonBanner from '~/components/Elements/PythonBanner'

export default Vue.extend({
  components: { PythonBanner },
  computed: {
    faTwitter() {
      return faTwitter
    },
    faFacebook() {
      return faFacebook
    },
  },
  head() {
    return { title: this.$t('pages.staff.title') }
  },
})
</script>

<style>
.staff-box-shawow {
  box-shadow: 0px 3px 6px #00000029;
}

.titter-color {
  color: #1da1f2;
}
.facebook-color {
  color: #4267b2;
}
</style>

<i18n>
{
  "en": {
    "core-staff-list": [
      {
        "name": "Yoshiro Nishimura",
        "title": "Chair",
        "photo": "",
        "twitter": "",
        "facebook": "yoshiro.nishimura.9"
      },
      {
        "name": "Daisuke Saito",
        "title": "Vice Chair",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Daisuke_Saito.jpg",
        "twitter": "PCShop_kabu",
        "facebook": "ds110.sai"
      },
      {
        "name": "Shunsuke Yoshida",
        "title": "Adviser",
        "photo": "https://www.pycon.jp/_images/yoshida.png",
        "twitter": "koedoyoshida",
        "facebook": "koedoyoshida"
      },
      {
        "name": "Manabu TERADA",
        "title": "Board Chair",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Manabu_TERADA.png",
        "twitter": "terapyon",
        "facebook": "terapyon"
      },
      {
        "name": "Iosif Takakura",
        "title": "",
        "photo": "",
        "twitter": "huideyeren",
        "facebook": "iosif.takakura.yusuke"
      },
      {
        "name": "nikkie",
        "title": "Content Team Leader",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/nikkie.jpg",
        "twitter": "ftnext",
        "facebook": ""
      },
      {
        "name": "Takumi Kuramoto",
        "title": "",
        "photo": "",
        "twitter": "try",
        "facebook": ""
      },
      {
        "name": "Kouji Ueki",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "hanai",
        "title": "Secretariat team leader",
        "photo": "",
        "twitter": "hanahiro_aze",
        "facebook": "hiroyuki.hanai.71"
      },
      {
        "name": "yousuke nakabayashi",
        "title": "",
        "photo": "",
        "twitter": "elaborateplan",
        "facebook": ""
      },
      {
        "name": "Akira Inamori",
        "title": "",
        "photo": "",
        "twitter": "ainamori",
        "facebook": "ainamori01"
      },
      {
        "name": "eda3",
        "title": "",
        "photo": "",
        "twitter": "eda3__",
        "facebook": ""
      },
      {
        "name": "Manami Matsuura",
        "title": "",
        "photo": "https://avatars2.githubusercontent.com/u/35416089?s=400&u=320bbe5913dc12efd6dd88d03e3e199b6a4fa5a1&v=4",
        "twitter": "mtmn07384",
        "facebook": "manami.matsuura.227"
      },
      {
        "name": "natsu",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Masaru Irisawa",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Rei Suyama",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Masataka Arai",
        "title": "",
        "photo": "",
        "twitter": "massa142",
        "facebook": "mstk214"
      },
      {
        "name": "Jonas Obrist",
        "title": "Board Member",
        "photo": "",
        "twitter": "ojiidotch",
        "facebook": ""
      },
      {
        "name": "Jasveen S",
        "title": "",
        "photo": "https://africa.pycon.org/media/speakers/Jasveen_Sandral1.jpg",
        "twitter": "SJasveen",
        "facebook": "jasveen.sandral"
      },
      {
        "name": "Peacock",
        "title": "\nDesign Team Leader",
        "photo": "",
        "twitter": "peacock0803sz",
        "facebook": ""
      },
      {
        "name": "Torai KOJIMA",
        "title": "",
        "photo": "",
        "twitter": "_KozyCorner_",
        "facebook": "torai.kojima"
      },
      {
        "name": "Koji Ishimoto",
        "title": "",
        "photo": "",
        "twitter": "kojii0817",
        "facebook": ""
      },
      {
        "name": "Yuji Akisue",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Hayato Kobayashi",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Motoki Hirao",
        "title": "System Team Leader",
        "photo": "https://raw.githubusercontent.com/pyconjp/media-sponsor/master/2019/gihyo/profile/_static/HiraoMotoki.jpg",
        "twitter": "__yumechi",
        "facebook": ""
      },
      {
        "name": "Yuuki Ebihara",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Hiroya Akita",
        "title": "System Team Leader",
        "photo": "https://s.gravatar.com/avatar/9555cbb135e46733608f2adb57a06106?s=200",
        "twitter": "papi_tokei",
        "facebook": ""
      },
      {
        "name": "Yuko Isshiki",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Emi Fukuta",
        "title": "",
        "photo": "https://avatars3.githubusercontent.com/u/11752744?s=460&v=4",
        "twitter": "working_cat_zzz",
        "facebook": ""
      },
      {
        "name": "Masahiro Morino",
        "title": "",
        "photo": "https://avatars3.githubusercontent.com/u/60207264?s=400&u=5b52b08d312cf2022e8a5aef805cba0825372aac&v=4",
        "twitter": "0083Masa",
        "facebook": ""
      },
      {
        "name": "Yuichi Nakashima",
        "title": "Delivery Team Leader",
        "photo": "",
        "twitter": "",
        "facebook": "yuichi.nakashima.7"
      },
      {
        "name": "Nori Suzuki",
        "title": "Delivery Team Leader",
        "photo": "https://pbs.twimg.com/profile_images/1166720283090145280/YTwcPMN8_400x400.jpg",
        "twitter": "szkn27",
        "facebook": "szkn27"
      },
      {
        "name": "yasuyuki utsunomiya",
        "title": "",
        "photo": "",
        "twitter": "parman_osaru",
        "facebook": "utsunomiyayasuyuki"
      },
      {
        "name": "Takuya Kumagai",
        "title": "",
        "photo": "",
        "twitter": "kumappp27",
        "facebook": ""
      },
      {
        "name": "Maiko Sakamoto",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Naoki Aoyama",
        "title": "NOC Team Leader",
        "photo": "https://github.com/naa0yama.png",
        "twitter": "naa0yama",
        "facebook": "naa0yama"
      },
      {
        "name": "Kenta Yoshida",
        "title": "",
        "photo": "https://avatars3.githubusercontent.com/u/7807989?s=460&v=4",
        "twitter": "yoshiken_tut",
        "facebook": ""
      },
      {
        "name": "Kento Kawakami\n",
        "title": "",
        "photo": "",
        "twitter": "kawakami_kento",
        "facebook": ""
      },
      {
        "name": "aiko itatani",
        "title": "",
        "photo": "https://pbs.twimg.com/profile_images/1125619278105825280/GslQxSYh_400x400.jpg",
        "twitter": "mary_tuba",
        "facebook": "aiko.miyairi"
      },
      {
        "name": "Juo Kumada",
        "title": "",
        "photo": "https://ja.gravatar.com/userimage/173651889/543c0edbe30252eb31f8c2c2281b0773.png?size=500",
        "twitter": "pana_pana_kuma",
        "facebook": "panakuma8787"
      },
      {
        "name": "kazuaki miyawaki",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Momoka Takeda",
        "title": "",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Momoka_Takeda.png",
        "twitter": "wahho",
        "facebook": ""
      },
      {
        "name": "Satoshi Itatani",
        "title": "",
        "photo": "https://avatars1.githubusercontent.com/u/1680467?s=460&v=4",
        "twitter": "H_Shinonome",
        "facebook": "hiyou.shinonome"
      }
    ],
    "support-staff-list": [
      {
        "name": "Ryoko Yasutake",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": "RYOKO YASUTAKE"
      },
      {
        "name": "Yusuke Nakayama",
        "title": "",
        "photo": "",
        "twitter": "yusuken__",
        "facebook": ""
      },
      {
        "name": "Keita Matsuyama",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "Kyogo Toyoshima ",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      { "name": "", "title": "", "photo": "", "twitter": "", "facebook": "" },
      {
        "name": "Ryota Miyashita",
        "title": "",
        "photo": "",
        "twitter": "fiotto42",
        "facebook": ""
      },
      {
        "name": "Ryosuke Izumi",
        "title": "",
        "photo": "https://isryo-profile-image.s3-ap-northeast-1.amazonaws.com/p_image.jpg",
        "twitter": "is_ryo",
        "facebook": ""
      },
      {
        "name": "Kento Yamanaka",
        "title": "",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Kento_Yamanaka.JPG",
        "twitter": "kentoym_jp",
        "facebook": ""
      }
    ]
  },
  "ja": {
    "core-staff-list": [
      {
        "name": "西村ヨシロウ",
        "title": "座長",
        "photo": "",
        "twitter": "",
        "facebook": "yoshiro.nishimura.9"
      },
      {
        "name": "齋藤 大輔",
        "title": "副座長",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Daisuke_Saito.jpg",
        "twitter": "PCShop_kabu",
        "facebook": "ds110.sai"
      },
      {
        "name": "吉田 俊輔",
        "title": "アドバイザー",
        "photo": "https://www.pycon.jp/_images/yoshida.png",
        "twitter": "koedoyoshida",
        "facebook": "koedoyoshida"
      },
      {
        "name": "寺田 学",
        "title": "一般社団法人PyCon JP 代表理事",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Manabu_TERADA.png",
        "twitter": "terapyon",
        "facebook": "terapyon"
      },
      {
        "name": "高倉佑輔",
        "title": "",
        "photo": "",
        "twitter": "huideyeren",
        "facebook": "iosif.takakura.yusuke"
      },
      {
        "name": "にっきー",
        "title": "コンテンツチームリーダー",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/nikkie.jpg",
        "twitter": "ftnext",
        "facebook": ""
      },
      {
        "name": "倉本 拓実\n",
        "title": "",
        "photo": "",
        "twitter": "try",
        "facebook": ""
      },
      {
        "name": "植木浩次",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "はない",
        "title": "事務局チームリーダー",
        "photo": "",
        "twitter": "hanahiro_aze",
        "facebook": "hiroyuki.hanai.71"
      },
      {
        "name": "中林陽介",
        "title": "",
        "photo": "",
        "twitter": "elaborateplan",
        "facebook": ""
      },
      {
        "name": "稲森 景",
        "title": "",
        "photo": "",
        "twitter": "ainamori",
        "facebook": "ainamori01"
      },
      {
        "name": "えだ",
        "title": "",
        "photo": "",
        "twitter": "eda3__",
        "facebook": ""
      },
      {
        "name": "松浦麻奈未",
        "title": "",
        "photo": "https://avatars2.githubusercontent.com/u/35416089?s=400&u=320bbe5913dc12efd6dd88d03e3e199b6a4fa5a1&v=4",
        "twitter": "mtmn07384",
        "facebook": "manami.matsuura.227"
      },
      {
        "name": "natsu",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "入澤 賢",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "陶山 嶺",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "新井 正貴",
        "title": "",
        "photo": "",
        "twitter": "massa142",
        "facebook": "mstk214"
      },
      {
        "name": "オブリスト ヨナス",
        "title": "一般社団法人PyCon JP 理事",
        "photo": "",
        "twitter": "ojiidotch",
        "facebook": ""
      },
      {
        "name": "Jasveen S",
        "title": "",
        "photo": "https://africa.pycon.org/media/speakers/Jasveen_Sandral1.jpg",
        "twitter": "SJasveen",
        "facebook": "jasveen.sandral"
      },
      {
        "name": "Peacock",
        "title": "デザインチームリーダー",
        "photo": "",
        "twitter": "peacock0803sz",
        "facebook": ""
      },
      {
        "name": "小島 虎偉",
        "title": "",
        "photo": "",
        "twitter": "_KozyCorner_",
        "facebook": "torai.kojima"
      },
      {
        "name": "石本幸士",
        "title": "",
        "photo": "",
        "twitter": "kojii0817",
        "facebook": ""
      },
      {
        "name": "Yuji Akisue",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "小林 隼人",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "平尾 元紀",
        "title": "システムチームリーダー",
        "photo": "https://raw.githubusercontent.com/pyconjp/media-sponsor/master/2019/gihyo/profile/_static/HiraoMotoki.jpg",
        "twitter": "__yumechi",
        "facebook": ""
      },
      {
        "name": "海老原 由夫樹",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "秋田浩也",
        "title": "システムチームリーダー",
        "photo": "https://s.gravatar.com/avatar/9555cbb135e46733608f2adb57a06106?s=200",
        "twitter": "papi_tokei",
        "facebook": ""
      },
      {
        "name": "一色 優孝",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "福田 絵美",
        "title": "",
        "photo": "https://avatars3.githubusercontent.com/u/11752744?s=460&v=4",
        "twitter": "working_cat_zzz",
        "facebook": ""
      },
      {
        "name": "森野正博",
        "title": "",
        "photo": "https://avatars3.githubusercontent.com/u/60207264?s=400&u=5b52b08d312cf2022e8a5aef805cba0825372aac&v=4",
        "twitter": "0083Masa",
        "facebook": ""
      },
      {
        "name": "中嶋 友一",
        "title": "配信チームリーダー",
        "photo": "",
        "twitter": "",
        "facebook": "yuichi.nakashima.7"
      },
      {
        "name": "鈴木 教之",
        "title": "配信チームリーダー",
        "photo": "https://pbs.twimg.com/profile_images/1166720283090145280/YTwcPMN8_400x400.jpg",
        "twitter": "szkn27",
        "facebook": "szkn27"
      },
      {
        "name": "宇都宮靖之",
        "title": "",
        "photo": "",
        "twitter": "parman_osaru",
        "facebook": "utsunomiyayasuyuki"
      },
      {
        "name": "熊谷 拓也",
        "title": "",
        "photo": "",
        "twitter": "kumappp27",
        "facebook": ""
      },
      {
        "name": "坂本麻衣子",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "青山 尚暉",
        "title": "NOCチームリーダー",
        "photo": "https://github.com/naa0yama.png",
        "twitter": "naa0yama",
        "facebook": "naa0yama"
      },
      {
        "name": "吉田 健太",
        "title": "",
        "photo": "https://avatars3.githubusercontent.com/u/7807989?s=460&v=4",
        "twitter": "yoshiken_tut",
        "facebook": ""
      },
      {
        "name": "川上 けんと\n",
        "title": "",
        "photo": "",
        "twitter": "kawakami_kento",
        "facebook": ""
      },
      {
        "name": "板谷藍子",
        "title": "",
        "photo": "https://pbs.twimg.com/profile_images/1125619278105825280/GslQxSYh_400x400.jpg",
        "twitter": "mary_tuba",
        "facebook": "aiko.miyairi"
      },
      {
        "name": "熊田 樹央",
        "title": "",
        "photo": "https://ja.gravatar.com/userimage/173651889/543c0edbe30252eb31f8c2c2281b0773.png?size=500",
        "twitter": "pana_pana_kuma",
        "facebook": "panakuma8787"
      },
      {
        "name": "宮脇一晃",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "武田 桃花",
        "title": "",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Momoka_Takeda.png",
        "twitter": "wahho",
        "facebook": ""
      },
      {
        "name": "板谷 郷司",
        "title": "",
        "photo": "https://avatars1.githubusercontent.com/u/1680467?s=460&v=4",
        "twitter": "H_Shinonome",
        "facebook": "hiyou.shinonome"
      }
    ],
    "support-staff-list": [
      {
        "name": "安武涼子",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": "RYOKO YASUTAKE"
      },
      {
        "name": "中山 裕介",
        "title": "",
        "photo": "",
        "twitter": "yusuken__",
        "facebook": ""
      },
      {
        "name": "松山 慶太",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "豊嶋 恭梧",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "永井優斗",
        "title": "",
        "photo": "",
        "twitter": "",
        "facebook": ""
      },
      {
        "name": "宮下 亮太",
        "title": "",
        "photo": "",
        "twitter": "fiotto42",
        "facebook": ""
      },
      {
        "name": "泉 亮輔",
        "title": "",
        "photo": "https://isryo-profile-image.s3-ap-northeast-1.amazonaws.com/p_image.jpg",
        "twitter": "is_ryo",
        "facebook": ""
      },
      {
        "name": "山中 建人",
        "title": "",
        "photo": "https://github.com/pyconjp/pycon.jp.2020.ui/raw/develop/assets/img/staff/Kento_Yamanaka.JPG",
        "twitter": "kentoym_jp",
        "facebook": ""
      }
    ]
  }
}

</i18n>
