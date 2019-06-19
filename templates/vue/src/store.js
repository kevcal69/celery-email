import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
    state: {},
    actions: {
        sendEmail(context, payload) {
            var form_data = new FormData();

            for ( let key in payload ) {
                form_data.append(key, payload[key]);
            }
            return axios.post(
                'api/email-queue',
                form_data,
                {
                    xsrfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                }
            )
            .catch(error => {
                return error.response
            })
        },
        fetchEmailQueue(context, top) {
            return axios.get('api/email-queue', {params: { top }});
        }
    }

})