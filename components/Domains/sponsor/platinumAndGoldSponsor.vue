<template>
  <div class="w-full">
    <h3 class="flex items-center mb-4 text-xl sm:text-2xl lg:text-3xl">
      <slot name="companyName">
        ダミーの会社名です
      </slot>
      <i class="mt-1 ml-2 material-icons">launch</i>
    </h3>
    <p class="bg-blue-200 dummy-logo">Logo</p>
    <div class="relative flex justify-center">
      <div
        class="relative w-full toggle-button-bg sm:w-10/12 md:w-9/12 lg:w-8/12"
      >
        <h4
          class="z-10 w-1/2 text-center"
          :class="{ 'active-toggle-button': isCompanyInformation }"
          @click="
            isCompanyInformation = true
            isRecruitInformation = false
          "
        >
          会社概要
        </h4>
        <div
          class="active-toggle-button-bg"
          :class="{ 'move-effect-toggle-button': isRecruitInformation }"
        ></div>
        <h4
          class="z-10 w-1/2 text-center"
          :class="{ 'active-toggle-button': isRecruitInformation }"
          @click="
            isCompanyInformation = false
            isRecruitInformation = true
          "
        >
          採用情報
        </h4>
      </div>
    </div>

    <div class="flex flex-col items-center">
      <div class="w-full pt-4 border border-gray-400 rounded-lg">
        <p class="px-8 py-6 mt-2">
          <slot v-if="isCompanyInformation" name="companyInformation">
            ダミーの会社情報です
          </slot>
          <slot v-if="isRecruitInformation" name="recruitInformation">
            ダミーの採用情報です
          </slot>
        </p>
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
