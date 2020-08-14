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
                  <div
                    class="flex justify-start w-2/3 mt-2 md:justify-center md:items-center md:w-3/12"
                  >
                    <fa class="text-2xl text-gray-700" :icon="faPlayCircle" />
                    <p class="ml-2">Live</p>
                  </div>
                  <!-- Document Link -->
                  <div
                    class="flex items-center justify-start w-2/3 mt-2 md:justify-center md:w-3/12"
                  >
                    <fa class="text-2xl text-gray-700" :icon="faFileAlt" />
                    <p class="ml-2">Document</p>
                  </div>
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
              <p class="text-lg font-medium">{{ speakerName }}</p>
              <div class="mt-4">
                <p class="text-lg font-medium">エレベーターピッチ</p>
                <div
                  class="list_style"
                  v-html="$md.render(elevatorPitch)"
                ></div>
              </div>
              <div class="mt-4">
                <p class="text-lg font-medium">聴衆に求める前提知識</p>
                <div
                  class="list_style"
                  v-html="$md.render(prerequisiteKnowledge)"
                ></div>
              </div>
              <div class="mt-4">
                <p class="text-lg font-medium">
                  聴衆が持ち帰ることができるもの
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
                  <p
                    class="inline-block px-4 text-center bg-gray-300 rounded-lg md:rounded-xl"
                  >
                    {{ track }}
                  </p>
                </div>
                <p>Level</p>
                <div>
                  <p
                    class="inline-block px-4 text-center bg-gray-300 rounded-lg md:rounded-xl"
                  >
                    {{ audiencePythonLevel }}
                  </p>
                </div>
                <p>Audience expertise</p>
                <div>
                  <p
                    class="inline-block px-4 text-center bg-gray-300 rounded-lg md:rounded-xl"
                  >
                    {{ audienceExpertise }}
                  </p>
                </div>
                <p>Language</p>
                <div>
                  <p
                    class="inline-block px-4 text-center bg-gray-300 rounded-lg md:rounded-xl"
                  >
                    {{ langOfTalk }}
                  </p>
                </div>
                <p>発表資料の言語</p>
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
export default {
  props: {
    sessionData: {
      type: Object,
      default() {
        return {
          title: '',
          name: '',
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
    this.youtubeLink = ''
    this.documentLink = ''
    this.elevatorPitch = this.sessionData.elevator_pitch
    this.prerequisiteKnowledge = this.sessionData.prerequisite_knowledge
    this.audienceTakeaway = this.sessionData.audience_takeaway
    this.talkFormat = this.sessionData.talk_format
    this.track = this.sessionData.track
    this.audiencePythonLevel = this.sessionData.audience_python_level
    this.audienceExpertise = this.sessionData.audience_expertise
    this.langOfTalk = this.sessionData.lang_of_talk ? 'JP' : 'EN'
    this.langOfSlide = this.sessionData.lang_of_slide ? 'JP' : 'EN'
    this.description = this.sessionData.description
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
