<template>
   <div class="header">
      <router-link
         v-for="link, i in links"
         class="header-link"
         tag="a"
         :to="link.url"
         :key="`headerLink_${i}`">{{link.title}}</router-link>
   </div>
</template>

<script lang="ts">
   import { Component, Prop, Vue } from 'vue-property-decorator';

   @Component
   export default class HeaderMenu extends Vue {
      public links: Array<{ url: string, title: string }> = [
         { url: '/page1', title: 'page 1' },
         { url: '/page2', title: 'page 2' },
      ];
   }
</script>

<style scoped>
   .header {
      background-color: #1A9DDB;
      text-align: center;
      padding: 12px;
      color: white;
   }
   .header-link {
      padding: 12px;
      color: white;
   }
</style>
