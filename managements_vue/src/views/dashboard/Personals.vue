<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">นายทหารเทคโนโลยีสารสนเทศและสงครามอิเล็คทรอนิกส์</h1>
                <router-link 
                    to="/dashboard/personals/add-personal"
                >+ นายทหารเทคโนโลยีสารสนเทศและสงครามอิเล็คทรอนิกส์</router-link>
                <form @submit.prevent="getPersonals">
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
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>ยศ</th>
                            <th>ชื่อ</th>
                            <th>นามสกุล</th>
                            <th>ตำแหน่ง</th>
                            <th>สังกัด</th>
                            <th>สถานะ</th>
                            <th>รายละเอียด</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="personal in personals"
                            v-bind:key="personal.id">
                                <td>{{ personal.rank }}</td>
                                <td>{{ personal.first_name }}</td>
                                <td>{{ personal.last_name }}</td>
                                <td>{{ personal.position }}</td>
                                <td>{{ personal.department }}</td>
   
                                <td class="is-selected">{{ personal.status }}</td>

                                <!-- <td>
                                    <template v-if="personal.assigned_to">{{ personal.assigned_to.first_name }} {{ personal.assigned_to.last_name }}</template>
                                </td> -->
                                <td>
                                    <router-link :to="{ name: 'Personal', params: { id: personal.id }}">Details</router-link>
                                </td>
                        </tr>
                    </tbody>
                </table>

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
        name: 'Personals',
        data() {
            return {
                personals: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1,
                query: '',
                num_personals: 0
            }
        },
        mounted() {
            this.getPersonals()
        },
        methods: {
            goToNextPage() {
                this.currentPage += 1
                this.getPersonals()
            },
            goToPreviousPage() {
                this.currentPage -= 1
                this.getPersonals()
            },
            async getPersonals() {
                this.$store.commit('setIsLoading', true)
                
                this.showNextButton = false
                this.showPreviousButton = false

                await axios
                    .get(`/api/dict/personals/`)
                    .then(response => {
                        console.log("Next",response.data)
                        this.num_personals = response.data.count
                    })
                await axios
                    // .get('/api/dict/personals/')
                    .get(`/api/dict/personals/?page=${this.currentPage}&search=${this.query}`)
                    .then(response => {
                        this.personals = response.data.results
                        // this.personals = response.data
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