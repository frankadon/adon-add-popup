import { createStore } from 'vuex'

export default createStore({
  state: {
    access: '',
    refresh: ''
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem("access")) {
        state.access = localStorage.getItem("access")
        state.refresh = localStorage.getItem("refresh")
      } else {
        state.access = ''
        state.refresh = ''
      }
    },
    setAccess(state, access){
      state.access = access
    },
    setRefreshToken(state, refresh){
      state.refresh = refresh
    }
  },
  actions: {
  },
  modules: {
  }
})