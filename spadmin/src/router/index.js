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
        component: () => import('../views/User/Login.vue'),
        meta: {
          needLogin: false
        }
      }
    ]
  },
  {
    path: '/',
    component: () => import('@/layout/BasicLayout.vue'),
    meta: {
      needLogin: true
    },
    children: [{
        path: '/',
        redirect: '/dashboard/analysis'
      },
      {
        path: '/dashboard',
        name: 'dashboard',
        meta: {
          needLogin: true
        },
        component: {
          render: h => h("router-view")
        },
        children: [{
            path: '/dashboard/analysis',
            name: 'analysis',
            meta: {
              needLogin: true
            },
            component: () => import('../views/Dashboard/Analysis.vue')
          },
          {
            path: '/user/manage',
            name: 'manage',
            component: () => import('../views/User/Manage.vue'),
            meta: {
              needLogin: true
            }
          },
          {
            path: '/system/fileupload',
            name: 'fileupload',
            meta: {
              needLogin: true
            },
            component: () => import('../views/System/FileUpload.vue')
          },
          {
            path: '/system/jobsmanage',
            name: 'jobsmanage',
            meta: {
              needLogin: true
            },
            component: () => import('../views/System/JobsManage.vue')
          },
          {
            path: '/system/holiday',
            name: 'holiday',
            meta: {
              needLogin: true
            },
            component: () => import('../views/System/Holiday.vue')
          },
          {
            path: '/analysis/fbp',
            name: 'fbp',
            meta: {
              needLogin: true
            },
            component: () => import('../views/Analysis/FBProphet.vue')
          },
          {
            path: '/analysis/timeanalysis',
            name: 'timeanalysis',
            meta: {
              needLogin: true
            },
            component: () => import('../views/Analysis/TimeAnalysis.vue')
          }
        ]
      }
    ]
  },
  {
    path: '*',
    name: '404',
    meta: {
      needLogin: false
    },
    component: () => import('../views/404.vue')
  },

];
const router = new VueRouter({
  routes
});
router.beforeEach((to, from, next) => {
  NProgress.start();
  if(!to.meta.needLogin) {
    next();
  } else if(localStorage.getItem('flag') == 'isLogin') {
    next()
  } else {
    next({path: '/user/login'});
  }
})
router.afterEach(() => {
  NProgress.done();
})


export default router