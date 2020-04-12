<template>
  <div class="w-full text-gray-700 bg-white">
    <div
      class="flex flex-col max-w-screen-xl px-4 mx-auto md:items-center md:justify-between md:flex-row md:px-6 lg:px-8"
    >
      <div class="flex flex-row items-center justify-between p-4">
        <n-link
          :to="localePath('/')"
          class="text-lg font-semibold tracking-widest text-gray-900 uppercase rounded-lg focus:outline-none focus:shadow-outline"
        >
          Pycon JP 2020
        </n-link>
        <hamburger
          :is-drawer-open="isDrawerOpen"
          @toggleDrawer="isDrawerOpen = !isDrawerOpen"
        />
      </div>
      <nav
        :class="{ flex: isDrawerOpen, hidden: !isDrawerOpen }"
        class="flex-col flex-grow pb-4 md:pb-0 md:flex md:justify-end md:flex-row"
      >
        <n-link
          class="px-4 py-2 mt-2 text-sm font-semibold transition-colors duration-200 rounded-lg md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
          exact
          active-class="text-gray-900 bg-gray-200"
          :to="localePath('/')"
        >
          {{ $t('about') }}
        </n-link>
        <a
          class="px-4 py-2 mt-2 text-sm font-semibold transition-colors duration-200 bg-transparent rounded-lg md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
          href="https://pyconjp.blogspot.com/search/label/pyconjp2020"
          target="_blank"
          rel="noopener noreferrer"
        >
          {{ $t('news') }}
        </a>
        <n-link
          class="px-4 py-2 mt-2 text-sm font-semibold transition-colors duration-200 bg-transparent rounded-lg md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
          active-class="text-gray-900 bg-gray-200"
          :to="localePath('/sponsors')"
        >
          {{ $t('sponsor') }}
        </n-link>
        <n-link
          class="px-4 py-2 mt-2 text-sm font-semibold transition-colors duration-200 bg-transparent rounded-lg md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
          active-class="text-gray-900 bg-gray-200"
          :to="localePath('/staff')"
        >
          {{ $t('staff') }}
        </n-link>
        <dropdown
          :is-dropdown-open="isDropdownOpen"
          @toggleDropdown="isDropdownOpen = !isDropdownOpen"
        >
          <fade-transition>
            <DropdownMenu v-if="isDropdownOpen" />
          </fade-transition>
        </dropdown>
      </nav>
    </div>
  </div>
</template>

<script>
import Hamburger from '~/components/Domains/Header/Hamburger'
import Dropdown from '~/components/Domains/Header/Dropdown'
import DropdownMenu from '~/components/Domains/Header/DropdownMenu'
import FadeTransition from '~/components/Elements/FadeTransition'

export default {
  components: {
    Hamburger,
    Dropdown,
    DropdownMenu,
    FadeTransition
  },
  data() {
    return {
      isDrawerOpen: false,
      isDropdownOpen: false
    }
  },
  methods: {
    toggleTab(toggle) {
      this.isToggled = toggle
    }
  }
}
</script>

<style scoped>
.border-bottom-blank {
  border-width: 2px;
  border-color: #e2e8f0 #e2e8f0 white #e2e8f0;
}

.border-top-blank {
  border-width: 2px;
  border-color: white white #e2e8f0 white;
}
</style>
