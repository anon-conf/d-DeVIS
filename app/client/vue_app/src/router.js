import Vue from 'vue'
import Router from 'vue-router'
import Index from './views/Index'
import FileUpload from './views/FileUpload'
import VisualizePage from './views/VisualizePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
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
