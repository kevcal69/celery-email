import Vue from 'vue'
import Router from 'vue-router'
import HomePage from 'components/HomePage'
import EmailForm from 'components/EmailForm'
import EmailList from 'components/EmailList'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomePage
        },
        {
            path: '/email-queue',
            name: 'queue',
            component: EmailList
        },
    ],
    mode: 'history',
    scrollBehavior (to, from, savedPosition) {
        return { x: 0, y: 0 }
    }
})