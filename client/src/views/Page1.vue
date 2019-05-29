<template>
   <section>
      Content {{text}}
   </section>
</template>

<script lang="ts">
   import {Component, Vue} from 'vue-property-decorator';

   @Component
   export default class Page1 extends Vue {
      public text: string = 'from 1-st page';
   }
</script>

<style lang="less" scoped>
   section {
      background-color: white;
      padding: 12px;
   }
</style>
