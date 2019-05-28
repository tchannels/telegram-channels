<template>
   <div id="app">
      <headerMenu />
      <div class="content">
         <router-view/>
      </div>
   </div>
</template>

<script lang="ts">
   import { Component, Prop, Vue } from 'vue-property-decorator';
   import headerMenu from './components/Header.vue';

   @Component({
      components: {
         headerMenu,
      },
   })
   export default class App extends Vue {

   }
</script>

<style>
   body {
      padding: 0;
      margin: 0;
      font-family: Arial,serif;
      background-color: #F5F5F5;
   }

   .content {
      margin: 12px;
      padding: 12px;
      background-color: #fff;
   }
</style>
