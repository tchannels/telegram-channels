<template>
   <header class="header">
      <div class="header-wrapper">
         <router-link class="header-logo" tag="a" to="/">Telegram channels</router-link>
         <div class="header-menu">
            <router-link
               v-for="(link, i) in links"
               class="header-link"
               tag="a"
               :to="link.url"
               :key="`headerLink_${i}`">{{link.title}}</router-link>
         </div>
         <div class="header-search">
            <input type="text" placeholder="Search…" class="header-searchInput" />
         </div>
      </div>
   </header>
</template>

<script lang="ts">
   import { Component, Vue } from 'vue-property-decorator';

   @Component
   export default class HeaderMenu extends Vue {
      public links: Array<{ url: string, title: string }> = [
         { url: '/page1', title: 'Channels' },
         { url: '/page2', title: 'Bots' },
      ];
   }
</script>

<style lang="less" scoped>
   .header {
      display: flex;
      flex-direction: column;
      align-items: center;
      background-color: #05C3FF;
      color: #fff;
      &-wrapper {
         display: flex;
         width: 1280px;
         justify-content: space-between;
         flex-direction: row;
      }
      &-logo {
         display: flex;
         flex-direction: column;
         justify-content: center;
         align-content: center;
         flex-shrink: 0;
         font-weight: bold;
         text-transform: uppercase;
         font-size: 20px;
         color: #fff;
         text-decoration: none;
         &:hover {
            color: #fdeeee;
         }
      }
      &-menu {
         display: flex;
         flex-direction: row;
         justify-content: space-between;
      }
      &-link {
         padding: 20px;
         text-decoration: none;
         color: #fff;
         &:hover {
            text-decoration: underline;
            background-color: #09b3e8;
         }
      }
      &-search {
         width: 190px;
         display: flex;
         flex-direction: column;
         justify-content: center;
      }
      &-searchInput {
         background-color: #72ddff;
         border-radius: 10px;
         border: 0;
         padding: 10px;
         outline: none;
         &:focus {
            background-color: #81E6FF;
         }
      }
   }
</style>
