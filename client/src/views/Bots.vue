<template>
   <section>
      {{text}}
   </section>
</template>

<script lang="ts">
   import {Vue} from 'vue-property-decorator';

   export default class Bots extends Vue {
      public text: string = 'Another text';
   }
</script>

<style lang="less" scoped>
   section {
      background-color: white;
      padding: 12px;
   }
</style>
