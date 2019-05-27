<template>
   <div>
      {{text}}
   </div>
</template>

<script lang="ts">
   import {Component, Prop, Vue} from 'vue-property-decorator';

   @Component
   export default class Page2 extends Vue {
      public text: string = 'Another text';
   }
</script>

<style scoped>

</style>
