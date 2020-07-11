<template>
  <article class="relative">
    <div
      class="relative z-10 flex flex-col items-center justify-center bg-white border-4 border-solid rounded-xl"
      :style="{ 'border-color': '#3D40CB' }"
    >
      <div class="mx-6 my-4">
        <div class="flex flex-col items-center justify-center mb-8">
          <slot name="image"></slot>
        </div>
        <h2 class="text-xl font-bold md:text-2xl">
          <slot name="name"></slot>
        </h2>
        <p class="mb-4 text-sm md:text-base">
          <slot name="date"> </slot>
        </p>

        <p class="mb-8 text-sm md:text-base">
          <slot name="description"></slot>
        </p>
      </div>
    </div>
    <div
      class="absolute top-0 w-20 h-20 -mt-6 -ml-10 border-4 border-solid rounded-card-head"
      :class="[talkType === 'talk' ? 'ml-0 left-1/2' : 'ml-10 left-3/4']"
      :style="{ 'border-color': '#3D40CB', 'background-color': '#3D40CB' }"
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
      default: 'talk',
    },
    mainColor: {
      type: String,
      default: 'blue',
    },
  },
}
</script>

<style scoped></style>
