<template>
   <section class="channel">
      <div v-for="channel in channelsFiltered" class="channel-block">
         <a class="channel-title" :href="`https://t.me/${channel.channel_id}`" target="_blank" :title="channel.title">{{channel.title}}</a>
      </div>
   </section>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {Action, Getter} from 'vuex-class';

@Component({
   beforeRouteEnter(to, from, next) {
      next((vm: any) => {
         vm.getData();
      });
   },
})
export default class Channels extends Vue {
   @Action('getData') public getData: any;
   @Getter('channelsFiltered') public channelsFiltered: any;
}
</script>

<style lang="less" scoped>
   .channel {
      &-block {
         display: inline-flex;
         width: calc(25% - 33px);
         height: 50px;
         padding: 12px;
         margin: 0 12px 12px 0;
         background-color: #fff;
         color: #384047;

         &:nth-child(4n) {
            margin-right: 0;
         }
      }

      &-title {
         color: #384047;
         text-decoration: none;
         font-weight: bold;
         overflow: hidden;
         text-overflow: ellipsis;
      }
   }
</style>
