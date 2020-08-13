<template>
  <section class="">
    <div class="relative">
      <div class="flex flex-col items-center title-block">
        <h2 class="inline mb-2 text-4xl font-semibold md:text-6xl">
          Sprint
        </h2>
        <p class="mb-8 text-xl md:text-2xl">-Sprint-</p>
      </div>
      <div class="flex flex-col">
        <div class="flex flex-wrap items-center justify-center md:flex-no-wrap">
          <div class="w-full md:w-1/2 xl:w-1/3">
            <p class="mb-0 text-5xl font-bold text-center md:mr-8">
              2020.08.22<span class="ml-2 text-lg text-blue-600">(Sat)</span>
            </p>
            <p class="text-5xl font-bold text-center md:mr-8">
              - 30<span class="ml-2 text-lg text-blue-600">(Sun)</span>
            </p>
          </div>
          <div class="flex justify-center w-full mt-8 md:w-1/3 lg:w-1/2">
            <img
              :src="require('~/assets/img/sprint/sprint.png')"
              class="z-10 w-full h-full rounded-xl"
            />
          </div>
        </div>
        <div class="mt-12 md:mt-20 lg:ml-10">
          <div>
            <p
              v-for="(message, key) in $t('description')"
              :key="key"
              class="m-0 text-base"
            >
              {{ message }}
            </p>
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
    <div class="pt-24 pb-24 mt-24 way-to-join-block m-screen">
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
                class="inline-block w-10/12 mx-0 mb-6 md:w-8/12 lg:my-3 lg:ml-4"
              >
                <a
                  class="text-2xl text-blue-400 no-underline"
                  href="https://pyconjp.connpass.com/event/183507/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <button
                    class="flex items-center w-full h-20 px-4 py-2 font-medium duration-200 bg-white rounded-full shadow xl:w-9/12 xl:ml-10 transition-color group md:px-6 md:py-6 text-py-black hover:bg-py-black focus:outline-none"
                  >
                    <p
                      class="w-6 h-6 rounded-full bg-py-black group-hover:bg-white"
                    />
                    <span
                      class="ml-2 md:text-xl md:ml-6 md:mr-4 group-hover:text-white"
                      >{{ $t('sprint.connpass') }}</span
                    >
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
            PyCon JP 2020 Sprint
          </template>
        </python-banner>

        <div class="mt-16">
          <div>
            <div class="mb-2 text-2xl font-bold title">
              {{ $t('contents.section1.title') }}
            </div>
            <p
              v-for="(message, key) in $t('contents.section1.description')"
              :key="key"
              class="mt-2"
            >
              {{ message }}
            </p>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              {{ $t('contents.section2.title') }}
            </div>
            <p
              v-for="(message, key) in $t('contents.section2.description')"
              :key="key"
              class="mt-2"
            >
              {{ message }}
            </p>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              {{ $t('contents.section3.title') }}
            </div>
            <p class="mt-2 mb-8">
              {{ $t('contents.section3.description.p-1') }}
            </p>
            <div class="w-full overflow-x-scroll">
              <table>
                <thead>
                  <tr>
                    <th
                      v-for="(message, key) in $t('contents.section3.table')"
                      :key="`table-${key}`"
                    >
                      {{ message }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>2020/08/22 ({{ $t('weekday.friday') }})</td>
                    <td>13:00</td>
                    <td>Zoom/Discord</td>
                    <td>
                      {{ $t('contents.section3.description.p-2') }}
                    </td>
                  </tr>
                  <tr>
                    <td>
                      2020/08/23 ({{ $t('weekday.sunday') }}) ~ 8/29 ({{
                        $t('weekday.saturday')
                      }})
                    </td>
                    <td>-</td>
                    <td>Discord</td>
                    <td>
                      {{ $t('contents.section3.description.p-3') }}
                    </td>
                  </tr>
                  <tr>
                    <td>
                      2020/08/28 ({{ $t('weekday.friday') }}) ~ 8/29 ({{
                        $t('weekday.saturday')
                      }})
                    </td>
                    <td>-</td>
                    <td>-</td>
                    <td>
                      {{ $t('contents.section3.description.p-4') }}
                    </td>
                  </tr>
                  <tr>
                    <td>2020/08/30 ({{ $t('weekday.sunday') }})</td>
                    <td>15:00</td>
                    <td>Zoom/Discord</td>
                    <td>
                      {{ $t('contents.section3.description.p-5') }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              {{ $t('contents.section4.title') }}
            </div>
            <p class="mt-2">
              {{ $t('contents.section4.description.p-1') }}
            </p>
            <nuxt-link
              :to="localePath('/code-of-conduct')"
              class="block mt-2 text-blue-600 underline cursor-pointer"
            >
              {{ $t('contents.section4.description.p-2') }}</nuxt-link
            >
          </div>
          <div class="mt-8">
            <div class="mb-2 text-2xl font-bold title">
              {{ $t('contents.section5.title') }}
            </div>
            <p
              v-for="(message, key) in $t('contents.section5.description')"
              :key="key"
              class="mt-2"
            >
              {{ message }}
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
table,
td {
  border: 1px solid #333;
  text-align: center;
}
td {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}
th {
  border: 1px solid #333;
}

thead,
tfoot {
  background-color: #d4d4ff;
  color: rgb(45, 55, 72);
}
</style>

<i18n>
{
"en": {
  "description": {
      "p-1": "We're looking for people interested in attending and leading sprints at PyCon JP 2020." ,
      "p-2": "The sprints will be held on Saturday, August 22nd to 30th(JST) Online and are free to attend for anyone, you do not require a PyCon JP 2020 ticket!" ,
      "p-3": "You can join Sprint for a week or even a day as many days as you can meet the project goal."
    },
    "title": "How to attend",
    "paragraphs": {
      "p-1": "Apply via connpass"
    },
    "sprint": {
      "connpass": "Join Sprint"
    },
    "contents": {
      "section1": {
        "title": "What is a sprint?",
        "description": {
          "p-1":"Most open source software development happens on the web and developers usually communicate only online when working on projects.This usually works out fine, but the lack of in-person meetings can sometimes be a limiting factor in making good progress.",
          "p-2": "For this reason, a form of impromptu coding meetups called “sprints” or “hackathons” (outside the Python community, the term “hackathon” is more common) were initiated, where developers interested in a project can get together in person for a short term to make quick progress.Since conferences provide the perfect place to meet, sprints are made part of the conference program.",
          "p-3": "PyCon JP 2020 will provide the space and infrastructure, such as Discord for communication and Zoom for shearing your project; you bring your skills, humanity, brainpower, computer and passion."
        }
      },
      "section2": {
        "title": "What is a Sprint Leader?",
        "description": {
          "p-1":"A Sprint Leader is the person who is informally in charge of a specific project at the sprint.They do not have to be the maintainer(or manager) of the project.As a Sprint Leader, you should pick a specific project you want to work on and have some specific goals you wish to achieve at the sprint can be helpful. Others might want to join your project, so please help them getting started in it.",
          "p-2": "The Sprint Leader system is very informal and you can work on any project you want, whether it has a leader or not.",
          "p-3": "If you want to be a Sprint Leader, please indicate on this connpass event page.And please submit your sprint topic via the Google Form(you can see this on this page after applying this event).You may fill the form in either English or Japanese. We will publish the list of submitted topics on our web page for other attendees can decide to join your sprint."
        }
      },
      "section3": {
        "title": "When/Where are the sprints?",
        "description": {
          "p-1": "PyConJP 2020 is held online. Here is the schedule for Sprint.",
          "p-2": "Kick-off",
          "p-3": "Sprint Week",
          "p-4": "PyCon JP 2020 Conference day",
          "p-5": "Result Presentation"
        },
        "table": {
          "date": "Date(JST)",
          "time": "Time(JST)",
          "tool": "Tools",
          "content": "Content"
        }
      },
      "section4": {
        "title": "Code of Conduct",
        "description": {
          "p-1": "At PyCon JP 2020, we ask all participants and staff to comply with the Code of Conduct in order to enjoy sprints with peace of mind. Please check the contents below and participate in the sprint.",
          "p-2": "PyCon JP 2020 Code of Conduct"
        }
      },
      "section5": {
        "title": "Contact",
        "description": {
          "p-1": "Contact Email : pyconjp [at] pycon.jp",
          "p-2": "As we are a volunteer run conference, it may take a few days for us to answer, thank you for your patience.",
          "p-3": "If you use the messaging feature on connpass.com, the response may be further delayed due to how that system works."
        }
      }
    },
    "weekday": {
      "friday": "Fri.",
      "saturday": "Sat.",
      "sunday": "Sun."
    }
  },
  "ja": {
    "description": {
      "p-1": "PyCon JP 2020のスプリント参加者およびスプリントリーダーの募集を開始しました！",
      "p-2": "今年のスプリントは、8/22（土）から8/30（日）までの1週間オンラインで開催いたします。 みなさんのテーマの目的を達成できるなら、期間中すべて活動頂いても、1日だけ活動頂いてもOKです。 （キックオフ時にプロジェクトごとに決めていただきます。）",
      "p-3": "本イベントに登録頂くだけで、どなたでも無料で参加いただけます！スプリント参加にあたってPyCon JP 2020カンファレンス参加のチケットは必要ありません。"
    },
    "title": "参加方法",
    "paragraphs": {
      "p-1": "connpass経由で申し込みをお願いします"
    },
    "sprint": {
      "connpass": "スプリント参加"
    },
    "contents": {
      "section1": {
        "title": "スプリントとは？",
        "description": {
          "p-1":"多くのオープンソースソフトウェアの開発は、ウェブ上でオンラインのコミュニケーションを通じて行われています。ほとんどの場合はオンライン上で事足りますが、時には集まって共同開発を行うことが、開発を大きく前に進めるために有効なことがあります。",
          "p-2": "特定のプロジェクトに興味がある開発者同士が集まって、短時間で素早く進捗を出す開発ミートアップを実現するイベントとして、スプリントやハッカソンが生まれました。 開発者が一同に集まるカンファレンスが、こういったスプリントを実現する場として最適な場であるため、カンファレンスの一部としてスプリントが開かれることがあります。",
          "p-3": "PyCon JP 2020のスプリントでは、コミュニケーションの場（Discord）と発表の場を用意します。スプリント参加者の皆さんには、ご自分のPC、スキル、そして開発への情熱を持ってご参加ください！"
        }
      },
      "section2": {
        "title": "スプリントリーダーとは？",
        "description": {
          "p-1":"スプリントリーダーは、スプリントで扱うテーマを決め、プロジェクトを立ち上げていただきます。 スプリントの中に開発の案内や参加者からの相談に乗っていただくロールになります。",
          "p-2": "リーダーは、開発を進めるプロジェクトの責任者である必要はありません。 リーダーは、自分が開発を進めたいと思うプロジェクトを立ち上げて頂き、スプリントで達成したいゴールを持って頂くだけで構いません。",
          "p-3": "スプリントリーダーの皆さんには、参加者の皆さんに自分が立ち上げたプロジェクトの紹介や開発の進め方の案内を行って頂きます。 また、開発中には適宜相談の対応をお願いします。",
          "p-4": "スプリントリーダーは形式上のものなので、他のプロジェクトに興味があった場合にはそちらに参加して頂いても構いません。",
          "p-5": "スプリントリーダーとして参加したい場合には、本connpassページで申込時にスプリントリーダーとして登録をお願いいたします。また、申込み後に表示される「参加者への情報」に記載されているフォームに回答し、スプリントで取り組みたいテーマを提出してください。フォームへの回答は日本語または英語でお願いします。",
          "p-6": "スプリント参加者が閲覧できるように、応募されたテーマは後ほど一覧にして公開します。\n ※一覧の内容はリーダーの入力内容に基づきます。",
          "p-7": "※一覧の内容はリーダーの入力内容に基づきます。"
        }
      },
      "section3": {
        "title": "スプリント開催場所/スケジュール",
        "description": {
          "p-1": "PyConJP 2020はオンラインで開催いたします。 スケジュールは以下のとおりです。",
          "p-2": "キックオフイベント",
          "p-3": "スプリント",
          "p-4": "PyCon JP 2020 カンファレンス",
          "p-5": "成果報告会"
        },
        "table": {
          "date": "日付",
          "time": "時間",
          "tool": "ツール",
          "content": "内容"
        }
      },
      "section4": {
        "title": "行動規範遵守のお願い",
        "description": {
          "p-1": "PyCon JP 2020では安心してスプリントを楽しんで頂くため、参加者およびスタッフ全員に行動規範の遵守をお願いしています。 下記より内容をご確認の上、スプリントへのご参加をお願いします。",
          "p-2": "PyCon JP 2020 行動規範"
        }
      },
      "section5": {
        "title": "お問い合わせ先",
        "description": {
          "p-1": "pyconjp [ at ] pycon.jpまでメールで問い合わせてください。 ボランティアによる運営ですので、回答は数日お待ちください。",
          "p-2": "connpassの[イベント管理者への問い合わせ]機能を使用した場合はメール回答に使用するシステム上の制限により、回答が更に遅れることがあります。"
        }
      }
    },
    "weekday": {
      "friday": "金",
      "saturday": "土",
      "sunday": "日"
    }
  }
}
</i18n>
