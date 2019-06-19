import Vue from 'vue'
import App from './app'
import router from './router'
import store from './store'

import antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

Vue.use(antd);


new Vue({
    el: '#app',
    router,
    store,
    components: { App },
    template: '<App/>'
})