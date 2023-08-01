import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Places from '../components/Places.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/places',
      name: 'Places',
      component: Places
    }
  ]
})

export default router
