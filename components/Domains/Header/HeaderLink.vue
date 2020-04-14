<template>
  <isomorphic-link
    v-bind="$attrs"
    class="px-4 py-2 text-sm font-semibold transition-colors duration-200 bg-transparent rounded-lg hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
    active-class="text-gray-900 bg-gray-200"
    :path="path"
    v-on="$listeners"
  >
    <slot></slot>
  </isomorphic-link>
</template>

<script>
import IsomorphicLink from '~/components/Elements/IsomorphicLink'
export default {
  components: { IsomorphicLink },
  inheritAttrs: false,
  props: {
    path: { type: String, required: true }
  }
}
</script>

<style></style>
