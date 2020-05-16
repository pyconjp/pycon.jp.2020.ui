<template>
  <div class="relative">
    <div
      class="relative bg-white z-10 border-solid border-4 rounded-xl flex flex-col justify-center items-center"
      :class="[`border-${mainColor}-400`, `bg-${mainColor}-100`]"
    >
      <div class=" w-3/4">
        <div class="flex justify-center mt-8">
          <div class="w-24 h-24 bg-gray-400 rounded-full"></div>
        </div>
        <h4 class="text-xl md:text-3xl">
          <slot name="name">Taro Yamada</slot>
        </h4>
        <p class="text-base md:text-xl">
          <slot name="date">
            8/23
          </slot>
        </p>
        <h5 class="text-base md:text-xl mb-8">
          <slot name="description"
            >トークの説明トークの説明トークの説明トークの説明トークの説明トークの説明</slot
          >
        </h5>
      </div>
    </div>
    <div
      class="absolute w-20 h-20 border-solid border-4 rounded-card-head  top-0 -mt-6 -ml-10"
      :class="[
        mainColor,
        `border-${mainColor}-400`,
        `bg-${mainColor}-400`,
        talkType === 'talk' ? 'ml-0' : 'ml-10',
        talkType === 'talk' ? 'left-1/2' : 'left-3/4'
      ]"
    >
      <div class="relative">
        <div class="absolute w-2 h-2 bg-white rounded-full mt-2 ml-6"></div>
        <div class="absolute w-2 h-2 bg-white rounded-full mt-2 ml-10"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    talkType: {
      type: String,
      default: 'talk'
    },
    mainColor: {
      type: String,
      default: 'blue'
    }
  }
}
</script>

<style scoped></style>
