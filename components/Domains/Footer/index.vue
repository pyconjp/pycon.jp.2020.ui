<template>
  <div class="flex flex-col items-center w-full py-8">
    <section
      class="flex flex-col items-center justify-center px-4 pt-8 pb-12 m-screen"
    >
      <h2 class="inline mb-12 text-4xl font-bold md:text-6xl">
        Contact
      </h2>

      <p class="text-center md:text-xl">
        事前にFAQをご確認いただけますようにお願いします。 <br />
        ボランティアによる運営ですので、回答には1週間程度を要します。 <br />
        何卒お待ちいただけますようにお願いします。 <br />
      </p>
      <a
        href="mailto:pyconjp@pycon.jp"
        class="mt-10 text-2xl font-semibold hover:underline"
      >
        <i class="text-2xl align-middle material-icons">email</i>
        <span>pyconjp@pycon.jp</span>
      </a>
    </section>

    <div
      class="flex flex-col items-center justify-between w-full max-w-screen-xl mx-auto md:items-center md:flex-row"
    >
      <h2
        class="mb-8 text-xl font-semibold tracking-widest text-gray-900 uppercase md:mb-0"
      >
        <a
          href="https://www.pycon.jp"
          target="_blank"
          rel="noopener noreferrer"
        >
          <img
            :src="require('~/assets/img/pycon-conference-japan.png')"
            class="w-40"
          />
        </a>
      </h2>
      <div class="flex flex-col items-center justify-end sm:items-start">
        <h3 class="mb-2">主催: 一般社団法人PyCon JP Association</h3>
        <h3 class="text-center">
          PyCon JP 2020 in Tokyo is a production of the
          <span> </span>
          <a
            class="text-blue-400 transition-colors duration-100 hover:text-blue-600"
            href="https://www.pycon.jp/"
            target="_blank"
            rel="noopener noreferrer"
          >
            PyCon JP Association
          </a>
        </h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style></style>
