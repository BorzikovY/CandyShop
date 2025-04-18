import { createRouter, createWebHistory } from 'vue-router'
import { setupLayouts } from 'virtual:generated-layouts'

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/pages/HomePage.vue")
  },
  {
    path: "/about",
    name: "About",
    component: () => import("@/pages/About.vue")
  },
  {
    path: "/store",
    name: "Store",
    component: () => import("@/pages/Store.vue")
  },
  {
    path: "/guarantees",
    name: "Guarantee",
    component: () => import("@/pages/GuaranteesPage.vue")
  }

]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: setupLayouts(routes),
})

// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
    if (!localStorage.getItem('vuetify:dynamic-reload')) {
      console.log('Reloading page to fix dynamic import error')
      localStorage.setItem('vuetify:dynamic-reload', 'true')
      location.assign(to.fullPath)
    } else {
      console.error('Dynamic import error, reloading page did not fix it', err)
    }
  } else {
    console.error(err)
  }
})

router.isReady().then(() => {
  localStorage.removeItem('vuetify:dynamic-reload')
})

export default router
