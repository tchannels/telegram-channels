import Vue from 'Vue';
import VueRouter from 'vue-router';

const routes = [
    // { path: '/', component: Component },
];

Vue.use(VueRouter);
const router = new VueRouter({ mode: 'history', routes });
export default router;
