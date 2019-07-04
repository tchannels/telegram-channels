import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const apiHost = 'http://37.230.114.137:5000';

export function createStore() {
   return new Vuex.Store({
      state: {
         channels: [],
         searchString: '',
      },

      actions: {
         getData({commit}, request) {
            return axios
               .get(`${apiHost}/channels`)
               .then((response) => {
                  commit('setData', response.data);
               });
         },
      },

      mutations: {
         setData(state, data) {
            Vue.set(state, 'channels', data);
         },
         setSearch(state, data) {
            Vue.set(state, 'searchString', data);
         },
      },

      getters: {
         channelsFiltered: (state) => {
            let value = state.searchString.toLowerCase();
            return state.channels.filter((channel: {title: string}) => channel.title.toLowerCase().includes(value));
         },
      },
   });
}
