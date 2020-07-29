<template>
  <section class="w-full py-8">
    <div class="hero-block">
      <div class="flex flex-col items-center title-block">
        <h2 class="inline mb-2 text-4xl font-semibold md:text-6xl">
          Tutorial
        </h2>
        <p class="mb-8 text-xl md:text-2xl">-チュートリアル-</p>
      </div>
      <div class="flex flex-wrap mt-12 mb-12">
        <div class="flex flex-wrap items-center justify-center">
          <div class="mr-8 date-block">
            <div class="mb-0 text-5xl font-bold date-text">
              2020.08.30<span class="ml-2 text-lg">(Sun)</span>
            </div>
            <div class="mx-1 mb-2 text-lg font-semibold md:text-3xl">
              10:00 - 17:00
            </div>
          </div>
          <div class="mt-8">
            <img
              :src="require('~/assets/img/tutorial/tutorial.png')"
              class="z-10"
            />
          </div>
        </div>
        <div class="description-block lg:ml-10">
          <div>
            <p class="mt-12 mb-4 text-base">
              {{ $t('description.p-1') }}<br />
              {{ $t('description.p-2') }}
            </p>
            <p class="mb-4 text-base">
              {{ $t('description.p-3') }}<br />
              <span class="font-bold">{{ $t('description.p-4') }}</span>
            </p>
          </div>
          <div class="description-link-block">
            <div class="mb-4 text-lg font-bold">
              <nuxt-link to="#event-one">
                {{ $t('description.event-one-title') }}
              </nuxt-link>
            </div>
            <div class="text-lg font-bold">
              <nuxt-link to="#event-two">
                {{ $t('description.event-two-title') }}
              </nuxt-link>
            </div>
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
      </div>
    </div>
    <div class="w-screen pt-24 pb-24 mt-24 way-to-join-block m-screen">
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
              <div
                class="inline-block w-8/12 mx-0 mb-6 lg:my-3 lg:ml-4 btn-tuto"
              >
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
            {{ $t('description.event-one-title') }}
          </template>
        </python-banner>
        <div class="mt-12 event-description">
          このチュートリアルではSlack
          Botの開発を通じて、Pythonによるアプリケーション開発の基礎知識やテスト駆動開発のためのpytestの基本的な使い方、Sphinxを使ったdocstringからのドキュメント作成の基礎を学ぶことができます。各国の挨拶を返したり、Livedoor天気APIで現在の天気を取得したり、connpassのAPIでイベント情報を検索できるSlack
          Botを作ることができるようになるでしょう。
        </div>
        <div class="mt-8 event-detials">
          <div class="date-block">
            <div class="mb-2 text-xl font-bold title">
              日程
            </div>
            <div class="content">
              2020.08.30(日)10:00-17:00
            </div>
          </div>
          <div class="mt-4 powered-block">
            <div class="mb-2 text-xl font-bold title">提供</div>
            <div class="content">
              <ul>
                <li>・Python駿河</li>
                <li>・Unagi.py</li>
              </ul>
            </div>
          </div>
          <div class="mt-4 background-block">
            <div class="mb-2 text-xl font-bold title">必要な知識</div>
            <div class="content">
              <ul>
                <li>・Pythonの基礎的文法</li>
                <li>・Slackの操作</li>
                <li>・Web API（REST API）の扱い方</li>
                <li class="text-indent-one">・JSONフォーマットの扱い方</li>
              </ul>
            </div>
          </div>
          <div class="environment-block">
            <div class="mt-4 mb-2 text-xl font-bold title">利用する環境</div>
            <div class="content">
              <ul>
                <li class="mb-4">後日環境設定手順書を公開します。</li>
                <li>・事前にPython 3.7以上をセットアップしてください。</li>
                <li class="text-indent-one">
                  ・Windowsの場合は<a
                    href="https://www.python.org/"
                    target="_blank"
                    rel="noopener noreferrer"
                    >Python.org</a
                  >からダウンロードしてください。
                </li>
                <li class="text-indent-one">
                  ・Macは<a
                    href="https://www.python.org/"
                    target="_blank"
                    rel="noopener noreferrer"
                    >Python.org</a
                  >からダウンロード or homebrewでインストールしてください。
                </li>
                <li class="text-indent-one">
                  ・pip/venv or pipenv で開発環境を用意してください。
                </li>
                <li class="mt-4">・OSはWin10, macOS 10.14に対応します。</li>
                <li>・以下のPythonライブラリを使用する予定です。</li>
                <li class="text-indent-one">・Slack Bot向け</li>
                <li class="text-indent-two">・slackclient</li>
                <li class="text-indent-two">・slackeventapi</li>
                <li class="text-indent-two">・flask</li>
                <li class="text-indent-two">・requests</li>
                <li class="text-indent-one">・pytest</li>
                <li class="text-indent-one">・sphinx</li>
              </ul>
              <p class="mt-4">
                エディタはVisual Studio Codeを使用します。
                また、以下の拡張機能を使用します。
              </p>
              <div>
                <div>
                  ・
                  <a
                    href="https://marketplace.visualstudio.com/items?itemName=ms-python.python"
                    target="_blank"
                    rel="noopener noreferrer"
                    >Python - Visual Studio Marketplace</a
                  >
                </div>
                <div>
                  ・
                  <a
                    href="https://docs.microsoft.com/ja-jp/visualstudio/liveshare/"
                    target="_blank"
                    rel="noopener noreferrer"
                    >概要 - Visual Studio Live Share - Visual Studio Live Share
                    | Microsoft Docs</a
                  >
                </div>
                <div class="mt-4">
                  <div class="mb-4">
                    そのほかに、以下の外部サービスへの登録が必要です。
                  </div>
                  <ul>
                    <li>
                      <a
                        href="https://slack.com/intl/ja-jp/"
                        target="_blank"
                        rel="noopener noreferrer"
                        >Slack</a
                      >
                      : Slack
                      Botを動かすために必要です。チュートリアル参加者は新規にワークスペースの作成を推奨します。
                    </li>
                    <li>
                      <a
                        href="https://ngrok.com/"
                        target="_blank"
                        rel="noopener noreferrer"
                        >ngrok</a
                      >
                      : ローカル環境で動作するSlack
                      Botと、Slackワークスペースとの双方向通信で利用します。ローカル環境のサーバーを一時的に外部へ公開できるサービスです。
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="event-two" class="mb-20 event-two">
        <python-banner
          direction="right"
          back-ground-color="#EE9D2C"
          size="small"
        >
          <template #title>
            {{ $t('description.event-two-title') }}
          </template>
        </python-banner>
        <div class="mt-12 event-description">
          このチュートリアルでは、世の中の動向を可視化、予測するために必要なデータ分析の知識を習得できます。貿易収支や家計調査、境界データと国勢調査などのオープンデータをもとに、分析できるように前処理を行い、作ったデータをPlotlyとPydeckを使って可視化し、DashやStreamlitを使ってダッシュボードを作り、scikit-learnを使って機械学習を行うといった、一連のデータ分析をGoogle
          Colaboratoryを使用して体験できます。
        </div>
        <div class="mt-8 event-detials">
          <div class="date-block">
            <div class="mb-2 text-xl font-bold title">日程</div>
            <div class="content">2020.08.30(日)10:00-17:00</div>
          </div>
          <div class="powerd-block">
            <div class="mt-4 mb-2 text-xl font-bold title">提供</div>
            <div class="content">
              <ul>
                <li>・はんなりPythonの会</li>
                <li>・PyData Osaka</li>
                <li>・PyCon mini Hiroshima</li>
              </ul>
            </div>
          </div>
          <div class="powered-block">
            <div class="mt-4 mb-2 text-xl font-bold title">環境</div>
            <div class="content">
              今回のチュートリアルでは以下の環境を使用します。
            </div>
          </div>
          <div class="background-block">
            <div class="mt-4 mb-2 text-xl font-bold title"></div>
            <div class="content"></div>
          </div>
          <div class="environment-block">
            <div class="mt-4 mb-2 text-xl font-bold title">利用する環境</div>
            <div class="content">
              <ul>
                <li class="mt-4 mb-4">
                  今回のチュートリアルでは、以下のサービスを使用して動かす予定です。
                </li>
                <li>
                  ・
                  <a
                    href="https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja"
                    target="_blank"
                    rel="noopener noreferrer"
                    >Google Colaboratory</a
                  >
                </li>
                <li>
                  ・
                  <a
                    href="https://mybinder.org/"
                    target="_blank"
                    rel="noopener noreferrer"
                    >Binder</a
                  >
                </li>
                <li class="mt-4 mb-4">
                  そのため、事前にPythonをインストールしなくても大丈夫です。
                </li>
                <li class="mb-4">
                  Google
                  Colaboratoryのアカウントは事前に取得しておいてください。
                </li>
                <div>
                  <ul>
                    <li>利用予定のライブラリ</li>
                    <li>以下のPythonライブラリを使用します。</li>
                    <li>・pandas</li>
                    <li>・geopandas</li>
                    <li>・plotly</li>
                    <li>・deck.gl</li>
                    <li class="text-indent-one">・pydeck</li>
                    <li>・dash</li>
                    <li>・streamlit</li>
                    <li>・scikit-learn</li>
                  </ul>
                </div>
                <div class="mt-4">
                  そのほかに、Mapbox APIの利用申請が必要です。<br />
                  限度を超えると課金が必要ですが、このチュートリアルを受講するにあたっては無料枠で済むので課金しなくても大丈夫です。
                </div>
              </ul>
            </div>
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
    return { title: 'PyCon JP 2020', titleTemplate: null }
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
  "description": {
      "p-1": "This event is for a beginner to intermediate level at Python held on Sunday, August 30 - the day after the conference." ,
      "p-2": "Those who do not attend the conference can still participate in this tutorial." ,
      "p-3": "This year we will have two tutorials." ,
      "p-4": "Still, both tutorials assume that you have development knowledge in other(non-Python) programming languages." ,
      "event-one-title": "Learn the Python Development Ecosystem, Slack Bot Edition",
      "event-two-title": "Using Open Data to Analyze Data in Python"
    },
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
    "description": {
      "p-1": "カンファレンス翌日8/30（日）に行われるPython初心者〜中級者向けのイベントです。",
      "p-2": "カンファレンス本体に参加しない方もチュートリアルに参加可能です。",
      "p-3": "今年は以下の2種類のチュートリアルを行います。",
      "p-4": "なお、今年のチュートリアルではどちらもPython以外のプログラム言語での開発知識がある事を前提としています。",
      "event-one-title": "Pythonの開発エコシステムを学ぼう Slack Bot編",
      "event-two-title": "オープンデータを使って、Pythonでデータ分析"
    },
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
