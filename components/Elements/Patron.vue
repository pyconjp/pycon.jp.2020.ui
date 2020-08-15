<template>
  <div class="p-4 shadow-lg rounded-xl">
    <a
      :href="connpassLink"
      class="flex items-center justify-center"
      target="_blank"
      rel="noopener noreferrer"
    >
      <img
        :src="iconImageLink"
        alt="Patron Icon"
        class="object-center w-12 h-12 rounded-full"
      />
      <p class="ml-2 text-lg font-semibold text-py-black">{{ name }}</p>
    </a>
  </div>
</template>

<script>
export default {
  props: {
    connpassLink: {
      type: String,
      default: '',
    },
    name: {
      type: String,
      default: '',
    },
    iconImageLink: {
      type: String,
      default: '',
    },
  },
}
</script>

<style></style>
