import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify/lib'
// import 'vuetify/dist/vuetify.min.css'
import 'vuetify/src/stylus/main.styl'




Vue.config.productionTip = false;
Vue.use(Vuetify);

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

/*
, {
    VApp,
    VDialog,
    VCard,
    VCardText,
    VToolbar,
    VSpacer,
    VBtn,
    VMenu,
    VList,
    VListTile,
    VListTileTitle,
    VTabs,
    VTabItem
}

, {
    components: {
    VApp,
    VDialog,
    VCard,
    VCardText,
    VToolbar,
    VSpacer,
    VBtn,
    VMenu,
    VList,
    VListTile,
    VListTileTitle,
    VTabs,
    VTabItem
}
}
 */
