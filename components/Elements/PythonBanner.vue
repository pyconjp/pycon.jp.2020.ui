<template>
  <div
    class="relative h-auto shadow-lg m-screen"
    :class="[
      direction == 'left' ? 'ml-auto' : 'mr-auto',
      size === 'small' ? 'w-50vw md:w-35vw' : 'w-70vw',
    ]"
    :style="{ 'background-color': backGroundColor }"
  >
    <div
      class="absolute inset-y-0 flex flex-col items-center justify-center h-full overflow-hidden transform"
      :class="[
        direction === 'left'
          ? 'left-0 shadow-left rounded-l-xl'
          : 'right-0 shadow-right rounded-r-xl',
        size === 'small' ? 'w-12' : 'w-20 md:w-32',
        direction === 'left' && size === 'small'
          ? '-translate-x-12'
          : direction === 'right' && size === 'small'
          ? 'translate-x-12'
          : direction === 'left' && size === 'big'
          ? '-translate-x-20'
          : 'translate-x-20',
      ]"
      :style="{ 'background-color': backGroundColor }"
    >
      <template v-if="size === 'small'">
        <div class="w-4 h-4 mb-4 bg-white rounded-full"></div>
        <div class="w-full h-4 bg-white"></div>
      </template>
      <template v-if="size === 'big'">
        <div class="w-8 h-8 mb-8 bg-white rounded-full"></div>
        <div class="w-full h-8 bg-white"></div>
      </template>
    </div>

    <div
      class="flex flex-col px-4 py-8 md:px-16"
      :class="direction == 'left' ? 'items-start' : 'items-end'"
    >
      <template v-if="size === 'big'">
        <h3
          v-show="hasTitle === true"
          class="inline mb-6 text-xl text-white sm:text-2xl md:text-4xl"
        >
          <slot name="title">
            企業スポンサー様募集中
          </slot>
        </h3>
        <p class="flex flex-col items-center text-white">
          <slot name="content">
            <span class="text-lg sm:text-xl md:text-2xl">
              PyCon JP 2020を応援して下さるスポンサー様を募集しております
            </span>
          </slot>
          <slot name="button">
            <button
              class="flex items-center px-8 py-6 mt-4 bg-white rounded-full shadow text-py-black"
            >
              <p class="w-6 h-6 mr-4 rounded-full bg-py-blue-dark" />
              スポンサーに申し込む
            </button>
          </slot>
        </p>
      </template>
      <template v-else>
        <h3 class="inline text-lg text-white sm:text-xl md:text-3xl">
          <slot name="title">
            企業スポンサー様募集中
          </slot>
        </h3>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    direction: {
      validator(value) {
        // The value must match one of these strings
        return ['left', 'right'].includes(value)
      },
      default: 'left',
    },
    backGroundColor: {
      type: String,
      default: '#3D40CB',
    },
    size: {
      validator(value) {
        // The value must match one of these strings
        return ['small', 'big'].includes(value)
      },
      default: 'small',
    },
    hasTitle: {
      type: Boolean,
      default: true,
    },
  },
}
</script>

<style scoped></style>
