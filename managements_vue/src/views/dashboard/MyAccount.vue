<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Account of : {{ $store.state.user.username }}</h1>
                <h1 class="title">email : {{ $store.state.user.email }}</h1>
                <h1 class="title">สังกัด {{ $store.state.team.team_name }} </h1>
                <h1> {{ $store.state.team.subteam_name }}</h1>
            </div>
            <div class="column is-12">
                <div class="buttons">

                    <router-link :to="{ name: 'EditMember', params: { id: $store.state.user.id }}" class="button is-light">Edit Data</router-link>

                    <button @click="logout()" class="button is-danger">Log out</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    import axios from 'axios'

    export default {

        name: 'MyAccount',
        data () {
            return {
                username: '',
                firstname: '',
                lastname: '',
            }
        },

        methods: {

            async logout() {
                await axios
                    .post('/api/dict/token/logout/')
                    .then(response => {

                        console.log('Logged out')

                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                localStorage.removeItem('username')
                localStorage.removeItem('firstname')
                localStorage.removeItem('lastname')
                localStorage.removeItem('userid')
                localStorage.removeItem('team_name')
                localStorage.removeItem('subteam_name')
                localStorage.removeItem('team_id')

                this.$store.commit('removeToken')

                this.$router.push('/')
            }



        }

    }

</script>
