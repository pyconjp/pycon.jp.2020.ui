<template>
  <div
    class="flex flex-col max-w-screen-xl mx-auto tb:items-center tb:justify-between tb:flex-row tb:my-4 xl:w-3/4"
  >
    <div class="flex flex-row items-center justify-between py-4">
      <n-link :to="localePath('/')">
        <img :src="require('~/assets/img/header-logo.png')" class="w-40" />
      </n-link>
      <hamburger
        :is-drawer-open="isDrawerOpen"
        class="-mr-1"
        @toggleDrawer="isDrawerOpen = !isDrawerOpen"
      />
    </div>
    <transition
      name="nav"
      enter-active-class="transition-all duration-200 ease-out"
      leave-active-class="transition-all duration-150 ease-in"
      @enter="enter"
      @after-enter="afterEnter"
      @leave="leave"
      @after-leave="afterLeave"
    >
      <nav
        v-show="isDrawerOpen || !isMobile"
        id="navigation"
        class="flex flex-col pb-4 md:pb-0 md:justify-end tb:flex-row"
      >
        <div
          v-for="page in filteredPages"
          :key="page.path"
          class="flex flex-col pb-4 md:pb-0 md:justify-end tb:flex-row"
        >
          <header-link
            v-if="page.path !== undefined"
            :path="page.path"
            :exact="page.path === '/' ? true : false"
            class="mt-2 mr-0 md:mr-2 md:mt-0"
          >
            {{ page.title }}
          </header-link>
          <dropdown
            v-else-if="!isMobile"
            :is-dropdown-open="isEventListDropdownOpen"
            emit-event="toggleEventListDropdown"
            @toggleEventListDropdown="
              isEventListDropdownOpen = !isEventListDropdownOpen
            "
          >
            {{ $t('pages.event-list.title') }}
            <template #menu>
              <event-list
                v-if="isEventListDropdownOpen"
                emit-event="toggleEventListDropdown"
                @toggleEventListDropdown="
                  isEventListDropdownOpen = !isEventListDropdownOpen
                "
              />
            </template>
          </dropdown>
          <div v-else>
            <h5 class="block px-4 py-2 mt-2 text-sm bg-transparent md:mt-0">
              {{ $t('pages.event-list.title') }}
            </h5>
            <n-link
              v-for="event in $t('pages.event-list.content-list')"
              :key="event.title"
              class="block px-4 py-2 mt-2 ml-10 text-sm bg-transparent md:mt-0"
              :to="localePath(event.path)"
            >
              {{ event.title }}
            </n-link>
          </div>
        </div>

        <locales-list />
      </nav>
    </transition>
  </div>
</template>

<script>
import Hamburger from '~/components/Domains/Header/Hamburger'
import Dropdown from '~/components/Domains/Header/Dropdown'
import EventList from '~/components/Domains/Header/EventList'
import LocalesList from '~/components/Domains/Header/LocalesList'
import HeaderLink from '~/components/Domains/Header/HeaderLink'

export default {
  components: {
    Hamburger,
    Dropdown,
    EventList,
    LocalesList,
    HeaderLink,
  },
  data() {
    return {
      isDrawerOpen: false,
      isDropdownOpen: false,
      isEventListDropdownOpen: false,
      isMobile: true,
    }
  },
  computed: {
    filteredPages() {
      Object.filter = (obj, predicate) =>
        Object.fromEntries(Object.entries(obj).filter(predicate))
      return Object.filter(
        this.$i18n.t('pages'),
        ([_key, value]) => value.path !== '/'
      )
    },
  },
  mounted() {
    this.$router.beforeEach((_to, _from, next) => {
      this.isDrawerOpen = false
      this.isDropdownOpen = false
      next()
    })
    const mql = window.matchMedia('(min-width: 848px)')
    this.updateMatches(mql)
    mql.addListener(this.updateMatches)
  },
  methods: {
    updateMatches(mql) {
      if (mql.matches) {
        this.isMobile = false
      } else {
        this.isMobile = true
      }
    },
    nextFrame(fn) {
      window.requestAnimationFrame(() => window.requestAnimationFrame(fn))
    },
    enter(el) {
      el.style.overflow = 'hidden'
      el.style.height = '0'

      this.nextFrame(() => {
        el.style.height = `${el.scrollHeight}px`
      })
    },
    leave(el) {
      el.style.overflow = 'hidden'
      el.style.height = `${el.scrollHeight}px`

      this.nextFrame(() => {
        el.style.height = '0'
      })
    },
    afterEnter(el) {
      el.style.height = ''
      el.style.overflow = ''
    },
    afterLeave(el) {
      el.style.height = ''
      el.style.overflow = ''
    },
  },
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
