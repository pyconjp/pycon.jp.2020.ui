<template>
  <div class="main-color">
    <section
      class="relative flex items-start justify-center mb-12 h-80 md:h-120 md:items-center"
    >
      <div class="relative z-10 mt-16 mr-2 md:m-0">
        <h1 class="text-4xl font-extrabold leading-tight md:text-6xl">
          PyCon JP <br />2020 <span class="font-semibold">Online</span>
        </h1>
        <div class="mt-6 space-y-2">
          <h2 class="flex items-center text-2xl md:text-3xl">
            <i class="mr-2 material-icons">location_on</i>
            Online Conference
          </h2>
          <h2
            class="flex flex-wrap items-center justify-start text-2xl md:text-3xl"
          >
            <i class="mr-2 text-gray-700 material-icons">event</i>
            <span class="mr-1 font-semibold">2020 08/28 </span>(Fri.) /
            <span class="mx-1 font-semibold">29 </span>(Sat.)
          </h2>
          <div class="flex items-center">
            <img :src="require('~/assets/img/twitter.png')" class="h-6 mr-2" />
            <a
              class="text-2xl text-blue-400"
              href="https://twitter.com/search?q=%23pyconjp&src=typed_query"
              target="_blank"
              rel="noopener noreferrer"
              >#pyconjp</a
            >
          </div>
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

    <!-- <python-banner
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
          href="https://pyconjp.blogspot.com/2020/05/2020-sponsorship-application.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          <button
            class="flex items-center px-4 py-2 font-medium transition-colors duration-200 bg-white rounded-full shadow group md:px-6 md:py-6 text-py-black hover:bg-py-blue-dark focus:outline-none"
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
    </python-banner> -->

    <python-banner direction="right" back-ground-color="#EE9D2C" size="big">
      <template #title>
        {{ $t('ticket.title') }}
      </template>
      <template #content>
        {{ $t('ticket.content') }}
      </template>
      <template #button>
        <a
          class="mt-6"
          href="https://pyconjp.blogspot.com/2020/07/pycon-jp-2020-conference-ticket-on-sale.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          <button
            class="relative flex items-center px-4 py-2 mt-6 font-medium transition-colors duration-200 bg-white rounded-full shadow group md:px-6 md:py-6 hover:bg-py-orange-dark text-py-black focus:outline-none"
          >
            <p
              class="w-6 h-6 rounded-full bg-py-orange-dark group-hover:bg-white"
            />
            <span
              class="ml-2 md:text-xl md:ml-6 md:mr-4 group-hover:text-white"
            >
              {{ $t('ticket.button') }}
            </span>
          </button></a
        >
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
          class="relative z-10 flex flex-col justify-center px-6 py-12 space-y-6 bg-white sm:px-10 md:px-16 rounded-py"
        >
          <article
            v-for="(item, i) in news"
            :key="i"
            class="flex flex-col justify-between md:flex-row"
          >
            <time
              :datetime="formatISO(item.pubDate[0])"
              class="mb-2 text-lg font-medium text-left text-gray-700 md:text-xl md:mb-0"
            >
              {{ format(item.pubDate[0]) }}
            </time>
            <a
              class="w-full font-light md:ml-12 hover:underline"
              :href="item.link"
              target="_blank"
              rel="noopener noreferrer"
            >
              {{ item.title[0] }}
            </a>
          </article>
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
            <div class="flex flex-col flex-1 px-6 py-12 sm:px-10 md:px-16">
              <h2 class="inline mb-2 text-2xl font-semibold md:text-4xl">
                What is PyConJP?
              </h2>
              <h3 class="mb-8 text-xl font-medium md:text-2xl">
                {{ $t('overview.contentTitle') }}
              </h3>
              <p>
                {{ $t('overview.content') }}
              </p>
              <nuxt-link
                :to="localePath('/code-of-conduct')"
                class="self-center"
              >
                <button
                  class="flex items-center self-center justify-center px-2 py-2 mt-6 font-medium duration-200 bg-white rounded-full shadow group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none transition-color"
                >
                  <p
                    class="w-6 h-6 rounded-full bg-py-black group-hover:bg-white"
                  />
                  <span class="mx-4 md:text-xl group-hover:text-white">
                    {{ $t('overview.button') }}
                  </span>
                </button>
              </nuxt-link>
            </div>
            <img
              :src="require('~/assets/img/overview.jpg')"
              class="box-border object-cover object-right w-full h-64 md:h-auto lg:w-2/5"
            />
          </div>
        </div>
      </div>
    </section>

    <section class="flex flex-col items-center justify-center mt-12">
      <div class="flex flex-col items-center">
        <h2 class="inline mb-2 text-4xl font-semibold md:text-6xl">
          Conference
        </h2>
        <p class="mb-8 text-xl md:text-2xl">{{ $t('conference.subtitle') }}</p>
      </div>
      <python-banner direction="right" back-ground-color="#3D40CB" size="small">
        <template #title>
          Keynote
        </template>
      </python-banner>

      <div class="flex flex-wrap justify-around mt-12 mb-12">
        <talk-content
          v-for="(keynote, index) in $t('keynote')"
          :key="keynote.name"
          class="w-full md:w-2/3 xl:w-2/5 xl:mt-0"
          :class="[index == 0 ? 'mt-8' : 'mt-20']"
          talk-type="talk"
        >
          <template #image
            ><img
              :src="require(`~/assets/img/people/${keynote.image}`)"
              class="object-cover object-top w-24 h-24 rounded-full md:w-40 md:h-40"
          /></template>
          <template #name>{{ keynote.name }}</template>
          <template #date> {{ keynote.date }} </template>
          <template #description>
            <p
              v-for="(description, index2) in keynote.description"
              :key="`p-${index2}`"
            >
              {{ description }}
            </p>
          </template>
        </talk-content>
      </div>

      <python-banner direction="right" back-ground-color="#EE9D2C" size="small">
        <template #title>
          Invited talk
        </template>
      </python-banner>

      <div class="flex flex-wrap justify-around mt-12 mb-12">
        <talk-content
          v-for="invitedTalk in $t('invited-talk')"
          :key="invitedTalk.name"
          class="w-full mt-16 md:w-2/3 xl:w-2/5"
          talk-type="talk"
          main-color="#EE9D2C"
        >
          <template #image
            ><img
              :src="require(`~/assets/img/people/${invitedTalk.image}`)"
              class="object-cover object-top w-24 h-24 rounded-full md:w-40 md:h-40"
          /></template>
          <template #name>{{ invitedTalk.name }}</template>
          <template #date> {{ invitedTalk.date }} </template>
          <template #description>
            <p
              v-for="(description, index2) in invitedTalk.description"
              :key="`p-${index2}`"
            >
              {{ description }}
            </p>
          </template>
        </talk-content>
      </div>

      <!-- <python-banner direction="right" back-ground-color="#3F496A" size="small">
        <template #title>
          Sessions
        </template>
      </python-banner> -->
    </section>

    <section class="flex flex-col items-center justify-center mb-8 space-y-12">
      <div class="flex flex-col items-center">
        <h2 class="inline mb-2 text-4xl font-semibold md:text-6xl">
          Sponsor
        </h2>
        <p class="mb-8 text-xl md:text-2xl">-{{ $t('sponsor.subTitle') }}-</p>
      </div>

      <python-banner
        direction="right"
        back-ground-color="#71A4F1"
        size="small"
        length="long"
      >
        <template #title>
          Platinum
        </template>
      </python-banner>

      <div class="flex flex-wrap items-center justify-center">
        <a
          v-for="platinum in $t('sponsor.platinum')"
          :key="platinum.companyName"
          :href="platinum.url"
          target="_blank"
          rel="noopener noreferrer"
          class="w-full m-8 md:w-2/5"
        >
          <img :src="require(`~/assets/img/sponsor/${platinum.imagePath}`)"
        /></a>
      </div>

      <python-banner
        direction="right"
        back-ground-color="#E3AB4A"
        sie="small"
        length="mid"
      >
        <template #title>
          Gold
        </template>
      </python-banner>

      <div class="flex flex-wrap items-center justify-center">
        <a
          v-for="gold in $t('sponsor.gold')"
          :key="gold.companyName"
          :href="gold.url"
          target="_blank"
          rel="noopener noreferrer"
          class="w-full m-8 md:w-1/3"
        >
          <img :src="require(`~/assets/img/sponsor/${gold.imagePath}`)" />
        </a>
      </div>

      <python-banner
        direction="right"
        back-ground-color="#818181"
        size="small"
        length="small"
      >
        <template #title>
          Silver
        </template>
      </python-banner>

      <div class="grid grid-cols-1 gap-4 pb-8 md:grid-cols-2">
        <a
          v-for="silver in $t('sponsor.silver')"
          :key="silver.companyName"
          :href="silver.url"
          target="_blank"
          rel="noopener noreferrer"
        >
          <p class="text-2xl break-all">
            {{ silver.companyName }}
          </p></a
        >
      </div>
      <python-banner
        direction="right"
        back-ground-color="#3D40CB"
        size="small"
        length="small"
        class="mt-16"
      >
        <template #title>
          SPECIAL
        </template>
      </python-banner>
      <h3 class="mt-6 text-4xl font-medium text-py-black">
        {{ $t('sponsor.message.specialSponsor') }}
      </h3>
      <div class="flex flex-wrap items-center justify-center">
        <a
          v-for="cooperation in $t('sponsor.special.cooperation')"
          :key="cooperation.companyName"
          :href="cooperation.url"
          target="_blank"
          rel="noopener noreferrer"
          class="w-full m-8 md:w-1/3"
        >
          <img
            :src="require(`~/assets/img/sponsor/${cooperation.imagePath}`)"
            class="w-full"
          />
        </a>
      </div>
      <h3 class="mt-16 text-4xl font-medium text-py-black">
        {{ $t('sponsor.message.tutorial') }}
      </h3>
      <div class="flex flex-wrap items-center justify-center">
        <a
          v-for="tutorial in $t('sponsor.special.tutorial')"
          :key="tutorial.companyName"
          :href="tutorial.url"
          target="_blank"
          rel="noopener noreferrer"
          class="w-full m-8 md:w-1/3"
        >
          <img
            :src="require(`~/assets/img/sponsor/${tutorial.imagePath}`)"
            class="w-full"
          />
        </a>
      </div>
      <h3 class="mt-6 text-4xl font-medium text-py-black">
        {{ $t('sponsor.message.media') }}
      </h3>
      <div class="flex flex-wrap items-center justify-center">
        <a
          v-for="media in $t('sponsor.special.media')"
          :key="media.companyName"
          :href="media.url"
          target="_blank"
          rel="noopener noreferrer"
          class="w-full m-8 md:w-1/3"
        >
          <img
            :src="require(`~/assets/img/sponsor/${media.imagePath}`)"
            class="w-full"
          />
        </a>
      </div>

      <python-banner
        direction="right"
        back-ground-color="#3F496A"
        size="small"
        length="small"
        class="mt-16"
      >
        <template #title>
          PATRON
        </template>
      </python-banner>
      <div class="flex flex-wrap mt-4 mb-8">
        <Patron
          v-for="patron in $t('sponsor.patron')"
          :key="patron.name"
          class="ml-4"
          :connpass-link="patron.connpassLink"
          :name="patron.name"
          :icon-image-link="patron.iconImageLink"
        ></Patron>
      </div>
    </section>
  </div>
