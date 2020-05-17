<template>
  <article class="relative">
    <div
      class="relative z-10 flex flex-col items-center justify-center bg-white border-4 border-solid rounded-xl"
      :class="[`border-${mainColor}-400`, `bg-${mainColor}-100`]"
    >
      <div class="mx-6 my-4">
        <div class="flex flex-col items-center justify-center my-8">
          <div class="w-24 h-24 bg-gray-400 rounded-full"></div>
          <h2 class="text-xl md:text-2xl">
            <slot name="name">Taro Yamada</slot>
          </h2>
        </div>
        <p class="text-base md:text-xl">
          <slot name="date">
            8/23
          </slot>
        </p>

        <p class="mb-8 text-sm md:text-base">
          <slot name="description"
            >トークの説明トークの説明トークの説明トークの説明トークの説明トークの説明</slot
          >
        </p>
      </div>
    </div>
    <div
      class="absolute top-0 w-20 h-20 -mt-6 -ml-10 border-4 border-solid rounded-card-head"
      :class="[
        `border-${mainColor}-400`,
        `bg-${mainColor}-400`,
        talkType === 'talk' ? 'ml-0 left-1/2' : 'ml-10 left-3/4'
      ]"
    >
      <div class="relative">
        <div class="absolute w-2 h-2 mt-2 ml-6 bg-white rounded-full"></div>
        <div class="absolute w-2 h-2 mt-2 ml-10 bg-white rounded-full"></div>
      </div>
    </div>
  </article>
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
