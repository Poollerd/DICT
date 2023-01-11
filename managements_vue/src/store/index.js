import { createStore } from 'vuex'

export default createStore({

  state: {

    isLoading: false,
    isAuthenticated: false,
    // isStaff: false,
    token: '',
    user: {
      id: 0,
      username: '',
      email: '',
      firstname: '',
      lastname: '',
    },

    team:{
      id: 0,
      team_name: '',
      subteam_name: '',
    //   plan: '',
    //   max_leads: 0,
    //   max_clients: 0
    },
  },

  mutations: {

    initializeStore(state) {
      if (localStorage.getItem('token')) {

        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        // state.isStaff = true
        state.user.username = localStorage.getItem('username')
        state.user.email = localStorage.getItem('email')
        state.user.firstname = localStorage.getItem('firstname')
        state.user.lastname = localStorage.getItem('lastname')
        state.user.id = localStorage.getItem('userid')
        state.team.team_name = localStorage.getItem('team_name')
        state.team.subteam_name = localStorage.getItem('subteam_name')
        state.team.id = localStorage.getItem('teamid')
        // state.team.plan = localStorage.getItem('team_plan')
        // state.team.max_leads = localStorage.getItem('team_max_leads')
        // state.team.max_clients = localStorage.getItem('team_max_clients')

      } else {

        state.token = ''
        state.isAuthenticated = false
        // state.isStaff = false
        state.user.id = 0
        state.user.username = ''
        state.user.email = ''
        state.user.firstname = ''
        state.user.lastname = ''
        state.team.id = 0
        state.team.team_name = ''
        state.team.subteam_name = ''
        // state.team.plan = ''
        // state.team.max_leads = ''
        // state.team.max_clients = ''

      }
    },

    setIsLoading(state, status){

      state.isLoading = status

    },

    setToken(state, token) {

      state.token = token
      state.isAuthenticated = true
    
    },

    removeToken(state) {

      state.token = ''
      state.isAuthenticated = false

    },

    setUser(state, user) {
      state.user = user
      // localStorage.setItem('username',user.username)
      // localStorage.setItem('email', user.email)
      // localStorage.setItem('firstname', user.firstname)
      // localStorage.setItem('lastname', user.lastname)
      // localStorage.setItem('id', user.userid)
    },

    setTeam(state, team) {
      state.team = team
      
      localStorage.setItem('id', team.teamid)
      
      localStorage.setItem('team_name', team.team_name)
      localStorage.setItem('subteam_name', team.subteam_name)
    //   localStorage.setItem('team_plan', team.plan)
    //   localStorage.setItem('team_max_leads', team.max_leads)
    //   localStorage.setItem('team_max_clients', team.max_clients)
    }
  },

  actions: {
  },

  modules: {
  }

})