</template>

<script>
import Vue from 'vue'
import { format, formatISO } from 'date-fns'
import PythonBanner from '~/components/Elements/PythonBanner'
import TalkContent from '~/components/Elements/TalkContent'
import Patron from '~/components/Elements/Patron'

export default Vue.extend({
  components: {
    PythonBanner,
    TalkContent,
    Patron,
  },
  async asyncData({ app }) {
    const jsonPath =
      process.env.targetBranch === 'master'
        ? '/2020/_nuxt/news.json'
        : '/_nuxt/news.json'
    const news = await app.$axios.$get(jsonPath)
    return { news }
  },
  data() {
    return {}
  },
  methods: {
    format(date) {
      return format(new Date(date), 'yyyy.MM.dd')
    },
    formatISO(date) {
      return formatISO(new Date(date))
    },
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
      "button": "Apply for Sponsor",
      "subTitle": "sponsor"
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
    },
    "conference": {
      "subtitle": "-conference list-"
    },
    "keynote": [
      {
        "name": "Seiji Shiba",
        "image": "Shiba_Image.jpg",
        "date": "08/28",
        "description": {
          "p-1": "In 2017, he began self-taught machine learning, and in the same year, he became the runner-up in the Shogi (Japanese Chess) Den-O tournament he participated in for the first time.",
          "p-2": "The following year, he won the World Computer Shogi Championship even though it was the first time he participated.",
          "p-3": "Since then, he has been a runner-up in the 2019 and 2020 meets and has a phenomenal one-point average ranking in the participating meets.",
          "p-4": "He is a researcher who mainly works on numerical simulations, but most of his recent publications have been about shogi.",
          "p-5": "His hobbies are beer and watching shogi."
        }
      },
      {
        "name": "Rich Jones",
        "image": "Rich_Image.png",
        "date": "08/29",
        "description": {
          "p-1": "Rich is the cofounder of Gun.io, a global consulting firm staffed by the best hackers from the Free and Open Source software community.",
          "p-2": "He is the author of Zappa, the leading server-less Python framework, used by thousands of companies and users to save time and money for their web deployments. He has worked on everything from cloud GPU clusters for medical and scientific computing to mobile peer to peer file sharing applications, and on everything in between.",
          "p-3": "In his spare time, he enjoys skateboarding, dirty southern trap music, and Laphroaig."
        }
      }
    ],
    "invited-talk": [
      {
        "name": "Tomoko Uchida",
        "image": "Uchida_Image.jpg",
        "date": "08/28",
        "description": {
          "p-1": "Tomoko completed the master's program at the University of Tsukuba Graduate School of Systems and Information Engineering in 2007. ",
          "p-2": "After working for several IT companies, she is currently engaged in research and development of search systems and language processing at the R&D team of LegalForce Inc. In 2015, she released Janome, a Japanese Python morphological analysis library as OSS, and had a presentation on PyCon JP. She is also a committer of Apache Lucene, an OSS search engine library, from 2019. She is interested in information retrieval, machine learning, and natural language processing. She is dreaming of living with her cats in a room with a view of the ocean."
        }
      },
      {
        "name": "Makoto Tsuyuki",
        "image": "Tsuyuki_Image.jpg",
        "date": "08/29",
        "description": {
          "p-1": "Makoto moved from the fashion jewelry industry to the IT industry around 2000 and has been working as a software engineer ever since.",
          "p-2": "He has worked on a variety of development projects both for BtoB and BtoC using Python, Java, Perl, Ruby, etc.",
          "p-3": "He has worked not only in development as a software engineer, a chief architect or a technical lead, but also worked outside of development, such as a programming courses teacher and a member of starting up in-house factory.",
          "p-4": "In the past few years, he has been involved in creating a comfortable environment for engineers."
        }
      },
      {
        "name": "Yuki Iwazaki",
        "image": "Iwazaki_Image.jpg",
        "date": "08/28",
        "description": {
          "p-1": "Yuki is a Research Engineer at AI Lab on CyberAgent, Inc.",
          "p-2": "After joining the company in 2014 as a server-side engineer, he developed an ad delivery platform, ad rendering engine and effect prediction system using Scala, JavaScript and Python in the Internet Advertising Business.",
          "p-3": "He has been in his current position since 2017 after working in frontend, infrastructure and data analysis.",
          "p-4": "He works in the Creative Research Group and analyzes the impact of streaming from high-dimensional features such as text, images and videos in ads.",
          "p-5": "In RPG games, he likes paper armor attackers like wizards."
        }
      },
      {
        "name": "Lina Katayose",
        "image": "Katayose_Image.jpg",
        "date": "08/29",
        "description": {
          "p-1": "Lina Katayose has been interested in aircraft since childhood, and her desire to learn more led her to pursue a master's degree in aerospace at Tokai University's Graduate School of Engineering, where she studied helicopters and other VTOL(vertical takeoff and landing) aircraft.",
          "p-2": "After finishing the graduate school, she worked on her personal research while working on web-related projects and came across Python. ",
          "p-3": "She has programmed using Python mainly focusing on controlling \"things\" around using Raspberry Pi.",
          "p-4": "She attended PyCon JP for the first time in 2016, and after discovering the fun and depth of Python, she joined various communities and made many friends. She joined the PyLadies Tokyo community and now she is an organizer of PyLadies Tokyo.",
          "p-5": "She presented and demonstrated drones and controlling them by Python at PyCon JP 2017 and 2018. ",
          "p-6": "She is known as an international speaker at PyCon Thailand 2019 and talked about PyLadies' community activities, also has attended in PyCon US and other international PyCon events. ",
          "p-7": "In 2018, she founded moegi, Inc. and develops smartphone applications. She is also researching the uses and problems of the skies not only in Japan but also in the world, and working as a developer in the field of aviation."
        }
      }
    ]
  },
  "ja": {
    "sponsor": {
      "title": "企業スポンサー募集中",
      "content": "PyCon JP 2020を応援して下さるスポンサーを募集しております",
      "button": "スポンサーに申し込む",
      "subTitle": "スポンサー"
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
    },
    "conference":{
      "subtitle": "-会議一覧-"
    },
    "keynote": [
      {
        "name": "芝世弐",
        "image": "Shiba_Image.jpg",
        "date": "8月28日",
        "description": {
          "p-1": "2017年に独学で機械学習を始め，同年に初参加の将棋電王トーナメントにて準優勝。翌年には世界コンピュータ将棋選手権に初参加で優勝してしまう。",
          "p-2": "以後，2019年および2020年の大会では準優勝と参加大会の平均順位が1点台という驚異的な強さを誇る。",
          "p-3": "本職は数値シミュレーションを主とする研究者であるが最近の発表は大半将棋に関するものになっている。",
          "p-4": "趣味はビールと将棋観戦。"
        }
      },
      {
        "name": "Rich Jones",
        "image": "Rich_Image.png",
        "date": "8月29日",
        "description": {
          "p-1": "RichはGun.ioの共同設立者です。",
          "p-2": "Gun.ioはグローバルなコンサルティングファームで、フリーソフトウェアやオープンソースソフトウェアのコミュニティから来た最も優秀なエンジニア（ハッカー）たちが所属しています。",
          "p-3": "彼は、Pythonにおける主要なサーバレスフレームワーク、Zappaの作者です。",
          "p-4": "Zappaは、何千もの企業やユーザによって使われ、Web開発における時間と費用を節約しています。彼は医療や科学計算向けのクラウドGPUクラスタからモバイルのピア・ツー・ピアのファイル共有アプリまで、そしてその間にあるあらゆるものに取り組んできました。彼の趣味はスケートボード、サザン・ヒップホップと、ラフロイグを飲むことです。"
        }
      }
    ],
    "invited-talk": [
      {
        "name": "打田智子",
        "image": "Uchida_Image.jpg",
        "date": "08/28",
        "description": {
          "p-1": "2007年に筑波大学大学院システム情報工学研究科の博士前期課程を修了後，いくつかのIT系企業を経て，現在は株式会社 LegalForce の R&D チームで検索システムや言語処理の研究開発に従事。2015年に Python 製日本語形態素解析ライブラリ Janome を OSS として公開し，同年 PyConJP にも登壇。Janome の開発をほそぼそ続けながら，2019年から OSS 検索エンジンライブラリ Apache Lucene のコミッターも務める。興味のある分野は情報検索と機械学習，自然言語処理。海の見える部屋で猫と暮らすのが夢。"
        }
      },
      {
        "name": "露木誠",
        "image": "Tsuyuki_Image.jpg",
        "date": "08/29",
        "description": {
          "p-1": "2000年頃にファッションジュエリー業界からIT業界へ移り、以来ソフトウェアエンジニアとして働いています。",
          "p-2": "Python、Java、Perl、Rubyなどのプログラミング言語を用いてB向けC向けを問わずさまざまな開発に従事してきました。",
          "p-3": "ソフトウェアエンジニア・チーフアーキテクト・テックリードなどとして開発に携わるのみならず、プログラミング講習の講師や自社サービス用工場の立ち上げなど、開発から外れた仕事もしてきました。",
          "p-4": "ここ数年はエンジニアが働きやすい環境づくりなどにも関わっています。"
        }
      },
      {
        "name": "岩崎祐貴",
        "image": "Iwazaki_Image.jpg",
        "date": "08/28",
        "description": {
          "p-1": "株式会社サイバーエージェント AI Lab Research Engineer。",
          "p-2": "2014年にサーバーサイドエンジニアとして入社後、インターネット広告事業でScala、JavaScript、Pythonを使った配信基盤や広告レンダリングエンジン、効果予測システムを作成。",
          "p-3": "フロント・インフラ・データ分析業務を経て、2017年から現職。",
          "p-4": "クリエイティブリサーチグループにて広告のテキストや画像、動画等の高次元特徴から配信影響を紐解く研究に従事。",
          "p-5": "ゲームでは魔法使いのような紙耐久アタッカーが好き。"
        }
      },
      {
        "name": "片寄里菜",
        "image": "Katayose_Image.jpg",
        "date": "08/29",
        "description": {
          "p-1": "片寄里菜さんは、幼い時より航空機に興味があり、もっと学びたいという想いから東海大学工学研究科・航空宇宙学専攻の博士課程前期に進み、ヘリコプターなど垂直離着陸機の研究を行っていました。",
          "p-2": "大学院修了後は、WEB関連の仕事をしながら個人的な研究テーマを進め、Pythonと出会いました。Pythonでは主にRaspberryPiを使ったモノを動かすプログラミングに視点を置き、開発などを行っていました。 ",
          "p-3": "PyConJPには2016年に初参加。Pythonの楽しさや奥深さを知り、様々なコミュニティに参加し友人・知人を増やしたようです。またPyLadiesTokyoコミュニティ参加をきっかけに、今ではスタッフとして活動しています。",
          "p-4": "登壇経験としてPyConJP2017と2018ではドローンとPythonに関する内容で発表・実演を行いました。またPyCon Thailand2019ではPyLadiesのコミュニティ活動に関する海外の登壇経験もあります。PyConUSなど海外のPyConに参加している経験もあり、精力的に活動を行っています。",
          "p-5": "ご自身の仕事は2018年に株式会社moegiを創業し、計測用のスマホアプリなどを開発。日本だけでなく世界の空の活用法や問題点なども調べ、航空機分野の開発者として活躍できるようにと日々活動をしています。"
        }
      }
    ]
  }
}
</i18n>
