<template>
  <section class="">
    <div class="relative">
      <div class="flex flex-col items-center title-block">
        <h2 class="mb-2 text-4xl font-semibold text-center md:text-6xl">
          Youth Coder Workshop
        </h2>
        <p class="mb-8 text-xl md:text-2xl">-ユースコーダーワークショップ-</p>
      </div>
      <div class="flex flex-col">
        <div class="flex flex-wrap items-center justify-center md:flex-no-wrap">
          <div class="w-full md:w-1/2 xl:w-1/3">
            <p class="mb-0 text-5xl font-bold text-center md:mr-8">
              2020.08.30<span class="ml-2 text-lg text-blue-600">(Sun.)</span>
            </p>
          </div>
          <div class="flex justify-center w-full mt-8 md:w-1/3 lg:w-1/2">
            <img
              :src="require('~/assets/img/youth-coder/youth-coder.png')"
              class="z-10 w-full h-full rounded-xl"
            />
          </div>
        </div>
      </div>
      <div
        class="absolute w-screen opacity-25 md:opacity-100 main-visual md:w-50vw md:relative"
      >
        <div
          class="absolute hidden rounded-full balloon-1 bg-py-blue-light md:block"
        ></div>
        <div
          class="absolute hidden rounded-full balloon-2 bg-py-orange-light md:block"
        ></div>
      </div>
    </div>
    <div class="pt-24 pb-24 mt-12 md:mt-24 way-to-join-block m-screen">
      <div
        class="relative flex items-start justify-center md:items-center way-to-join-block"
      >
        <div class="relative flex flex-col items-center justify-center">
          <div class="relative z-10 flex justify-center w-screen m-screen">
            <div
              class="flex flex-wrap items-center justify-center w-11/12 px-6 border-8 border-solid sm:px-8 md:px-10 lg:px-12 lg:flex-row md:w-4/5 border-py-black rounded-xl way-to-join-content"
            >
              <div class="my-6 md:w-3/5">
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
              <div class="inline-block w-full mx-0 md:w-2/5">
                <a
                  class="text-xl text-blue-400 no-underline lg:text-2xl"
                  href="https://pyconjp.connpass.com/event/182553/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <button
                    class="flex items-center w-full h-20 px-4 py-2 font-medium duration-200 bg-white rounded-full shadow xl:w-9/12 xl:ml-10 transition-color group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none"
                  >
                    <div class="w-1/5">
                      <div
                        class="w-6 h-6 rounded-full bg-py-black group-hover:bg-white"
                      ></div>
                    </div>
                    <div class="w-4/5">
                      <p class="mx-0 md:text-xl md:mr-4 group-hover:text-white">
                        {{ $t('workshop.connpass') }}
                      </p>
                    </div>
                  </button></a
                >
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
    <div class="mt-24 text-base description-block">
      <div id="event-one" class="mb-20 event-one">
        <python-banner
          direction="right"
          back-ground-color="#3D40CB"
          size="small"
        >
          <template #title>
            ProcessingでPythonのモブプログラミング！
          </template>
        </python-banner>

        <div class="mt-12">
          <div>
            <p>
              今年はProccessing.pyといわれる、電子アートとビジュアルデザインのための環境を使って、Pythonを学びます。
              グラフィックを書くための機能がたくさん用意されているので、簡単にビジュアルプログラミングを楽しめます。
              また、モブプログラミングは複数人数でプログラミングを行う手法で、メンバー1人がプログラミングをし、残りのメンバーはプログラミングのサポートやアドバイスを出す役割をします。また、役割を時間ごとに区切って交換し、この流れを複数回行います。
              今回のワークショップでは1グループ、3人から4人で作品作りに挑戦します。
            </p>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              参加枠について:
            </div>
            <p class="mt-2">
              募集人数は24名です。募集締め切りは8月28日18時までになります。
              申込みは先着順となります。定員に達した場合はキャンセル待ちとなります。
              参加可能の可否について募集締め切り後、当ページにてご確認ください。
            </p>
            <p class="mt-2">
              *本ワークショップは、PyCon JP
              2020のイベントとして8月30日に開催されます。本年度はCOVID-19の影響によりオンライン開催となりました。本チケットは、Youth
              Coder WorkshopへのZoomでの参加チケットです。
            </p>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              参加対象:
            </div>
            <p class="mt-2 mb-8">
              本ワークショップの対象は小学4年生から中学生くらいまでを想定しています。
              また、アルファベットの大文字小文字の違いがわかることが望ましいです。
            </p>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              教材について:
            </div>
            <p class="mt-2 mb-4">
              本ワークショップでは以下の教材を使用します
            </p>
            <ol class="pl-6 list-decimal">
              <li>
                Proccessing.py <br />
                <a
                  href="https://py.processing.org/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-blue-600 underline cursor-pointer"
                  >Proccessing.pyの概要</a
                >
              </li>
              <li class="mt-4">
                EduBlocks <br />
                当日はEduBlocksといわれる、ブラウザ上でプログラミングできるツールを使います。<br />
                <a
                  href="https://edublocks.org/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-blue-600 underline cursor-pointer"
                  >EduBlocksの概要</a
                >
              </li>
            </ol>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              参加方法について:
            </div>
            <p class="mt-2 mb-4">
              本ワークショップはオンラインでの開催となります。参加に伴い、以下のご準備をお願いします。
            </p>
            <ul class="list-disc">
              <li>
                パソコン
                <ul class="list-disc">
                  <li>本イベント参加のため</li>
                </ul>
              </li>
              <li class="mt-2">
                ブラウザ（InternetExplorerを除く）
                <ul>
                  <li>動作確認などを行うため</li>
                </ul>
              </li>
              <li class="mt-2">
                Zoomのアカウント
                <ul>
                  <li>
                    本イベントの参加のコミュニケーションツールとして使用するため
                  </li>
                </ul>
              </li>
              <li class="mt-2">
                Googleアカウント
                <ul>
                  <li>
                    EduBlocksというツールを使い、モブプログラミングをするため
                  </li>
                </ul>
              </li>
            </ul>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              ワークショップの時間について:
            </div>
            <p class="mt-2">
              ワークショップは以下の時間（予定）にて実施されます。
            </p>
            <p>全体学習 10:30 - 12:00</p>
            <p>お昼休憩 12:00 - 13:30</p>
            <p>グループ学習 13:30 - 15:00</p>
            <p>成果発表会 15:00 - 15:30</p>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              行動規範
            </div>
            <p class="mt-2">
              保護者様には本ワークショップの参加に際してPyCon JP
              2020の行動規範を一読いただき、遵守いただきますようお願い申し上げます。
            </p>
            <nuxt-link
              :to="localePath('/code-of-conduct')"
              class="block mt-2 text-blue-600 underline cursor-pointer"
            >
              PyCon JP 2020 行動規範</nuxt-link
            >
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              ワークショップ協力（あいうえお順。敬称略）
            </div>
            <p
              v-for="(member, index) in memberList"
              :key="`member-${index}`"
              class="my-0"
            >
              {{ member }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Vue from 'vue'
import PythonBanner from '~/components/Elements/PythonBanner'

export default Vue.extend({
  components: {
    PythonBanner,
  },
  data() {
    return {
      memberList: [
        '今津 善文（所属 CoderDojo 厚木',
        '瀬戸 亮一（所属 CoderDojo 浦安',
        '田中 真輔（所属 CoderDojo 大船）',
        '土井 敬司（所属 CoderDojo 大船）',
        '千葉 幸恵（所属 CoderDojo 鎌ヶ谷）',
        '野田 浩晶（所属 CoderDojo 鎌ヶ谷）',
        'とがぞの （所属 CoderDojo 小平）',
        '増澤 智将（所属 CoderDojo 船橋）',
        '矢嶋 貴宜（所属 CoderDojo 船橋）',
      ],
    }
  },
  methods: {},
  head() {
    return { title: 'PyCon JP 2020', titleTemplate: null }
  },
})
</script>

<style scoped>
section {
  color: #404a6b;
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
  left: 240px;
  top: -520px;
  width: 110px;
  z-index: -1;
}
.balloon-2 {
  bottom: 80px;
  height: 110px;
  left: 60px;
  width: 110px;
  z-index: -1;
}
.way-to-join-block {
  background-color: #ffd8a1;
}
.way-to-join-content {
  background-color: #ffffff;
}
ul {
  list-style-type: disc;
  padding-left: 1rem;
}

ul ul {
  padding-left: 1rem;
}
</style>

<i18n>
{
"en": {
    "title": "How to attend",
    "paragraphs": {
      "p-1": "Apply via connpass"
    },
    "workshop": {
      "connpass": "Join Workshop"
    }
  },
  "ja": {
    "title": "参加方法",
    "paragraphs": {
      "p-1": "connpass経由で申し込みをお願いします"
    },
    "workshop": {
      "connpass": "ワークショップ参加"
    }
  }
}
</i18n>
