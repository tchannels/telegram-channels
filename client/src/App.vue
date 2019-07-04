<template>
   <div id="app">
      <headerMenu />
      <article class="wrapper">
         <div class="content">
            <router-view />
         </div>
      </article>
   </div>
</template>

<script lang="ts">
   import { Component, Vue } from 'vue-property-decorator';
   import headerMenu from './components/Header.vue';

   @Component({
      components: {
         headerMenu,
      },
   })
   export default class App extends Vue {

   }
</script>

<style lang="less">
   body {
      padding: 0;
      margin: 0;
      font-family: Arial,serif;
      background-color: #F5F5F5;
   }
   .wrapper {
      display: flex;
      justify-content: center;
   }
   .content {
      margin: 12px 0;
      width: 1280px;
   }
</style>
