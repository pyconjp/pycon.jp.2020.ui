<template>
  <div>
    <div class="flex flex-col items-center justify-center h-32 md:h-56">
      <h1
        class="flex items-center justify-center w-screen text-2xl font-semibold text-center text-py-black sm:text-3xl md:text-4xl lg:text-5xl m-screen"
      >
        Timetable
      </h1>
      <h3
        class="flex items-center justify-center w-screen mb-8 text-lg font-semibold text-center text-py-black sm:text-xl md:text-2xl lg:text-3xl m-screen"
      >
        {{ $t('pages["event-list"]["content-list"][0].title') }}
      </h3>
    </div>
    <div class="flex flex-row items-center justify-around w-full">
      <a
        v-for="platinum in $t('sponsor.platinum')"
        :key="platinum.companyName"
        :href="platinum.url"
        target="_blank"
        rel="noopener noreferrer"
        class="w-1/5"
      >
        <img :src="require(`~/assets/img/sponsor/${platinum.imagePath}`)"
      /></a>
    </div>

    <nuxt-link :to="localePath('/special-booth')" class="w-full banner">
      <img class="w-full mb-8" src="~/assets/img/57_12x.png" />
    </nuxt-link>

    <div class="w-full mb-8">
      <div class="flex justify-center w-full">
        <div
          class="flex items-start justify-center h-32 text-white cursor-pointer day_width bg-py-blue-dark rounded-2xl"
          @click="isDayOne = true"
        >
          <p class="tab_message_area md:mt-4 md:text-xl">
            Day 1 <span class="br tab_font_size md:text-4xl">08/28(Fri.)</span>
          </p>
        </div>
        <div
          class="flex items-start justify-center h-32 text-white cursor-pointer day_width bg-py-orange-dark rounded-2xl"
          @click="isDayOne = false"
        >
          <p class="tab_message_area md:mt-4 md:text-xl">
            Day 2 <span class="br tab_font_size md:text-4xl">08/29(Sat.)</span>
          </p>
        </div>
      </div>

      <!-- 1日目のタイムテーブル -->
      <div v-if="isDayOne" class="relative z-10 -mt-16 bg-white text-py-black">
        <div
          class="border-8 timetable_outer_style timetable_container border-py-blue-dark"
        >
          <div class="hidden border-r-4 border-py-blue-dark md:block"></div>
          <div class="flex flex-col items-center justify-center">
            <div
              v-if="!isTablet"
              class="grid items-center grid-cols-5 gap-2 mt-4 timetable_inner_width justify_centering"
            >
              <div
                v-for="index in [1, 2, 3, 4, 5]"
                :key="index"
                class="flex flex-col items-center justify-center w-full cursor-pointer box_style1 hover:bg-py-blue-light"
              >
                <a
                  :href="youtubeLiveUrlList[0][`#pyconjp_${index}`]"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <p class="font-bold text-center">#pyconjp_ {{ index }}</p>
                  <div class="flex items-center justify-center mt-2 mb-2">
                    <fa class="text-2xl text-gray-700" :icon="faPlayCircle" />
                    <p class="ml-2 underline">{{ $t('OnAir') }}</p>
                  </div>
                </a>
              </div>
            </div>

            <!-- オープニング -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>10:00</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('214734'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('214734').title }}
                </p>
              </div>
            </div>

            <!-- 基調講演 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>10:30</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('214736'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('214736').title }}
                </p>
              </div>
            </div>

            <!-- No.1の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>{{ getSessionTime(1, 0) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day1_line1_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('1', `#pyconjp_${index}`, '1')
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('1', `#pyconjp_${index}`, '1')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- PyconJP Association 運営会議 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>12:45</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('215380'))"
              >
                <p class="text-2xl font-bold text-center">
                  {{ getTargetSessionDataById('215380').title }}
                </p>
              </div>
            </div>

            <!-- No.2の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>{{ getSessionTime(1, 1) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day1_line2_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('1', `#pyconjp_${index}`, '2')
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('1', `#pyconjp_${index}`, '2')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- No.3の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>{{ getSessionTime(1, 2) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day1_line3_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('1', `#pyconjp_${index}`, '3')
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('1', `#pyconjp_${index}`, '3')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- スペシャルブースツアー -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>15:20</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('215383'))"
              >
                <p class="text-2xl font-bold text-center">
                  {{ getTargetSessionDataById('215383').title }}
                </p>
              </div>
            </div>

            <!-- No.4~6の行 -->
            <div
              v-for="outerIndex in [4, 5, 6]"
              :key="`outer${outerIndex}`"
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>{{ getSessionTime(1, outerIndex - 1) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width"
                :class="[`day1_line${outerIndex}_session_height`]"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData(
                      '1',
                      `#pyconjp_${index}`,
                      String(outerIndex)
                    )
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData(
                        '1',
                        `#pyconjp_${index}`,
                        String(outerIndex)
                      )
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- クロージング -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 mb-8 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style1">
                <p>18:30</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('214739'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('214739').title }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2日目のタイムテーブル -->
      <div v-else class="relative z-10 -mt-16 bg-white text-py-black">
        <div
          class="border-8 timetable_outer_style timetable_container border-py-orange-dark"
        >
          <div class="hidden border-r-4 border-py-orange-dark md:block"></div>
          <div class="flex flex-col items-center justify-center">
            <div
              v-if="!isTablet"
              class="grid items-center grid-cols-5 gap-2 mt-4 timetable_inner_width justify_centering"
            >
              <div
                v-for="index in [1, 2, 3, 4, 5]"
                :key="index"
                class="flex flex-col items-center justify-center w-full cursor-pointer box_style1 hover:bg-py-blue-light"
              >
                <a
                  :href="youtubeLiveUrlList[1][`#pyconjp_${index}`]"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <p class="font-bold text-center">#pyconjp_ {{ index }}</p>
                  <div class="flex items-center justify-center mt-2 mb-2">
                    <fa class="text-2xl text-gray-700" :icon="faPlayCircle" />
                    <p class="ml-2 underline">{{ $t('OnAir') }}</p>
                  </div>
                </a>
              </div>
            </div>

            <!-- オープニング -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>10:00</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('214735'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('214735').title }}
                </p>
              </div>
            </div>

            <!-- 基調講演 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>10:30</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('214737'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('214737').title }}
                </p>
              </div>
            </div>

            <!-- No.1の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>{{ getSessionTime(2, 0) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day2_line1_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('2', `#pyconjp_${index}`, '1')
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('2', `#pyconjp_${index}`, '1')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- スペシャルパネルディスカッション -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>13:00</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('214742'))"
              >
                <p class="text-2xl font-bold text-center">
                  {{ getTargetSessionDataById('214742').title }}
                </p>
              </div>
            </div>

            <!-- No.2の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>{{ getSessionTime(2, 1) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day2_line2_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('2', `#pyconjp_${index}`, '2')
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('2', `#pyconjp_${index}`, '2')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- No.3の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>{{ getSessionTime(2, 2) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day2_line3_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('2', `#pyconjp_${index}`, '3')
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('2', `#pyconjp_${index}`, '3')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- スペシャルブースツアー -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>15:20</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('215384'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('215384').title }}
                </p>
              </div>
            </div>

            <!-- No.4の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>{{ getSessionTime(2, 3) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day2_line4_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 4, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('2', `#pyconjp_${index}`, '4')
                  "
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('2', `#pyconjp_${index}`, '4')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- No.5の行 -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>{{ getSessionTime(2, 4) }}</p>
              </div>
              <div
                class="grid items-start grid-cols-1 grid-rows-1 gap-2 md:grid-cols-5 timetable_inner_width day2_line5_session_height"
              >
                <Session
                  v-for="index in [1, 2, 3, 5]"
                  :key="`outer${index}`"
                  :session-data="
                    getTargetSessionData('2', `#pyconjp_${index}`, '5')
                  "
                  :class="[`grid_layout_style${index}`]"
                  @click.native="
                    openSessionModal(
                      getTargetSessionData('2', `#pyconjp_${index}`, '5')
                    )
                  "
                ></Session>
              </div>
            </div>

            <!-- クロージング -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 mb-8 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>17:15</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('214740'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('214740').title }}
                </p>
              </div>
            </div>

            <!-- Online Party -->
            <div
              class="relative flex flex-col items-center justify-center w-full mt-4 mb-8 md:mt-16"
            >
              <div class="md:rounded-full time_balloon_style2">
                <p>18:15</p>
              </div>
              <div
                class="flex items-center justify-center w-full h-16 mt-2 cursor-pointer md:m-0 box_style1 timetable_inner_width rounded-xl hover:bg-py-blue-light"
                @click="openSessionModal(getTargetSessionDataById('215531'))"
              >
                <p class="text-2xl font-bold">
                  {{ getTargetSessionDataById('215531').title }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <SessionDetailModal
      v-if="isModal"
      :session-data="modalDisplaySessionData"
      @close="closeSessionModal"
    ></SessionDetailModal>
  </div>
</template>
<script>
import { faPlayCircle } from '@fortawesome/free-solid-svg-icons'
import Session from '~/components/Domains/TimeTable/session'
import SessionDetailModal from '~/components/Domains/TimeTable/sessionDetailModal'
import { getYoutubeLiveLink } from '~/lib/youtute-link'

export default {
  components: {
    Session,
    SessionDetailModal,
  },
  async asyncData({ $content }) {
    // const sessionDataList = await $content('/talks').fetch()
    const sessionDataList = await $content().fetch()
    return {
      sessionDataList: sessionDataList[0],
    }
  },
  data() {
    return {
      youtubeLiveUrlList: getYoutubeLiveLink(),
      day1SessionList: [],
      day2SessionList: [],
      isTablet: false,
      isDayOne: true,
      isModal: false,
      modalDisplaySessionData: {},
    }
  },
  computed: {
    faPlayCircle() {
      return faPlayCircle
    },
  },
  mounted() {
    this.day1SessionList = this.sessionDataList.body.filter(
      (sessionData) => sessionData.day === '1'
    )
    this.day2SessionList = this.sessionDataList.body.filter(
      (sessionData) => sessionData.day === '2'
    )
    const mql = window.matchMedia('(min-width: 848px)')
    this.updateMatches(mql)
    mql.addListener(this.updateMatches)

    if (this.$route.query.id !== undefined) {
      console.log(this.$route.query.id)
      const targetSession = this.getTargetSessionDataById(this.$route.query.id)
      this.openSessionModal(targetSession)
    }
  },
  methods: {
    updateMatches(mql) {
      if (mql.matches) {
        this.isTablet = false
      } else {
        this.isTablet = true
      }
    },
    getTargetSessionData(day, room, number) {
      let targetDataList
      if (day === '1') {
        targetDataList = this.day1SessionList
      } else {
        targetDataList = this.day2SessionList
      }

      for (const sessionData of targetDataList) {
        if (sessionData.room === room && sessionData.no === number) {
          return sessionData
        }
      }

      const dummyData = {
        title: '',
        talk_format: '',
        name: '',
        lang_of_talk: '',
        description: '',
        audience_python_level: '',
      }
      return dummyData
    },
    getTargetSessionDataById(id) {
      const targetSessionData = this.sessionDataList.body.filter(
        (sessionData) => sessionData.id === id
      )
      const dummyData = {
        title: '',
        talk_format: '',
        name: '',
        lang_of_talk: '',
        description: '',
        audience_python_level: '',
      }
      if (targetSessionData.length <= 0) {
        return dummyData
      } else {
        return targetSessionData[0]
      }
    },
    getSessionTime(day, index) {
      const dayIndex = day - 1
      const sessionTimeList = [
        ['11:50', '13:45', '14:50', '16:00', '16:50', '18:00'],
        ['11:50', '14:00', '14:50', '16:00', '16:30'],
      ]
      return sessionTimeList[dayIndex][index]
    },
    openSessionModal(sessionData) {
      this.isModal = true
      this.$router.push({ query: { id: sessionData.id } })
      this.modalDisplaySessionData = sessionData
    },
    closeSessionModal() {
      this.$router.replace({ query: null })
      this.isModal = false
    },
  },
}
</script>

<style scoped>
.day_width {
  width: 47%;
}

@media screen and (min-width: 375px) and (max-width: 424px) {
  .tab_font_size {
    font-size: 1.2rem;
  }
  .tab_message_area {
    margin-top: 0.7rem;
  }
  .br::before {
    content: '\A';
    white-space: pre;
  }
}

@media screen and (min-width: 425px) and (max-width: 768px) {
  .tab_font_size {
    font-size: 1.2rem;
  }

  .tab_message_area {
    margin-top: 1.5rem;
  }
}

@media screen and (min-width: 769px) {
  .timetable_container {
    display: grid;
    grid-template-columns: 0.5fr 9.5fr;
  }
}
/* .timetable_container {
  display: grid;
  grid-template-columns: 0.5fr 9.5fr;
} */
.justify_centering {
  justify-items: center;
}
.box_style1 {
  box-shadow: 0px 3px 6px #00000029;
}

.youtube_color {
  color: #282828;
}

.timetable_outer_style {
  border-radius: 1.5rem;
}
.timetable_inner_width {
  width: 95%;
}

.time_balloon_style1 {
  display: flex;
  justify-content: center;
  background-color: #3d40cb;
  align-items: center;
  /* font-size: 0.7rem; */
  /* position: absolute; */
  /* top: -2.4rem;
  left: -1.2rem; */
  color: white;
  width: 100%;
}

.time_balloon_style2 {
  display: flex;
  justify-content: center;
  background-color: #ee9d2c;
  align-items: center;
  /* font-size: 0.7rem; */
  /* position: absolute; */
  /* top: -2.4rem;
  left: -1.2rem; */
  color: white;
  width: 100%;
}

@media screen and (min-width: 768px) {
  .time_balloon_style1 {
    display: flex;
    justify-content: center;
    background-color: #3d40cb;
    align-items: center;
    font-size: 0.7rem;
    position: absolute;
    top: -2.4rem;
    left: -1.2rem;
    color: white;
    width: 2.4rem;
    height: 2.4rem;
  }
  .time_balloon_style2 {
    display: flex;
    justify-content: center;
    background-color: #ee9d2c;
    align-items: center;
    font-size: 0.7rem;
    position: absolute;
    top: -2.4rem;
    left: -1.2rem;
    color: white;
    width: 2.4rem;
    height: 2.4rem;
  }

  .grid_layout_style1 {
    grid-row: 1;
    grid-column: 1;
  }
  .grid_layout_style2 {
    grid-row: 1;
    grid-column: 2;
  }
  .grid_layout_style3 {
    grid-row: 1;
    grid-column: 3;
  }
  .grid_layout_style5 {
    grid-row: 1;
    grid-column: 5;
  }
}

@media screen and (min-width: 768px) and (max-width: 1023px) {
  .day1_line1_session_height {
    height: 274px;
  }
  .day1_line2_session_height {
    height: 322px;
  }
  .day1_line3_session_height {
    height: 298px;
  }
  .day1_line4_session_height {
    height: 298px;
  }
  .day1_line5_session_height {
    height: 346px;
  }
  .day1_line6_session_height {
    height: 322px;
  }

  .day2_line1_session_height {
    height: 298px;
  }
  .day2_line2_session_height {
    height: 370px;
  }
  .day2_line3_session_height {
    height: 346px;
  }
  .day2_line4_session_height {
    height: 274px;
  }
  .day2_line5_session_height {
    height: 226px;
  }
}

@media screen and (min-width: 1024px) and (max-width: 1439px) {
  .day1_line1_session_height {
    height: 250px;
  }
  .day1_line2_session_height {
    height: 298px;
  }
  .day1_line3_session_height {
    height: 250px;
  }
  .day1_line4_session_height {
    height: 274px;
  }
  .day1_line5_session_height {
    height: 298px;
  }
  .day1_line6_session_height {
    height: 298px;
  }

  .day2_line1_session_height {
    height: 274px;
  }
  .day2_line2_session_height {
    height: 322px;
  }
  .day2_line3_session_height {
    height: 298px;
  }
  .day2_line4_session_height {
    height: 250px;
  }
  .day2_line5_session_height {
    height: 226px;
  }
}

@media screen and (min-width: 1440px) {
  .day1_line1_session_height {
    height: 226px;
  }
  .day1_line2_session_height {
    height: 226px;
  }
  .day1_line3_session_height {
    height: 226px;
  }
  .day1_line4_session_height {
    height: 250px;
  }
  .day1_line5_session_height {
    height: 250px;
  }
  .day1_line6_session_height {
    height: 250px;
  }

  .day2_line1_session_height {
    height: 226px;
  }
  .day2_line2_session_height {
    height: 250px;
  }
  .day2_line3_session_height {
    height: 250px;
  }
  .day2_line4_session_height {
    height: 202px;
  }
  .day2_line5_session_height {
    height: 202px;
  }
}
</style>

<i18n>
{
  "en": {
    "OnAir": "On Air"
  },
  "ja": {
    "OnAir": "放送中のLive"
  }
}
</i18n>
