<template>
    <div class="container">
        <div class="columns is-multiline">
            <div>
                <!-- <h1 class="title is-4">ส่วนราชการ : {{ team.team_name }} : User name : {{ $store.state.user.username }}</h1> -->
                <!-- <h1 class="subtitle">User name : {{ $store.state.user.username }}</h1> -->
                <!-- <hr>  -->
            </div>
            <div class="column is-12">
                <h1 class="title is-4">Computers RTAF</h1>
                <router-link 
                    to="/dashboard/computers/add-Computer"
                >+ ข้อมูล Computers ในหน่วย</router-link>
                <form @submit.prevent="getComputers">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-success">Search</button>
                        </div>
                    </div>
                </form>
            </div>
            <div class="column is-12">
                <template v-if="computers.length">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>สถานที่ติดตั้ง</th>
                                <th>ชนิดคอมพิวเตอร์</th>
                                <th>ชื่อเครื่องคอมพิวเตอร์</th>
                                <th>ยี่ห้อของอุปกรณ์</th>
                                <th>ผู้รับผิดชอบ</th>
                                <th>โทรศัพท์ติดต่อ</th>
                                <th>สังกัด</th>
                                <th>สถานะ</th>
                                <th>รายละเอียด</th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="computer in computers"
                                v-bind:key="computer.id">
                                    <td>{{ computer.computer_install_place }}</td>
                                    <td>{{ computer.computer_type }}</td>
                                    <td>{{ computer.computer_name }}</td>
                                    <td>{{ computer.computer_brand }}</td>
                                    <td>{{ computer.person_responsible }}</td>
                                    <td>{{ computer.person_responsible_phone  }}</td>
                                    <!-- <td>{{ team.team_name }}</td> -->
                                    <td>{{ computer.status_computer }}</td>

                                    <!-- <td>
                                        <template v-if="personal.assigned_to">{{ personal.assigned_to.first_name }} {{ personal.assigned_to.last_name }}</template>
                                    </td> -->
                                    <td>
                                        <router-link :to="{ name: 'Computer', params: { id: computer.id }}">Details</router-link>
                                    </td>
                            </tr>
                        </tbody>
                    </table>
                </template>
                <template v-else>
                    <p>You don't have any Computer yet...</p>
                </template>
                <div class="buttons">
                    <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
                    <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Next</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Computers',

        data() {
            return {
                computers: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1,
                query: '',
                num_computers: 0,
            }
        },
        mounted() {
            this.getAllComputers()

        },
        methods: {
            goToNextPage() {
                this.currentPage += 1
                this.getAllComputers()
            },
            goToPreviousPage() {
                this.currentPage -= 1
                this.getAllComputers()
            },
            // async getTeam() {

            //     this.$store.commit('setIsLoading', true)

            //     await axios
            //         .get('/api/dict/teams/get_my_team/')
            //         .then(response => {
            //             console.log(response.data)
            //             this.team = response.data
            //         })
            //         .catch(error =>{
            //             console.log(error)
            //         })                    
            //     this.$store.commit('setIsLoading', false)
            //     },

            async getAllComputers() {
                this.$store.commit('setIsLoading', true)
                this.showNextButton = false
                this.showPreviousButton = false

                await axios
                    .get(`/api/dict/computers/`)
                    .then(response => {
                        console.log(response.data)
                        this.num_computers = response.data.count
                    })
                await axios
                    // .get(`/api/dict/computers/`)
                    .get(`/api/dict/computers/?page=${this.currentPage}&search=${this.query}`)
                    .then(response => {
                        this.computers = response.data.results
                        // this.computers = response.data
                        if (response.data.next) {
                            this.showNextButton = true
                        }
                        if (response.data.previous) {
                            this.showPreviousButton = true
                        }
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>