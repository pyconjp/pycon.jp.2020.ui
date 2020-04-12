<template>
  <transition
    name="fade"
    v-bind="$attrs"
    enter-active-class="transition ease-out duration-100"
    leave-active-class="transition ease-in duration-75"
    enter-class="opacity-0 transform scale-95"
    leave-class="opacity-100 transform scale-100"
    enter-to-class="opacity-100 transform scale-100"
    leave-to-class="opacity-0 transform scale-95"
    v-on="$listeners"
  >
    <slot></slot>
  </transition>
</template>

<script>
export default {
  inheritAttrs: false
}
</script>
