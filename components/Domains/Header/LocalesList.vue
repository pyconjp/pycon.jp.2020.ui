<template>
  <div>
    <n-link
      v-for="locale in availableLocales"
      :key="locale.code"
      class="flex items-center px-4 py-2 mt-2 transition-colors duration-200 bg-transparent border-2 rounded-lg border-py-black px- md:mt-0 hover:text-gray-900 focus:text-gray-900 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
      :to="switchLocalePath(locale.code)"
    >
      <i class="mr-2 text-gray-700 material-icons">translate</i>
      {{ locale.name }}
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
