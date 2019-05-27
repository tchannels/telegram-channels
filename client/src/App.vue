<template>
  <div id="app">
    Hello {{ text }}
    <router-view/>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      text: 'world',
    };
  },
};
</script>
