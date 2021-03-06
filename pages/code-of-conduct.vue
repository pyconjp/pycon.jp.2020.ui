<template>
  <div class="flex flex-col items-center justify-start w-full mb-16 md:mb-32">
    <h1
      class="flex items-center justify-center w-screen h-32 mb-8 text-2xl font-semibold text-center text-py-black md:h-56 sm:text-3xl md:text-4xl lg:text-5xl m-screen"
    >
      {{ $t('pages.code-of-conduct.title') }}
    </h1>
    <div class="relative flex flex-col items-center justify-center">
      <div class="relative z-10 flex justify-center w-screen bg-white m-screen">
        <div
          class="w-11/12 px-6 border-4 border-solid sm:px-8 md:px-10 lg:px-12 md:w-4/5 border-py-black rounded-xl"
        >
          <div
            :class="
              isEnglish
                ? 'text-left leading-relaxed tracking-wide'
                : 'text-justify leading-7 tracking-wider'
            "
            class="flex flex-col items-start justify-start my-8 md:text-lg"
          >
            <p
              v-for="(paragraph, i) in $t('paragraphs')"
              :key="`p-${i}`"
              class="my-4"
            >
              {{ paragraph }}
            </p>
          </div>
        </div>
      </div>
      <div
        class="absolute top-0 w-20 h-20 -mt-8 border-4 border-solid border-py-black bg-py-black rounded-card-head"
      >
        <div class="relative">
          <div class="absolute w-2 h-2 mt-2 ml-6 bg-white rounded-full"></div>
          <div class="absolute w-2 h-2 mt-2 ml-10 bg-white rounded-full"></div>
        </div>
      </div>
    </div>

    <h1
      class="flex items-center justify-center w-screen h-32 mt-16 mb-8 text-2xl font-semibold text-center text-py-black md:h-56 sm:text-3xl md:text-4xl lg:text-5xl m-screen"
    >
      {{ $t('guideline.title') }}
    </h1>
    <div class="relative flex flex-col items-center justify-center">
      <div class="relative z-10 flex justify-center w-screen bg-white m-screen">
        <div
          class="w-11/12 px-6 border-4 border-solid sm:px-8 md:px-10 lg:px-12 md:w-4/5 border-py-black rounded-xl"
        >
          <div
            :class="
              isEnglish
                ? 'text-left leading-relaxed tracking-wide'
                : 'text-justify leading-7 tracking-wider'
            "
            class="flex flex-col items-start justify-start my-8 md:text-lg"
          >
            <p
              v-for="(paragraph, i) in $t('guideline.section1')"
              :key="`s1-${i}`"
              class="my-4"
            >
              {{ paragraph }}
            </p>

            <p class="mt-4 mb-2 text-xl font-semibold">
              {{ $t('guideline.section2.title') }}
            </p>
            <p
              v-for="(paragraph, i) in $t('guideline.section2.paragraph')"
              :key="`s2-${i}`"
            >
              {{ paragraph }}
            </p>
            <p class="mt-6 mb-2 text-xl font-semibold">
              {{ $t('guideline.section3.title') }}
            </p>
            <p
              v-for="(paragraph, i) in $t('guideline.section3.paragraph')"
              :key="`s3-${i}`"
            >
              {{ paragraph }}
            </p>
            <p class="mt-6 mb-2 text-xl font-semibold">
              {{ $t('guideline.section4.title') }}
            </p>
            <p
              v-for="(paragraph, i) in $t('guideline.section4.paragraph')"
              :key="`s4-${i}`"
            >
              {{ paragraph }}
            </p>
            <p class="mt-6 mb-2 text-xl font-semibold">
              {{ $t('guideline.section5.title') }}
            </p>
            <p
              v-for="(paragraph, i) in $t('guideline.section5.paragraph')"
              :key="`s5-${i}`"
            >
              {{ paragraph }}
            </p>
            <p class="mt-6 mb-2 text-xl font-semibold">
              {{ $t('guideline.section6.title') }}
            </p>
            <p
              v-for="(paragraph, i) in $t('guideline.section6.paragraph')"
              :key="`s6-${i}`"
            >
              {{ paragraph }}
            </p>
          </div>
        </div>
      </div>
      <div
        class="absolute top-0 w-20 h-20 -mt-8 border-4 border-solid border-py-black bg-py-black rounded-card-head"
      >
        <div class="relative">
          <div class="absolute w-2 h-2 mt-2 ml-6 bg-white rounded-full"></div>
          <div class="absolute w-2 h-2 mt-2 ml-10 bg-white rounded-full"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
// import TalkContent from '~/components/Elements/TalkContent'

export default Vue.extend({
  components: {},
  computed: {
    isEnglish() {
      return this.$i18n.locale === 'en'
    },
  },
  head() {
    return { title: this.$t('pages.code-of-conduct.title') }
  },
})
</script>

