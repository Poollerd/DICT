<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-8 is-offset-2">
                <h1 class="title">Edit ข้อมูล Computer </h1>
            </div>
           
            <div class="column is-half is-offset-one-quarter">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>สถานที่ติดตั้ง</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_install_place">
                        </div>
                    </div>
                     <!-- <div class="field">
                        <label>ชนิดคอมพิวเตอร์</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer_type">
                        </div>
                    </div> -->
                    <div class="field">
                        <label>ชนิดคอมพิวเตอร์</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="computer.computer_type">
                                    <option value="PC">PC</option>
                                    <option value="Notebook">Notebook</option>
                                    <option value="PC Server">PC Server</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>ชื่อเครื่องคอมพิวเตอร์</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_name">
                        </div>
                    </div>
                    <!-- <div class="field">
                        <label>ยี่ห้อของอุปกรณ์</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer_brand">
                        </div>
                    </div> -->
                    <div class="field">
                        <label>ยี่ห้อของอุปกรณ์</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="computer.computer_brand">
                                    <option value="Handmake">Handmake</option>
                                    <option value="Acer">Acer</option>
                                    <option value="Hp">Hp</option>
                                    <option value="SVOA">SVOA</option>
                                    <option value="Lenovo">Lenovo</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>รุ่นของอุปกรณ์</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_series">
                        </div>
                    </div>
                    <div class="field">
                        <label>หมายเลขพัสดุ ทอ.</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_number_rtaf">
                        </div>
                    </div>
                    <div class="field">
                        <label>Serial number</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_series_number">
                        </div>
                    </div>
                    <div class="field">
                        <label>ยี่ห้อ CPU</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.cpu_brand">
                        </div>
                    </div>
                    <div class="field">
                        <label>รุ่น CPU</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.cpu_model">
                        </div>
                    </div>
                    <div class="field">
                        <label>ความเร็วสัญญาณนาฬิกา</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.cpu_speed_clock">
                        </div>
                    </div>
                    <div class="field">
                        <label>หน่วยความเร็วสัญญาณนาฬิกา</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.cpu_unit_speed_clock">
                        </div>
                    </div>
                    <div class="field">
                        <label>MAC Address</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_mac_address">
                        </div>
                    </div>
                    <div class="field">
                        <label>เครื่องข่ายที่ใช้(ภายใน ทอ./ภายนอก ทอ.)</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_use_network">
                        </div>
                    </div>
                    <div class="field">
                        <label>ประเภทของ RAM</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.ram_type">
                        </div>
                    </div>
                    <div class="field">
                        <label>ความจุของ RAM</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.ram_capacity">
                        </div>
                    </div>

                    <div class="field">
                        <label>หน่วยความจุของ RAM</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.ram_unit_capacity">
                        </div>
                    </div>
                    <div class="field">
                        <label>ประเภท Harddisk Primary</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.harddisk_type_1">
                        </div>
                    </div>
                    <div class="field">
                        <label>ความจุของ Harddisk Primary</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.harddisk_capacity_1">
                        </div>
                    </div>
                    <div class="field">
                        <label>หน่วยความจุของ Harddisk Primary</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.harddisk_unit_1">
                        </div>
                    </div>
                    <div class="field">
                        <label>ประเภท Harddisk Secondary</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.harddisk_type_2">
                        </div>
                    </div>
                    <div class="field">
                        <label>ความจุของ Harddisk Secondary</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.harddisk_capacity_2">
                        </div>
                    </div>
                    <div class="field">
                        <label>หน่วยความจุของ Harddisk Secondary</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.harddisk_unit_2">
                        </div>
                    </div>
                    <div class="field">
                        <label>ชื่อระบบปฏิบัติการ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.os_computer">
                        </div>
                    </div>
                    <div class="field">
                        <label>ลิขสิทธิ์ของระบบปฏิบัติการ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.os_copyright">
                        </div>
                    </div>
                    <div class="field">
                        <label>ชื่อโปรแกรมสำนักงาน</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.office_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>รุ่นปีของโปรแกรมสำนักงาน</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.office_model_year">
                        </div>
                    </div>
                    <div class="field">
                        <label>ลิขสิทธิ์ของโปรแกรมสำนักงาน</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.office_copyright">
                        </div>
                    </div>
                    <div class="field">
                        <label>ชื่อโปรแกรมป้องกันไวรัส</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.antivirus_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>ลิขสิทธิ์ของโปรแกรมป้องกันไวรัส</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.antivirus_copyright">
                        </div>
                    </div>
                    <div class="field">
                        <label>คอมพิวเตอร์จากโครงการ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_acquisition">
                        </div>
                    </div>
                    <div class="field">
                        <label>ปีที่ติดตั้ง</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.computer_start_use_year">
                        </div>
                    </div>
                    <div class="field">
                        <label>ผู้รับผิดชอบ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.person_responsible">
                        </div>
                    </div>
                    <div class="field">
                        <label>โทรศัพท์ติดต่อผู้ที่รับผิดชอบเครื่อง</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.person_responsible_phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>สถานะเครื่องคอมพิวเตอร์</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="computer.status_computer">
                                    <option value="ใช้ราชการ">ใช้ราชการ</option>
                                    <option value="ชำรุด">ชำรุด</option>
                                    <option value="ส่งซ่อม">ส่งซ่อม</option>
                                    <option value="เบิกเปลี่ยน">เบิกเปลี่ยน</option>

                                </select>
                            </div>
                        </div>
                    </div>
                    <!-- <div class="field">
                        <label>สถานะเครื่องคอมพิวเตอร์</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="status_computer">
                                    <option value="ACTIVE">ใช้ราชการ</option>
                                    <option value="INACTIVE">ชำรุด</option>
                                    <option value="MANTAINENT">ส่งซ่อม</option>
                                    <option value="CHANGE">เบิกเปลี่ยน</option>

                                </select>
                            </div>
                        </div>
                    </div> -->
                    <div class="field">
                        <label>หมายเหตุ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="computer.note">
                        </div>
                    </div>
                    <!-- <div class="field">
                        <label>เบอร์โทรศัพท์ภายใน ทอ.</label>
                        <div class="control">
                            <input type="text" class="input" v-model="created_by">
                        </div>
                    </div>
                    <div class="field">
                        <label>เบอร์โทรศัพท์ภายใน ทอ.</label>
                        <div class="control">
                            <input type="text" class="input" v-model="created_at">
                        </div>
                    </div> -->
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
        name: 'EditComputer',
        data() {
            return {
                computer: {},
                // team: {
                //     members: []
                // }
            }
        },
        mounted() {
            this.getComputer()
            // this.getTeam()
        },
        methods: {
            async getComputer() {
                this.$store.commit('setIsLoading', true)
                const computerID = this.$route.params.id
                axios
                    .get(`/api/dict/computers/${computerID}/`)
                    .then(response => {
                        this.computer = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const computerID = this.$route.params.id
                axios
                    .patch(`/api/dict/computers/${computerID}/`, this.computer)
                    .then(response => {
                        toast({
                            message: 'แก้ไขข้อมูลเรียบร้อย',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push(`/dashboard/computers/${computerID}`)
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },

        }
    }
</script>