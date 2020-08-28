<template>
  <div
    class="absolute right-0 w-full mt-2 origin-top-right rounded-md shadow-lg md:w-48"
  >
    <div class="px-2 py-2 bg-white rounded-md shadow">
      <div
        v-for="event in $t('pages.event-list.content-list')"
        :key="event.title"
      >
        <n-link
          v-if="judgeNuxtPath(event.path)"
          class="block px-4 py-2 mt-2 text-sm font-semibold transition-colors duration-200 bg-transparent rounded-lg px- md:mt-0 focus:text-gray-900 hover:text-gray-600 focus:bg-gray-200 focus:outline-none"
          :to="localePath(event.path)"
          @click.native.stop="$emit(emitEvent)"
        >
          {{ event.title }}
        </n-link>
        <a
          v-else
          :href="event.path"
          class="block px-4 py-2 mt-2 text-sm font-semibold transition-colors duration-200 bg-transparent rounded-lg px- md:mt-0 focus:text-gray-900 hover:text-gray-600 focus:bg-gray-200 focus:outline-none"
          target="_blank"
          rel="noopener noreferrer"
          >{{ event.title }}</a
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    emitEvent: {
      type: String,
      default: '',
    },
  },
  computed: {},
  methods: {
    judgeNuxtPath(path) {
      return !/^https?:\/\//.test(path)
    },
  },
}
</script>
