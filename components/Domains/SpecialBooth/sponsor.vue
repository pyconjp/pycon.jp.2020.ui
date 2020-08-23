<template>
  <div class="">
    <article class="relative">
      <div
        class="relative z-10 flex flex-col items-center justify-center bg-white border-8 border-solid rounded-xl"
        :style="{ 'border-color': color }"
      >
        <div class="mx-6 my-4">
          <div class="flex flex-col items-center justify-center mb-8">
            <slot name="image"></slot>
          </div>
          <div class="flex flex-row items-center">
            <a target="_blank" rel="noopener noreferrer" :href="url">
              <h3 class="mb-2 text-xl sm:text-2xl lg:text-2xl">
                <slot name="companyName">
                  ダミーの会社名です
                </slot>
              </h3>
            </a>
            <a target="_blank" rel="noopener noreferrer" :href="url"
              ><i class="mt-1 ml-2 text-4xl material-icons">link</i>
            </a>
          </div>
        </div>
      </div>
      <div
        class="absolute top-0 w-20 h-20 -mt-6 -ml-10 border-4 border-solid rounded-card-head"
        :class="[
          sponsorType === 'platinum' ? 'ml-0 left-1/2' : 'ml-10 left-3/4',
        ]"
        :style="{ 'border-color': color, 'background-color': color }"
      >
        <div class="relative">
          <div class="absolute w-2 h-2 mt-2 ml-6 bg-white rounded-full"></div>
          <div class="absolute w-2 h-2 mt-2 ml-10 bg-white rounded-full"></div>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  components: {},
  props: {
    sponsorType: {
      type: String,
      default: 'platinum',
    },
    url: {
      type: String,
      default: '',
    },
    recruitExist: {
      type: Boolean,
      default: false,
    },
    color: {
      type: String,
      default: '#71A4F1',
    },
  },
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

.platinum-button-style {
  background-color: white;
}
.platinum-button-style:hover {
  background-color: #71a4f1;
  color: white;
}
.platinum-circle-style {
  background-color: #71a4f1;
}
.platinum-button-style:hover > .platinum-circle-style {
  background-color: white;
}

.gold-button-style {
  background-color: white;
}
.gold-button-style:hover {
  background-color: #e3ab4a;
  color: white;
}
.gold-circle-style {
  background-color: #e3ab4a;
}
.gold-button-style:hover > .gold-circle-style {
  background-color: white;
}
</style>
