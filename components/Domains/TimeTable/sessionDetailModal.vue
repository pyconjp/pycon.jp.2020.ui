<template>
  <transition name="modal" appear>
    <div class="modal modal-overlay" @click.self="$emit('close')">
      <div class="modal-window">
        <!-- ヘッダーエリア -->
        <div id="modal-content" class="modal-content text-py-black">
          <div class="flex bg-white outer_radius">
            <div class="flex justify-center w-3/4 mt-6 md:w-11/12">
              <div class="w-10/12">
                <p class="text-xl font-semibold">
                  {{ sessionTitle }}
                </p>
                <div
                  class="flex flex-col items-start justify-start mt-4 mb-2 md:flex-row"
                >
                  <!-- Language and Level -->
                  <div
                    class="flex items-center justify-center w-2/3 mt-2 md:w-4/12"
                  >
                    <div
                      class="w-1/6 font-bold text-center border-t border-b border-l rounded-l-lg border-py-blue-dark text-py-blue-dark"
                    >
                      {{ langOfTalk }}
                    </div>
                    <div
                      class="w-5/6 font-bold text-center text-green-700 truncate border border-green-700 rounded-r-lg"
                    >
                      {{ audiencePythonLevel }}
                    </div>
                  </div>
                  <!-- YouTube Link -->

                  <a
                    :href="youtubeLink"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="flex justify-start w-2/3 mt-2 md:justify-center md:items-center md:w-3/12"
                  >
                    <fa class="text-2xl text-gray-700" :icon="faPlayCircle" />
                    <p class="ml-2">Live</p>
                  </a>
                  <!-- Document Link -->
                  <!-- <div
                    class="flex items-center justify-start w-2/3 mt-2 md:justify-center md:w-3/12"
                  >
                    <fa class="text-2xl text-gray-700" :icon="faFileAlt" />
                    <p class="ml-2">Document</p>
                  </div> -->
                </div>
              </div>
            </div>
            <div
              class="relative w-1/4 cursor-pointer md:w-1/12"
              @click.stop="$emit('close')"
            >
              <!-- <div class="snake_head"></div> -->
              <div class="snake_eye">
                <fa class="text-2xl" :icon="faTimes" />
              </div>
              <div class="snake_mouth"></div>
            </div>
          </div>

          <!-- コンテンツエリア -->
          <div class="flex justify-center mt-1 bg-white">
            <div class="w-10/12 my-4">
              <p class="text-sm text-gray-800">Speaker</p>
              <p class="-mt-1 text-lg font-medium">{{ speakerName }}</p>
              <p>{{ speakerProfile }}</p>
              <div class="mt-4">
                <p class="text-lg font-medium">{{ $t('elevatorPitch') }}</p>
                <div
                  class="list_style"
                  v-html="$md.render(elevatorPitch)"
                ></div>
              </div>
              <div class="mt-4">
                <p class="text-lg font-medium">{{ $t('requiredKnowledge') }}</p>
                <div
                  class="list_style"
                  v-html="$md.render(prerequisiteKnowledge)"
                ></div>
              </div>
              <div class="mt-4">
                <p class="text-lg font-medium">
                  {{ $t('knowledgeGained') }}
                </p>
                <div
                  class="list_style"
                  v-html="$md.render(audienceTakeaway)"
                ></div>
              </div>

              <!-- セッション情報 -->
              <div class="grid grid-cols-2 row-gap-1 mt-4">
                <p>Session format</p>
                <div>
                  <p class="inline-block px-4 bg-gray-300 rounded-xl">
                    {{ talkFormat }}
                  </p>
                </div>
                <p>Track</p>
                <div>
                  <a
                    href="https://pyconjp.blogspot.com/2020/04/pyconjp-2020-proposal-track.html"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <p
                      class="inline-block px-4 text-center underline bg-gray-300 rounded-lg md:rounded-xl hover:text-blue-500"
                    >
                      {{ track }}
                    </p>
                  </a>
                </div>
                <p>Level</p>
                <div>
                  <a
                    href="https://pyconjp.blogspot.com/2020/04/pyconjp-2020-proposal-audience-information.html"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <p
                      class="inline-block px-4 text-center underline bg-gray-300 rounded-lg md:rounded-xl hover:text-blue-500"
                    >
                      {{ audiencePythonLevel }}
                    </p></a
                  >
                </div>
                <p>Audience expertise</p>
                <div>
                  <a
                    href="https://pyconjp.blogspot.com/2020/04/pyconjp-2020-proposal-audience-information.html"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <p
                      class="inline-block px-4 text-center underline bg-gray-300 rounded-lg md:rounded-xl hover:text-blue-500"
                    >
                      {{ audienceExpertise }}
                    </p></a
                  >
                </div>
                <p>Talk Language</p>
                <div>
                  <p
                    class="inline-block px-4 text-center bg-gray-300 rounded-lg md:rounded-xl"
                  >
                    {{ langOfTalk }}
                  </p>
                </div>
                <p>Slide Language</p>
                <div>
                  <p
                    class="inline-block px-4 text-center bg-gray-300 rounded-lg md:rounded-xl"
                  >
                    {{ langOfSlide }}
                  </p>
                </div>
              </div>

              <div class="mt-4">
                <p class="text-lg font-medium">
                  Description
                </p>
                <div
                  v-show="!isDescriptionOpen"
                  class="flex flex-col items-center justify-center cursor-pointer"
                  @click.stop="isDescriptionOpen = true"
                >
                  <p class="underline">Read more</p>
                  <i
                    class="text-2xl align-middle transform rotate-180 material-icons"
                    >change_history</i
                  >
                </div>
                <div
                  v-show="isDescriptionOpen"
                  class="list_style"
                  v-html="$md.render(description)"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import {
  faPlayCircle,
  faFileAlt,
  faTimes,
} from '@fortawesome/free-solid-svg-icons'
import { disableBodyScroll, clearAllBodyScrollLocks } from 'body-scroll-lock'
import { getYoutubeLiveLink } from '~/lib/youtute-link'

