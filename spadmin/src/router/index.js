import Vue from 'vue'
import VueRouter from 'vue-router'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
// import RenderRouterView from '../components/RenderRouterView'

Vue.use(VueRouter)

const routes = [{
    //   path: '/about',
    //   name: 'About',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import( /* webpackChunkName: "about" */ '../views/About.vue')
    // },
    // {
    //   path: '/index',
    //   name: 'Index',
    //   component: () => import('../views/Index.vue')
    // },
    path: 'user',
    name: 'user',
    component: {
      render: h => h("router-view")
    },
    children: [{
        path: '/user',
        redirect: '/user/login'
      },
      {
        path: '/user/login',
        name: 'login',
        component: () => import('../views/User/Login.vue')
      }
    ]
  },
  {
    path: '/',
    component: () => import('@/layout/BasicLayout.vue'),
    children: [{
        path: '/',
        redirect: '/dashboard/analysis'
      },
      {
        path: '/dashboard',
        name: 'dashboard',
        component: {
          render: h => h("router-view")
        },
        children: [{
            path: '/dashboard/analysis',
            name: 'analysis',
            component: () => import('../views/Dashboard/Analysis.vue')
          },
          {
            path: '/user/manage',
            name: 'manage',
            component: () => import('../views/User/Manage.vue')
          },
          {
            path: '/system/fileupload',
            name: 'fileupload',
            component: () => import('../views/System/FileUpload.vue')
          },
          {
            path: '/system/jobsmanage',
            name: 'jobsmanage',
            component: () => import('../views/System/JobsManage.vue')
          }
        ]
      }
    ]
  },
  {
    path: '*',
    name: '404',
    component: () => import('../views/404.vue')
  },

];
const router = new VueRouter({
  routes
});
router.beforeEach((to, from, next) => {
  NProgress.start();
  next();
})
router.afterEach(() => {
  NProgress.done();
})


export default router