<template>
  <div class="flex flex-col items-center justify-start w-full mb-16 md:mb-32">
    <h1
      class="flex items-center justify-center w-screen h-32 text-2xl font-semibold text-center text-py-black md:h-56 sm:text-3xl md:text-4xl lg:text-5xl m-screen"
    >
      {{ $t('pages.code-of-conduct.title') }}
    </h1>
    <div class="relative flex flex-col items-center justify-center">
      <div class="relative z-10 flex justify-center w-screen bg-white m-screen">
        <div
          class="w-11/12 px-2 border-4 border-solid md:px-10 lg:px-16 md:w-4/5 border-py-black rounded-xl"
        >
          <div
            :class="
              isEnglish
                ? 'text-left leading-relaxed tracking-wide'
                : 'text-justify leading-7 tracking-wider'
            "
            class="flex flex-col items-start justify-start my-8 text-sm sm:text-base md:text-lg"
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
      "p-7": "Conference staff will be happy to help participants contact hotel/venue security or local law enforcement, provide escorts, or otherwise assist those experiencing harassment to feel safe for the duration of the conference. We value your attendance.",
      "p-8": "We expect participants to follow these rules at conference and workshop venues and conference-related social events."
    }
  },
  "ja": {
    "paragraphs": {
      "p-1": "PyConは、Pythonユーザが集まり、PythonやPythonを使ったソフトウェアについて情報交換、交流をするためのカンファレンスです。 PyConJPの開催を通じて、Pythonの使い手が一堂に集まり、Pythonにまつわる様々な分野の知識や情報を交換し、新たな友達やコミュニティとのつながり、仕事やビジネスチャンスを増やせる場所とすることが目標です。",
      "p-2": "ハラスメント行為には、言葉による性別、性的指向、障碍の有無、外見、身体の大きさ、人種、宗教に関する攻撃的なコメント、公的空間での性的な映像表現、意図的な威力行為、ストーキング、つきまとい、写真撮影や録音によるいやがらせ、トークやその他の会議イベントに対して繰り返して中断しようとする行為、不適切な身体接触、そして望まれない性的な注意を引きつける行為を含みます。",
      "p-3": "参加者は、これらのハラスメント行為を止めるように求められた場合、すぐに従わなければなりません。",
      "p-4": "スポンサーもまた反ハラスメント行為ポリシーに従わなければなりません。特に、スポンサーは性的な関心を引き起こす映像表現、活動、あるいはその他の物品を使うべきではありません。ボランティアを含め、ブースのスタッフは、性的な関心を引き起こすような服装/制服/コスチュームを使うべきではありませんし、その他の手段で性的な関心を引き起こすような環境を作ることもすべきではありません。",
      "p-5": "もしあなたがハラスメントに遭った場合、他の人がハラスメントに遭っている場合、あるいは他に気になることがあった時は、すぐに会議スタッフの誰かに連絡していただくようお願いします。会議スタッフは会議のブランドを付けたTシャツを着ています。",
      "p-6": "会議スタッフは、ハラスメントを経験した人が、会議期間中安全かつ安心と感じられるように、参加者がホテル/会場の警備や近隣の警察に連絡すること、付き添い者の提供、およびその他の支援を行います。私達にとってあなたが参加しているのは大事なことなのです。",
      "p-7": "私達は参加者が会議場とワークショップ会場、また会議に関連したソーシャルイベントにて、このルールに従うことを望みます。"
    }
  }
}
</i18n>
