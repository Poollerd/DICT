<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>

                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <!-- <input type="email" name="email" class="input" v-model="username"> -->
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>

                   <div class="notification is-danger" v-if="errors.length">
                    
                        <p v-for="error in errors" 
                            v-bind:key="error">
                            {{ error }}
                        </p>
                    
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script>

    import axios from 'axios'

    export default {
    
        name: 'LogIn',
        data () {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
            async submitForm(){
                this.$store.commit('setIsLoading', true)

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios
                    .post('/api/dict/token/login', formData)
                    .then(response => {
                        const token = response.data.auth_token

                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = 'Token ' + token

                        localStorage.setItem('token', token)


                    })

                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                                console.log(JSON.stringify(error.response.data))
                         }
                        } else if (error.response) {
                            this.errors.push('Something went wront wrong. Please try again!')
                            console.log(JSON.stringify(error.message))
                        } else {
                        console.log(JSON.stringify(error))
                        }
                    })
                
                await axios
                    .get('/api/dict/users/me')
                    .then(response => {
                        this.$store.commit('setUser', {'id' : response.data.id, 'username' : response.data.username, 'email': response.data.email, 'firstname' : response.data.firstname, 'lastname' : response.data.lastname})

                        localStorage.setItem('username', response.data.username)
                        localStorage.setItem('firstname', response.data.firstname)
                        localStorage.setItem('lastname', response.data.lastname)
                        localStorage.setItem('userid', response.data.id)
                        localStorage.setItem('email', response.data.email)

                        this.$router.push('/dashboard/my-account')
                    })
                    .catch(error =>{
                        // console.log(error)
                        console.log(JSON.stringify(error))

                    })

                await axios
                    .get('/api/dict/teams/get_my_team/')
                    .then(response => {
                        console.log(response.data)
                        this.$store.commit('setTeam', {
                            'teamid': response.data.id, 
                            'team_name': response.data.team_name,
                            'subteam_name': response.data.subteam_name,
                            // 'plan': response.data.plan.name,
                            // 'max_leads': response.data.plan.max_leads,
                            // 'max_clients': response.data.plan.max_clients
                        })
                    })
                    .catch(error =>{
                        console.log(JSON.stringify(error))
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)

            }
        },
    }
</script>