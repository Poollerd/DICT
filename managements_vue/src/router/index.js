import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'

import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Personals from '../views/dashboard/Personals.vue'
import Personal from '../views/dashboard/Personal.vue'
import AddPersonal from '../views/dashboard/AddPersonal.vue'
import AddTeam from '../views/dashboard/AddTeam.vue'
import AddMember from '../views/dashboard/AddMember.vue'
import Team from '../views/dashboard/Team.vue'
import EditPersonal from '../views/dashboard/EditPersonal.vue'
import EditMember from '../views/dashboard/EditMember.vue'

import Computers from '../views/dashboard/Computers.vue'
import Computer from '../views/dashboard/Computer.vue'
import AddComputer from '../views/dashboard/AddComputer.vue'
import EditComputer from '../views/dashboard/EditComputer.vue'
import Networks from '../views/dashboard/Networks.vue'
import NetworksAll from '../views/dashboard/NetworksAll.vue'
import Network from '../views/dashboard/Network.vue'
import AddNetwork from '../views/dashboard/AddNetwork.vue'
import EditNetwork from '../views/dashboard/EditNetwork.vue'
import AddUpgradeComputer from '../views/dashboard/AddUpgradeComputer.vue'
import ComputersAll from '../views/dashboard/ComputersAll.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/personals',
    name: 'Personals',
    component: Personals,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/personals/:id',
    name: 'Personal',
    component: Personal,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/personals/:id/edit-personal',
    name: 'EditPersonal',
    component: EditPersonal,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/personals/add-personal',
    name: 'AddPersonal',
    component: AddPersonal,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/add-team',
    name: 'AddTeam',
    component: AddTeam,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team',
    name: 'Team',
    component: Team,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/add-member',
    name: 'AddMember',
    component: AddMember,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/computers',
    name: 'Computers',
    component: Computers,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/All-computers',
    name: 'ComputersAll',
    component: ComputersAll,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/networks',
    name: 'Networks',
    component: Networks,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/All-Networks',
    name: 'NetworksAll',
    component: NetworksAll,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/computers/add-computer',
    name: 'AddComputer',
    component: AddComputer,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/computers/:id/add-update-computer',
    name: 'AddUpgradeComputer',
    component: AddUpgradeComputer,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/networks/add-network',
    name: 'AddNetwork',
    component: AddNetwork,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/computers/:id',
    name: 'Computer',
    component: Computer,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/networks/:id',
    name: 'Network',
    component: Network,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/computers/:id/edit-computer',
    name: 'EditComputer',
    component: EditComputer,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/edit-member/:id',
    name: 'EditMember',
    component: EditMember,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/networks/:id/edit-network',
    name: 'EditNetwork',
    component: EditNetwork,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
router.beforeEach((to, from, next) => {

  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {

    next('/log-in')

  } else {

    next()
    
  }

})
export default router
