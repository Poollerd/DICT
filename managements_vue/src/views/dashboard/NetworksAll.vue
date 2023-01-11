<template>
    <div class="container">
        <div class="columns is-multiline">
            <div>
                <!-- <h1 class="title is-4">ส่วนราชการ : {{ team.team_name }}  : User name : {{ $store.state.user.username }}</h1> -->
                <!-- <h1 class="is-3">User name : {{ $store.state.user.username }}</h1> -->
                <!-- <h1 class="subtitle">User name : {{ $store.state.user.username }}</h1> -->
                <!-- <hr>  -->
            </div>
            <div class="column is-12">
                <!-- <h3 class="title">Networks RTAF</h3> -->
                <h4 class="title is-5">Networks RTAF</h4>
                <router-link 
                    to="/dashboard/networks/add-network"
                >+ ข้อมูล Networks ในหน่วย</router-link>
                <form @submit.prevent="getAllNetworks">
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
                <template v-if="networks.length">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>สถานที่ติดตั้ง</th>
                                <th>ชนิดอุปกรณ์เครือข่าย</th>
                                <th>ยี่ห้ออุปกรณ์เครือข่าย</th>
                                <!-- <th>ยี่ห้อของอุปกรณ์</th>
                                <th>ชื่อของอุปกรณ์</th>
                                <th>รุ่นของอุปกรณ์</th> -->
                                <th>ชื่ออุปกรณ์ในระบบ</th>
                                <!-- <th>Mac Address</th>
                                <th>IP Address</th>
                                <th>ที่มาของอุปกรณ์</th>
                                <th>Serial Number</th> -->
                                <th>จนท.ผู้รับผิดชอบ</th>
                                <th>เบอร์โทรศัพท์ติดต่อ</th>
                                <th>สังกัด</th>
                                <th>สถานะ</th>
                                <!-- <th>หมายเหตุ</th> -->
                                <!-- <th>รายละเอียด</th> -->
                            </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="network in networks"
                                v-bind:key="network.id">
                                    <td>{{ network.network_install_place }}</td>
                                    <td>{{ network.network_type }}</td>
                                    <td>{{ network.network_brand }}</td>
                                    <td>{{ network.network_name }}</td>
                                    <!-- <td>{{ network.network_version }}</td>
                                    <td>{{ network.network_name_in_system }}</td>
                                    <td>{{ network.network_mac_address }}</td> -->
                                    <!-- <td>{{ network.network_ip_address  }}</td> -->
                                    <!-- <td>{{ network.network_got }}</td> -->
                                    <!-- <td>{{ network.network_serial_number }}</td> -->
                                    <td>{{ network.network_person_responsible }}</td>
                                    <td>{{ network.network_person_responsible_phone }}</td>
                                    <!-- <td>{{ team.team_name }}</td> -->

                                    <td>{{ network.network_status }}</td>
                                    <!-- <td>{{ network.network_note }}</td> -->
                                    <!-- <td>
                                        <template v-if="personal.assigned_to">{{ personal.assigned_to.first_name }} {{ personal.assigned_to.last_name }}</template>
                                    </td> -->
                                    <td>
                                        <router-link :to="{ name: 'Network', params: { id: network.id }}">Details</router-link>
                                    </td>
                            </tr>
                        </tbody>
                    </table>
                </template>
                <template v-else>
                    <p>You don't have any Network yet...</p>
                </template>
                <div class="buttons">
                    <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">ย้อนกลับ</button>
                    <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">หน้าถัดไป</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Networks',

        data() {
            return {
                networksall: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1,
                query: '',
                num_networks: 0,

            }
        },

        mounted() {
            this.getAllNetworks()
        
        },

        methods: {
            goToNextPage() {
                this.currentPage += 1
                this.getAllNetworks()
            },
            goToPreviousPage() {
                this.currentPage -= 1
                this.getAllNetworks()
            },
            // async getTeam() {

            //     this.$store.commit('setIsLoading', true)

            //     await axios
            //           .get('/api/dict/teams/get_my_team/')
            //         .then(response => {
            //             console.log(response.data)
            //             this.team = response.data
            //         })
            //         .catch(error =>{
            //             console.log(error)
            //         })                    
            //     this.$store.commit('setIsLoading', false)
            //     },

            async getAllNetworks() {
                this.$store.commit('setIsLoading', true)
                this.showNextButton = false
                this.showPreviousButton = false
                await axios
                    .get(`/api/dict/networks/`)
                    .then(response => {
                        console.log(response.data)
                        this.num_networks = response.data.count
                    })

                await axios
                    // .get(`/api/dict/networks/`)
                    .get(`/api/dict/networks/?page=${this.currentPage}&search=${this.query}`)
                    .then(response => {
                        this.networks = response.data.results
                        // this.networks = response.data
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