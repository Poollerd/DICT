<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-8 is-offset-2">
                <h1 class="title">แก้ไขข้อมูล Network </h1>
            </div>
          
            <div class="column is-half is-offset-one-quarter">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>สถานที่ติดตั้ง</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_install_place">
                        </div>
                    </div>
                     <div class="field">
                        <label>ประเภทอุปกรณ์ Network</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="network.network_type">
                                    <option value="Router">Rounter</option>
                                    <option value="Switch">Switch</option>
                                    <option value="CONVERTER">CONVERTER</option>
                                    <option value="ACCESS POINT">ACCESS POINT</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>ยี่ห้ออุปกรณ์เครือข่าย</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_brand">
                        </div>
                    </div>

                    <div class="field">
                        <label>ชื่อในระบบ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_name_in_system">
                        </div>
                    </div>
                    <div class="field">
                        <label>IP address</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_mac_address">
                        </div>
                    </div>
                    <div class="field">
                        <label>MAC address</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_ip_address">
                        </div>
                    </div>
                    <div class="field">
                        <label>ที่มาของอุปกรณ์(โครงการ/หน่วยจัดหา/ส่วนตัว)</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_got">
                        </div>
                    </div>
                    <div class="field">
                        <label>Serial Number</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_serial_number">
                        </div>
                    </div>
                    <div class="field">
                        <label>ผู้รับผิดชอบ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_person_responsible">
                        </div>
                    </div>
                    <div class="field">
                        <label>เบอร์โทรศัพท์ติดต่อ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_person_responsible_phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>สถานะเครื่องคอมพิวเตอร์</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="network.network_status">
                                    <option value="ใช้ราชการ">ใช้ราชการ</option>
                                    <option value="ชำรุด">ชำรุด</option>
                                    <option value="ส่งซ่อม">ส่งซ่อม</option>
                                    <option value="เบิกเปลี่ยน">เบิกเปลี่ยน</option>

                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>หมายเหตุ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network.network_note">
                        </div>
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
    import { toast } from 'bulma-toast'
    export default {
        name: 'EditNetwork',
        data() {
            return {
                network: {},
                // team: {
                //     members: []
                // }
            }
        },
        mounted() {
            this.getNetwork()
            // this.getTeam()
        },
        methods: {
            async getNetwork() {
                this.$store.commit('setIsLoading', true)
                const networkID = this.$route.params.id
                axios
                    .get(`/api/dict/networks/${networkID}/`)
                    .then(response => {
                        this.network = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const networkID = this.$route.params.id
                axios
                    .patch(`/api/dict/networks/${networkID}/`, this.network)
                    .then(response => {
                        toast({
                            message: 'แก้ไขข้อมูลเรียบร้อย',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push(`/dashboard/networks/${networkID}`)
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },

        }
    }
</script>