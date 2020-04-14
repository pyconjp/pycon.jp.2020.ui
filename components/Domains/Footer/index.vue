<template>
  <div
    class="flex flex-col items-center justify-between w-full max-w-screen-xl px-8 mx-auto my-8 md:px-12 md:items-center md:flex-row"
  >
    <h2
      class="mb-8 text-xl font-semibold tracking-widest text-gray-900 uppercase md:mb-0"
    >
      <n-link :to="localePath('/')">
        Pycon JP 2020
      </n-link>
    </h2>
    <div class="flex flex-col items-start justify-end">
      <h3 class="mb-2">主催: 一般社団法人PyCon JP</h3>
      <h3>
        PyCon JP 2020 in Tokyo is a production of the
        <a
          class="text-blue-400 transition-colors duration-100 hover:text-blue-600"
          href="https://www.pycon.jp/"
          target="_blank"
          rel="noopener noreferrer"
        >
          PyCon JP Committee
        </a>
      </h3>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style></style>
