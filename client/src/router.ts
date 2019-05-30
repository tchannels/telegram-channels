import Vue from 'vue';
import VueRouter from 'vue-router';
const Page1 = () => import('./views/Page1.vue');
const Page2 = () => import('./views/Page2.vue');
Vue.use(VueRouter);


const routes = [
   { path: '/', component: Page1 },
   { path: '/page1', component: Page1 },
   { path: '/page2', component: Page2 },
];

export default new VueRouter({
   mode: 'history',
   routes,
});
