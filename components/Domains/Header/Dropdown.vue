<template>
  <div class="relative">
    <button
      class="flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg md:w-auto md:inline md:mt-0 md:ml-4 transition-colors duration-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
      @click="$emit('toggleDropdown')"
    >
      <span>Language</span>
      <svg
        fill="currentColor"
        viewBox="0 0 20 20"
        :class="{ 'rotate-180': isDropdownOpen, 'rotate-0': !isDropdownOpen }"
        class="inline w-4 h-4 mt-1 ml-1 transition-transform duration-200 transform md:-mt-1"
      >
        <path
          fill-rule="evenodd"
          d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
          clip-rule="evenodd"
        ></path>
      </svg>
    </button>
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: {
    isDropdownOpen: {
      type: Boolean,
      defaulte: false
    }
  }
}
</script>

<style></style>
