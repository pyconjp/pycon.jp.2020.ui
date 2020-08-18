<template>
  <div
    class="flex items-start justify-center w-full p-2 cursor-pointer md:h-full outer_style hover:bg-py-blue-light"
  >
    <div class="w-11/12 mt-2">
      <div class="flex items-center justify-center">
        <div
          class="w-1/6 font-bold text-center border rounded-l-lg border-py-blue-dark text-py-blue-dark"
        >
          {{ sessionLanguage }}
        </div>
        <div
          class="w-5/6 font-bold text-center text-green-700 truncate border border-green-700 rounded-r-lg"
        >
          {{
            sessionData.audience_python_level
              ? sessionData.audience_python_level
              : 'All'
          }}
        </div>
      </div>
      <p class="mt-4">{{ sessionData.title }}</p>
      <p class="mt-4 text-gray-600">{{ sessionData.name }}</p>
      <p class="">
        {{ sessionData.talk_format ? sessionData.talk_format : 'All' }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    sessionData: {
      type: Object,
      default() {
        return {
          title: '',
          talk_format: '',
          name: '',
          lang_of_talk: '',
          description: '',
          audience_python_level: '',
        }
      },
    },
  },
  computed: {
    sessionLanguage() {
      if (this.sessionData.lang_of_talk === 'Japanese') {
        return 'JA'
      } else {
        return 'EN'
      }
    },
  },
}
</script>

<style scoped>
.outer_style {
  box-shadow: 0px 3px 6px #00000029;
  border-radius: 1rem;
}
</style>
