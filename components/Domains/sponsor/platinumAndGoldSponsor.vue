<template>
  <div class="w-3/4">
    <div class="w-full">
      <p class="text-2xl">Pythonダミー株式会社</p>
      <p class="dummy-logo bg-blue-200">Logo</p>
      <div class="flex justify-center relative z-10">
        <div class="toggle-button-bg md:w-1/2 w-full relative">
          <div
            class="w-1/2 text-center"
            :class="{ 'active-toggle-button': isCompanyInformation }"
            @click="
              isCompanyInformation = true
              isRecruitInformation = false
            "
          >
            <p class="z-10">会社概要</p>
          </div>
          <div
            class="active-toggle-button-bg"
            :class="{ 'move-effect-toggle-button': isRecruitInformation }"
          ></div>
          <div
            class="w-1/2 text-center"
            :class="{ 'active-toggle-button': isRecruitInformation }"
            @click="
              isCompanyInformation = false
              isRecruitInformation = true
            "
          >
            <p class="z-10">採用情報</p>
          </div>
        </div>
      </div>

      <div class="flex flex-col items-center">
        <div class="border w-full pt-4 border-gray-400 rounded-lg">
          <div class="p-3">
            <div v-if="isCompanyInformation" class="mt-6">
              <p>
                弊社はPythonコミュニティの繁栄を目指して活動しています。
                たくさんの人が楽しみながらPythonを学ぶことができるように日々活動しています。
              </p>
            </div>
            <div v-if="isRecruitInformation" class="mt-6">
              <p>
                Python愛にあふれる人を募集しています。
                経験者、初心者を問わず、何事にも積極的にチャレンジする、失敗を恐れずに前向きな姿勢で取り組む人を
                歓迎します。
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  components: {},
  data() {
    return { isCompanyInformation: true, isRecruitInformation: false }
  }
})
</script>

<style scoped>
.dummy-logo {
  width: 100%;
  height: 300px;
}

.toggle-button-bg {
  border-radius: 200px;
  display: flex;
  align-items: center;
  background-color: #edf2f7;
  height: 3rem;
  cursor: pointer;
  color: rgb(159, 157, 163);
  margin-top: 1rem;
  margin-bottom: -1.5rem;
}

.active-toggle-button {
  box-shadow: 0 16px 27px rgba(83, 14, 223, 0.1);
  border-radius: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50%;
  height: 100%;
  text-align: center;
  color: rgb(83, 14, 223);
  transition: color 0.25s cubic-bezier(0.65, 0.05, 0.36, 1);
}
.active-toggle-button-bg {
  border-radius: 200px;
  width: 50%;
  height: 100%;
  position: absolute;
  background-color: white;
  transition: all 0.25s cubic-bezier(0.65, 0.05, 0.36, 1);
}

.move-effect-toggle-button {
  transform: translateX(100%);
}
</style>
