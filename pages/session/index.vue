<template>
  <div>
    {{ sessions }}
  </div>
</template>
<script>
export default {
  asyncData() {
    const sessions = require('~/mocks/session.json')
    return { sessions }
  },
}
</script>

<style></style>
