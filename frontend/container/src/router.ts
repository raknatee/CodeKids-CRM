import { createRouter, createWebHistory } from "vue-router";
<<<<<<< HEAD
import Home from "./pages/Home.vue";
import About from "./pages/about.vue";
import Customer from "./pages/customer/index.vue";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "home", component: Home },
    { path: "/about", name: "about", component: About },
    { path: "/customer", name: "customer", component: Customer },
  ],
=======
>>>>>>> f230285 (chore: router)
import ContactSession from "./pages/contact-session/index.vue";



const routes = [
  { path: '/', component: ()=>import('./pages/Home.vue') },
  { path: '/about', component: ()=>import('./pages/about.vue') },
  { path: '/login', component: ()=>import('./pages/login/index.vue')},
  { path: "/contact-session", name: "contact-session", component: ContactSession },
]

export const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});