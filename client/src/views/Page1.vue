<template>
   <div>
      Content {{text}}
   </div>
</template>

<script lang="ts">
   import {Component, Prop, Vue} from 'vue-property-decorator';

   @Component
   export default class Page1 extends Vue {
      public text: string = 'from 1-st page';
   }
</script>

<style scoped>

</style>
