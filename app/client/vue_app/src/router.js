import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import FileUpload from './views/FileUpload'
import VisualizePage from './views/VisualizePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/upload',
      name: 'upload',
      component: FileUpload
    },
    {
      path: '/visualize',
      name: 'visualize',
      component: VisualizePage
    }
  ]
})
