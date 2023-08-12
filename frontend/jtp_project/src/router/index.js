import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Places from '../components/Places.vue'
import NLP from '../components/NLP.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/places',
      name: 'Places',
      component: Places
    },
    {
      path: '/nlp',
      name: 'NLP',
      component: NLP
    }
  ]
})

export default router
