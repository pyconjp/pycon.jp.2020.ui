<template>
  <transition
    name="fade"
    v-bind="$attrs"
    enter-active-class="transition duration-100 ease-out"
    leave-active-class="transition duration-75 ease-in"
    enter-class="transform scale-95 opacity-0"
    leave-class="transform scale-100 opacity-100"
    enter-to-class="transform scale-100 opacity-100"
    leave-to-class="transform scale-95 opacity-0"
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
