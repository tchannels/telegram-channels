<template>
   <section>
      {{text}}
   </section>
</template>

<script lang="ts">
   import {Component, Vue} from 'vue-property-decorator';

   @Component
   export default class Page2 extends Vue {
      public text: string = 'Another text';
   }
</script>

<style lang="less" scoped>
   section {
      background-color: white;
      padding: 12px;
   }
</style>
