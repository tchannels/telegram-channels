import Vue from 'vue';
import VueRouter from 'vue-router';

const Channels = () => import('./views/Channels.vue');
const Bots = () => import('./views/Bots.vue');
Vue.use(VueRouter);

const routes = [
   { path: '/', component: Channels },
   { path: '/channels', component: Channels },
   { path: '/bots', component: Bots },
];

export default new VueRouter({
   mode: 'history',
   routes,
});
