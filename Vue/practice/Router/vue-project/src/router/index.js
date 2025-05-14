import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import OverThirty from '@/components/OverThirty.vue'
import UnderThirty from '@/components/UnderThirty.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),

      beforeEnter: (to,from,next)=>{
        const userRole = 'user'
        if (userRole !== 'admin') {
          console.log('관리자만 접근할 수 있는 페이지입니다. 홈으로 리디렉션')
          next('/')
        }
      }
    },
    {
      path: '/board',
      name: 'board',
      component: () => import('@/views/BoardView.vue'),
    },
    {
      path: '/board/:id',
      name: "detail",
      component: ()=>import('../views/BoardDetailView.vue'),
      children:[
        {path:'over',name:'over-thirty', component:OverThirty},
        {path:'under',name:'under-thirty', component:UnderThirty}
      
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: ()=>import('../views/LoginView.vue')
    }
  ],
})

router.beforeEach((to,from)=> {
  const isAuthenticated = true
  if (!isAuthenticated && to.name != 'login') {
    console.log('로그인이 필요합니다. Login 페이지로 이동!')
    return {name:'login'}
  }
  if (isAuthenticated && to.name === 'login'){
    console.log('이미 로그인 상태입니다. 홈으로 이동!')
    return {name:'home'}
  }
})

export default router
