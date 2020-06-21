<template>
  <div>
    <n-link
      v-for="locale in availableLocales"
      :key="locale.code"
      class="flex items-center px-4 py-2 mt-2 transition-colors duration-200 bg-transparent border-2 rounded-lg border-py-black md:mt-0 hover:bg-py-black group"
      :to="switchLocalePath(locale.code)"
    >
      <i class="mr-2 material-icons group-hover:text-white">translate</i>
      <span class="group-hover:text-white">{{ locale.name }}</span>
    </n-link>
  </div>
</template>

<script>
export default {
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter((i) => i.code !== this.$i18n.locale)
    },
  },
}
</script>
