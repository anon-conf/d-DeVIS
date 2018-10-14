import Vue from 'vue'
import Router from 'vue-router'
import CompareSound from './views/CompareSound'
import FileUpload from './views/FileUpload'
import VisualizePage from './views/VisualizePage'
import VisualizeLayer from './views/VisualizeLayer'

Vue.use(Router);

export default new Router({
    routes: [

        {
            path: '/',
            name: 'Upload',
            component: FileUpload
        },
        {
            path: '/visualize',
            name: 'visualize',
            component: VisualizePage
        },
        {
            path: '/layers',
            name: 'layers',
            component: VisualizeLayer
        },
        {
            path: '/compare',
            name: 'compare',
            component: CompareSound
        },
    ]
})
