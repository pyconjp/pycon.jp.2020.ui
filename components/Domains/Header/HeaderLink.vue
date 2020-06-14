<template>
  <isomorphic-link
    v-bind="$attrs"
    class="px-4 py-2 transition-colors duration-200 bg-transparent hover:text-gray-900 focus:outline-none"
    active-class="text-gray-900 border-b-4 border-py-black"
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
    path: { type: String, required: true },
  },
}
</script>

<style></style>
