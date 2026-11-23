import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Home from './views/Home.vue'
import Lesson from './views/Lesson.vue'
import Quiz from './views/Quiz.vue'
import './style.css'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: Home },
    { path: '/:unit(unit0[1-8])', component: Lesson },
    { path: '/:unit(unit0[1-8])/quiz', component: Quiz },
    { path: '/:pathMatch(.*)*', redirect: '/' }
  ],
  scrollBehavior: () => ({ top: 0 })
})
createApp(App).use(router).mount('#app')
