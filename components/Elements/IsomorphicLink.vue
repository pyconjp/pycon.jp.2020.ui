<template>
  <component
    :is="isInternalLink(path) ? 'nuxt-link' : 'a'"
    v-bind="$attrs"
    :to="isInternalLink(path) ? localePath(path) : ''"
    :href="isInternalLink(path) ? '' : path"
    :target="isInternalLink(path) ? '' : '_blank'"
    :rel="isInternalLink(path) ? '' : 'noopener noreferrer'"
    v-on="$listeners"
  >
    <slot></slot>
  </component>
</template>

<script>
export default {
  inheritAttrs: false,
  props: {
    path: { type: String, required: true }
  },
  methods: {
    isInternalLink(path) {
      return !/^https?:\/\//.test(path)
    }
  }
}
</script>
