<template>
  <transition
    name="fade"
    v-bind="$attrs"
    :enter-active-class="`transition ease-out duration-${enter}`"
    :leave-active-class="`transition ease-in duration-${leave}`"
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
  inheritAttrs: false,
  props: {
    enter: {
      validator(value) {
        // The value must match one of these strings
        return [
          '75',
          '100',
          '150',
          '200',
          '300',
          '500',
          '700',
          '1000'
        ].includes(value)
      },
      default: '100'
    },
    leave: {
      validator(value) {
        // The value must match one of these strings
        return [
          '75',
          '100',
          '150',
          '200',
          '300',
          '500',
          '700',
          '1000'
        ].includes(value)
      },
      default: '75'
    }
  }
}
</script>
