<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">+ ผู้ปฏิบัติงานในสังกัด</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" name="username" class="input" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="email">
                        </div>
                    </div>
                    <!-- <div class="field">
                        <label>First name</label>
                        <div class="control">
                            <input type="text" name ="firstname" class="input" v-model="firstname">
                        </div>
                    </div>
                    <div class="field">
                        <label>Last name</label>
                        <div class="control">
                            <input type="text" name="lastname" class="input" v-model="lastname">
                        </div>
                    </div> -->
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
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
    name: 'AddMember',
    data() {
        return {
            username: '',
            email: '',
            // firstname: '',
            // lastnam: '',
            password1: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }
            if (this.email === '') {
                this.errors.push('The email is missing')
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
                    firstname: this.firstname,
                    lastname: this.lastname,
                    password: this.password1
                }
                await axios
                    .post('/api/dict/users/', formData)
                    .then(response => {
                        toast({
                            message: 'The member was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        const emailData = {'username': this.username}
                        axios
                            .post('/api/dict/teams/add_member/', emailData)
                            .then(response => {
                                this.$router.push({'name': 'Team'})
                            })
                            .catch(error => {
                                if (error.response) {
                                    for (const property in error.response.data) {
                                        this.errors.push(`${property}: ${error.response.data[property]}`)
                                    }
                                } else if (error.message) {
                                    this.errors.push('Something went wrong. Please try again!')
                                }
                            })
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>