export default {
  props: {
    sessionData: {
      type: Object,
      default() {
        return {
          title: '',
          name: '',
          profile: '',
          elevator_pitch: '',
          prerequisite_knowledge: '',
          audience_takeaway: '',
          talk_format: '',
          track: '',
          audience_python_level: '',
          audience_expertise: '',
          lang_of_talk: '',
          lang_of_slide: '',
          description: '',
          room: '',
        }
      },
    },
  },
  data() {
    return {
      // セッション情報表示用
      sessionTitle: '',
      speakerName: '',
      speakerProfile: '',
      youtubeLink: '',
      documentLink: '',
      elevatorPitch: '',
      prerequisiteKnowledge: '',
      audienceTakeaway: '',
      talkFormat: '',
      track: '',
      audiencePythonLevel: '',
      audienceExpertise: '',
      langOfTalk: '',
      langOfSlide: '',
      description: '',

      // Read more表示しているかどうか
      isDescriptionOpen: false,
    }
  },
  computed: {
    faPlayCircle() {
      return faPlayCircle
    },
    faFileAlt() {
      return faFileAlt
    },
    faTimes() {
      return faTimes
    },
  },
  created() {
    this.sessionTitle = this.sessionData.title
    this.speakerName = this.sessionData.name
    this.speakerProfile = this.sessionData.profile
    // TODO: 開催後YouTubeのリンクを修正すること
    this.youtubeLink = getYoutubeLiveLink()[
      `pyconjp${this.sessionData.room.slice(-1)}`
    ]
    this.documentLink = ''
    this.elevatorPitch = this.sessionData.elevator_pitch
    this.prerequisiteKnowledge = this.sessionData.prerequisite_knowledge
    this.audienceTakeaway = this.sessionData.audience_takeaway
    this.talkFormat = this.sessionData.talk_format
    this.track = this.sessionData.track
    this.audiencePythonLevel = this.sessionData.audience_python_level
      ? this.sessionData.audience_python_level
      : 'All'
    this.audienceExpertise = this.sessionData.audience_expertise
    this.langOfTalk = this.sessionData.lang_of_talk ? 'JA' : 'EN'
    this.langOfSlide = this.sessionData.lang_of_slide ? 'JA' : 'EN'
    this.description = this.sessionData.description
    this.description = this.sessionData.description.replace(/\n/g, '\n\n')
  },
  mounted() {
    const targetElement = document.querySelector('#modal-content')
    disableBodyScroll(targetElement)
  },
  beforeDestroy() {
    clearAllBodyScrollLocks()
  },
}
</script>

<style lang="scss">
.modal {
  &.modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 30;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
  }

  &-window {
    background: #eef0f5;
    border-radius: 32px;
    overflow: scroll;
    width: 85%;
    max-height: 80%;
    overflow-x: hidden;

    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
  }
  &-window::-webkit-scrollbar {
    display: none;
  }

  &-content {
    padding: 8px 12px;
    display: flex;
    flex-direction: column;
    // max-height: 100%;
  }
}

// オーバーレイのトランジション
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.4s;

  // オーバーレイに包含されているモーダルウィンドウのトランジション
  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }
}

// ディレイを付けるとモーダルウィンドウが消えた後にオーバーレイが消える
.modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.modal-enter,
.modal-leave-to {
  opacity: 0;

  .modal-window {
    opacity: 0;
    transform: translateY(-20px);
  }
}

.snake {
  &_head {
    border-radius: 0 64px 0 0;
    background-color: white;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    right: -8px;
  }
  &_eye {
    position: absolute;
    display: flex;
    border-radius: 999px;
    justify-content: center;
    align-items: center;
    width: 2rem;
    height: 2rem;
    // background-color: aqua;
    top: 1.4rem;
    left: 0.4rem;
    color: #4a5568;
  }
  &_eye:hover {
    background-color: #4a5568;
    color: white;
  }
  &_mouth {
    position: absolute;
    background-color: #eef0f5;
    width: 100%;
    height: 4.5rem;
    bottom: 0;
    right: -12px;
  }
}

@media screen and (min-width: 768px) {
  .snake {
    &_mouth {
      height: 1.5rem;
    }
  }
}

.outer_radius {
  border-radius: 36px 36px 0 0;
}

ul {
  list-style-type: disc;
}

.list_style {
  ul {
    list-style-type: disc;
    padding-left: 1rem;
  }
}
</style>

<i18n>
{
  "en": {
    "elevatorPitch": "Elevator Pitch",
    "requiredKnowledge": "Prerequisite knowledge required from the audience",
    "knowledgeGained": "Knowledge that the audience can take home"
  },
  "ja": {
    "elevatorPitch": "エレベーターピッチ",
    "requiredKnowledge": "聴衆に求める前提知識",
    "knowledgeGained": "聴衆が持ち帰ることができるもの"
  }
}
</i18n>
