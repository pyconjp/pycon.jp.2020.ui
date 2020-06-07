<template>
  <div
    v-if="error.statusCode === 404"
    class="flex flex-col items-center justify-center flex-1"
  >
    <h1 class="flex flex-col w-full">
      <span
        class="mb-8 text-4xl italic font-black leading-normal tracking-widest text-center md:text-5xl lg:text-6xl"
      >
        404
      </span>
      <span
        class="font-medium leading-normal tracking-wider text-center sm:text-lg md:text-2xl lg:text-3xl"
      >
        {{ $t('error.404') }}
      </span>
    </h1>
    <n-link
      :to="localePath('/')"
      class="mt-2 text-xl leading-normal tracking-tight text-center text-blue-600 transition-colors duration-100 hover:text-blue-800 md:text-2xl xl:text-3xl"
    >
      {{ $t('error.back') }}
    </n-link>
  </div>
  <div v-else class="flex flex-col items-center justify-center flex-1">
    <h1 class="flex flex-col w-full">
      <span
        class="mb-8 text-4xl italic font-black leading-normal tracking-widest text-center md:text-5xl lg:text-6xl"
      >
        {{ error.statusCode }}
      </span>
      <span
        class="font-medium leading-normal tracking-wider text-center sm:text-lg md:text-2xl lg:text-3xl"
      >
        {{ $t('error.else') }}
      </span>
    </h1>
    <n-link
      :to="localePath('/')"
      class="mt-2 text-xl leading-normal tracking-tight text-center text-blue-600 transition-colors duration-100 hover:text-blue-800 md:text-2xl xl:text-3xl"
    >
      {{ $t('error.back') }}
    </n-link>
  </div>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      required: true,
    },
  },
}
</script>
