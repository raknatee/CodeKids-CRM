import { createRouter, createWebHistory } from "vue-router";

const routes = [
  { path: '/', component: ()=>import('./pages/Home.vue') },
  { path: '/about', component: ()=>import('./pages/about.vue') },
  { path: '/login', component: ()=>import('./pages/login/index.vue')},
  { path: "/contact-session", component: ()=>import('./pages/contact-session/index.vue') },
  { path: "/customer", component: ()=>import("./pages/customer/index.vue")}
]

export const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});