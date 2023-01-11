<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label>E - mail</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat Password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
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

    import {toast} from 'bulma-toast'


    export default {
    
        name: 'Signup',

        data () {
            return {
                username: '',
                email:'',
                password1: '',
                password2: '',
                errors: []
            }
        },

        methods: {
            async submitForm(){
                console.log('submitForm')

                console.log(this.username)

                this.errors = []

                if (this.username === '') {
                    this.errors.push('The username is missing')
                }

                if (this.password1 === '') {
                    this.errors.push('The password is too short')
                }

                if (this.password1 !== this.password2) {
                    this.errors.push('The password are not matching')
                }

                if (!this.errors.length) {
                    this.$store.commit('setIsLoading', true)

                    const formData = {

                        username: this.username,
                        email: this.email,
                        password: this.password1

                    }

                    await axios
                        .post('/api/dict/users/', formData)
                        .then(response => {
                            toast({
                                message: 'คุณมี account แล้ว, โปรด login',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 3000,
                                position: 'bottom-right',
                            })

                            this.$router.push('/log-in')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data){
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }
                                console.log(JSON.stringify(error.response.data))

                            } else if (error.response) {
                                this.errors.push('มีบางอย่างผิดพลาด. โปรดลองใหม่!')
                                console.log(JSON.stringify(error.message))

                            } else {
                                console.log(JSON.stringify(error))
                               
                            }
                        })
                    this.$store.commit('setIsLoading', false)
                }
            }
        }
    }
</script>