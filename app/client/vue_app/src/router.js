import Vue from 'vue'
import Router from 'vue-router'
const CompareModified = () => import('./views/CompareModified');
const CompareSound = () => import('./views/CompareSound');
const FileUpload = () => import('./views/FileUpload');
const VisualizeLayer = () => import('./views/VisualizeLayer');

Vue.use(Router);

export default new Router({
    routes: [

        {
            path: '/',
            name: 'Upload',
            component: FileUpload
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
        },{
            path: '/compare-modified',
            name: 'compare-modified',
            component: CompareModified
        },
    ]
})
