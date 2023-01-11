<template>
    <nav class="navbar is-info">

        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>DICT Managements</strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <template v-if="$store.state.isAuthenticated">
  

                    <div id="navbarExampleTransparentExample" class="navbar-menu">
                        <div class="navbar-start">
                            <a class="navbar-item" href="/dashboard/all-computers/">
                                Home
                            </a>
                        </div>
                        <div class="navbar-item has-dropdown is-hoverable">
                            <a class="navbar-link" href="#">
                                Personal
                            </a>
                            <div class="navbar-dropdown is-boxed">
                                <a class="navbar-item" href="/dashboard/personals/">
                                    Person ICT
                                </a>
                                <a class="navbar-item" href="#">
                                    All Person ICT
                                </a>
                                <a class="navbar-item" href="http://localhost:8000/admin/">
                                    Admin
                                </a>
                            </div>                            
                        </div>
                    </div>
                    <div id="navbarExampleTransparentExample" class="navbar-menu">
                        <div class="navbar-item has-dropdown is-hoverable">
                            <a class="navbar-link" href="#">
                            Hardware
                            </a>
                            <div class="navbar-dropdown is-boxed">
                                <a class="navbar-item" href="/dashboard/computers/">
                                    Computer 
                                </a>
                                <a class="navbar-item" href="#">
                                    Printer 
                                </a>
                                <a class="navbar-item" href="#">
                                    All 
                                </a>
                            </div>
                        </div>
                    </div>   
                    <div id="navbarExampleTransparentExample" class="navbar-menu">                      
                        <div class="navbar-item has-dropdown is-hoverable">
                            <a class="navbar-link" href="#">
                            Network
                            </a>
                            <div class="navbar-dropdown is-boxed">
                                <a class="navbar-item" href="/dashboard/networks/">
                                    Network 
                                </a>
                                <a class="navbar-item" href="/dashboard/all-networks/">
                                    All 
                                </a>
                            </div>                            
                        </div>
                    </div>
                    <div id="navbarExampleTransparentExample" class="navbar-menu">
                        <div class="navbar-item has-dropdown is-hoverable">
                            <a class="navbar-link" href="#">
                            Software
                            </a>
                            <div class="navbar-dropdown is-boxed">
                                <a class="navbar-item" href="#">
                                    Software
                                </a>
                                <a class="navbar-item" href="#">
                                    All 
                                </a>
                            </div>                            
                        </div>
                    </div>
                    <!-- <router-link to="/dashboard/personals/" class="navbar-item ">Person</router-link> -->

                    <!-- <router-link to="/dashboard/clients/" class="navbar-item ">Computer</router-link> -->
                    <!-- <router-link to="/dashboard/clients/" class="navbar-item ">Network</router-link> -->
                    <!-- <router-link to="/dashboard/clients/" class="navbar-item ">Software</router-link> -->
                    <router-link to="/dashboard/team/" class="navbar-item ">สังกัด</router-link>
                </template>
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up" class="button is-success">
                                <strong>Sign up</strong></router-link>
                            <router-link to="/log-in" class="button is-light">log in</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/dashboard/my-account" class="button is-primary">My Data</router-link>
                        </template>
                    </div>
                </div>

            </div>
        </div>
    </nav>
</template>
<script>
    export default {
        name: 'Navbar'
    }
</script>