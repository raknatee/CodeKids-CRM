import { createRouter, createWebHistory } from 'vue-router'



const routes = [
  { path: '/', component: ()=>import('./pages/Home.vue') },
  { path: '/about', component: ()=>import('./pages/about.vue') },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})