<i18n>
{
  "en": {
    "paragraphs": {
      "p-1": "PyCon JP is a conference organized and run by volunteers in the Japanese Python community that is dedicated to advancing and promoting the Python programming language. Through holding the PyCon JP conference, Python users can gather and exchange information with other deveopers from a wide variety of fields. It is our aim to create new relationships between the different communities and businesses using Python.",
      "p-2": "Harassment includes offensive verbal comments related to gender, age, sexual orientation, disability, physical appearance, body size, race, religion, sexual images in public spaces, deliberate intimidation, stalking, following, harassing photography or recording, sustained disruption of talks or other events, inappropriate physical contact, and unwelcome sexual attention.",
      "p-3": "Participants asked to stop any harassing behavior are expected to comply immediately.",
      "p-4": "Sponsors are also subject to the anti-harassment policy. In particular, sponsors should not use sexualised images, activities, or other material. Booth staff (including volunteers) should not use sexualised clothing/uniforms/costumes, or otherwise create a sexualised environment.",
      "p-5": "If a participant engages in harassing behavior, the conference organisers may take any action they deem appropriate, including warning the offender or expulsion from the conference with no refund.",
      "p-6": "If you are being harassed, notice that someone else is being harassed, or have any other concerns, please contact a member of conference staff immediately. Conference staff can be identified as they'll be wearing branded t-shirts.",
      "p-7": "* PyCon JP 2020 is held Online, so let a member of staff know by email in that case instead of finding a conference staff with branded t-shirts.",
      "p-8": "Conference staff will be happy to help participants contact hotel/venue security or local law enforcement, provide escorts, or otherwise assist those experiencing harassment to feel safe for the duration of the conference. We value your attendance.",
      "p-9": "We expect participants to follow these rules at conference and workshop venues and conference-related social events."
    },
    "guideline": {
      "title": "Guidelines of Conduct",
      "section1": {
        "p-0": "These are the guidelines of conduct based on PyCon JP Code of Conduct.To ensure an enjoyable and trouble free conference for all, participants are required to read and follow the following guidelines",
        "p-1": ""
      },
      "section2": {
        "title": "Respect, understanding and consideration",
        "paragraph": {
          "p-0": "- Treat all people (including but not limited to participants and speakers) and all objects in the conference with respect.",
          "p-1": "- Always keep it in mind that each person and each object has their own background and circumstances.",
          "p-2": "- Have empathy for others and communicate carefully."
        }
      },
      "section3": {
        "title": "Careful conduct and legal compliance",
        "paragraph": {
          "p-0": "- Even trivial or non-malicious comments or actions could be misunderstood as harassment. Even small actions will remain on the log and can be focused on or spread unintentionally. For example, any mentions about someone's appearance, even if it is a compliment, could be treated as harassment.",
          "p-1": "- Your display name, icon, avatar, and the things, such as background images, displayed by you may also be streamed online. You need to take full responsibility for using them. Be careful, especially not to violate copyrights, and not to do harassment.",
          "p-2": "- Direct message to other attendees will be disabled during the conference except for an online meetup after the conference. You can send a direct message to a conference staff anytime."
        }
      },
      "section4": {
        "title": "Calm and Patience",
        "paragraph": {
          "p-0": "- You might feel uncomfortable, stressed or upset by actions by others, unclear information, poor responses, or any other reason. Note that nobody’s perfect.",
          "p-1": "- If you feel uncomfortable, upset or stressed, please take a minute to calm down rather than reacting out of reflex if possible. Try to stay calm and be patient."
        }
      },
      "section5": {
        "title": "Courage and appropriate action",
        "paragraph": {
          "p-0": "- If you are harassed or you see someone harassed, let a member of staff know. Do not assume someone else will do it.",
          "p-1": "- DO NOT take direct action on your own in the case above. Inform the staff so cases can be handled correctly."
        }
      },
      "section6": {
        "title": "Contact Information",
        "paragraph": {
          "p-0": "If you feel harassed or you see someone violate the code of conduct (including doing harassment), let event staff know immediately by email).",
          "p-1": "* CoC team includes both male and female staff."
        }
      }
    }
  },
  "ja": {
    "paragraphs": {
      "p-1": "PyConは、Pythonユーザが集まり、PythonやPythonを使ったソフトウェアについて情報交換、交流をするためのカンファレンスです。 PyConJPの開催を通じて、Pythonの使い手が一堂に集まり、Pythonにまつわる様々な分野の知識や情報を交換し、新たな友達やコミュニティとのつながり、仕事やビジネスチャンスを増やせる場所とすることが目標です。",
      "p-2": "ハラスメント行為には、言葉による性別、性的指向、障碍の有無、外見、身体の大きさ、人種、宗教に関する攻撃的なコメント、公的空間での性的な映像表現、意図的な威力行為、ストーキング、つきまとい、写真撮影や録音によるいやがらせ、トークやその他の会議イベントに対して繰り返して中断しようとする行為、不適切な身体接触、そして望まれない性的な注意を引きつける行為を含みます。",
      "p-3": "参加者は、これらのハラスメント行為を止めるように求められた場合、すぐに従わなければなりません。",
      "p-4": "スポンサーもまた反ハラスメント行為ポリシーに従わなければなりません。特に、スポンサーは性的な関心を引き起こす映像表現、活動、あるいはその他の物品を使うべきではありません。ボランティアを含め、ブースのスタッフは、性的な関心を引き起こすような服装/制服/コスチュームを使うべきではありませんし、その他の手段で性的な関心を引き起こすような環境を作ることもすべきではありません。",
      "p-5": "もしあなたがハラスメントに遭った場合、他の人がハラスメントに遭っている場合、あるいは他に気になることがあった時は、すぐに会議スタッフの誰かに連絡していただくようお願いします。会議スタッフは会議のブランドを付けたTシャツを着ています。",
      "p-6": "※PyCon JP 2020はオンライン開催のため、CoCに関する連絡用メールアドレス宛に連絡をお願いします(Tシャツを着た現地スタッフを探す必要はありません)。※CoCに関する連絡用メールアドレスはクローズしました",
      "p-7": "会議スタッフは、ハラスメントを経験した人が、会議期間中安全かつ安心と感じられるように、参加者がホテル/会場の警備や近隣の警察に連絡すること、付き添い者の提供、およびその他の支援を行います。私達にとってあなたが参加しているのは大事なことなのです。",
      "p-8": "私達は参加者が会議場とワークショップ会場、また会議に関連したソーシャルイベントにて、このルールに従うことを望みます。"
    },
    "guideline": {
      "title": "行動ガイドライン",
      "section1": {
        "p-0": "全ての参加者・そしてあなた自身も、安心してイベントが楽しめるよう、PyCon JP 行動規範をより具体的にした行動のガイドラインを用意しました。",
        "p-1": "オンライン開催という特性上、意図しているか否かにかかわらず自身の行動がハラスメント行為と捉えられてしまう恐れや、ちょっとしたコメントがフォーカスされて大きく取り上げられてしまう恐れがあります。行動のガイドラインを確認・遵守することで、トラブル無くカンファレンスを楽しんでいただけることを望みます。"
      },
      "section2": {
        "title": "敬意・理解・思いやり",
        "paragraph": {
          "p-0": "- 参加者、スピーカー、その他イベントで関わる全ての人・モノに対して、敬意を持って接してください。",
          "p-1": "- イベントで接する様々な人・モノに対して、それぞれが個別のバックグラウンドや事情を持っていることを理解しようと努めてください。",
          "p-2": "- イベントで接する相手に対して思いやりをもち、自身の行動を相手に合わせるようなコミュニケーションをお願いします。"
        }
      },
      "section3": {
        "title": "注意深い行動・法令遵守",
        "paragraph": {
          "p-0": "- 些細な、または悪意がない発言・行動であっても、発信する前に、ハラスメント行為と誤解される可能性がないか注意してください。小さなアクションでも、ログ上に残ったものがフォーカスされ、拡散される可能性があります。例えば、容姿に関して言及することは、褒める行為であってもハラスメントとして扱われることに留意してくだいさい。",
          "p-1": "- あなたの表示名・アイコン/アバター・背景に映るモノも、オンラインで配信される可能性があり、あなたに使用責任が伴います。法令遵守(特に著作権関係)と行動規範遵守(特にハラスメント関連)となっているか注意を払ってください。",
          "p-2": "- スタッフへの問い合わせ及び交流会を除いて、ダイレクトメッセージ機能の使用は禁止いたします。"
        }
      },
      "section4": {
        "title": "冷静さと忍耐",
        "paragraph": {
          "p-0": "- 相手から自身が不快に感じる言動を受けることや、情報のあいまいさ・レスポンスの悪さ・相手にうまく伝わらない等の様々なストレスに直面することがあるかもしれません。イベント参加者・関係者全員が完璧な行動ができるわけではないことに、理解と留意をお願いします。",
          "p-1": "- 不快さ・ストレスを感じても、感情に任せて反射的に行動するのではなく、少し間を取って落ち着くことを心がけ、忍耐深く、常に冷静でいるようお願いします。"
        }
      },
      "section5": {
        "title": "勇気と適切な行動",
        "paragraph": {
          "p-0": "- ハラスメント行為を受けたと感じたり、見かけた場合は、見過ごすこと無くスタッフまでお知らせください。",
          "p-1": "- 上記の場合にも、必ずスタッフに連絡することとし、自身で判断して対処しないようお願いします(さらなるトラブルに巻き込まれる可能性があります)。"
        }
      },
      "section6": {
        "title": "連絡先",
        "paragraph": {
          "p-0": "CoC違反を目撃した場合、ハラスメントを受けた・見かけたと感じた場合は、直ちにお知らせください。(男女両方のスタッフを含む限定されたメンバーが対応します。)",
          "p-1": "※CoCに関する連絡用メールアドレスはクローズしました"
        }
      }
    }
  }
}
</i18n>
