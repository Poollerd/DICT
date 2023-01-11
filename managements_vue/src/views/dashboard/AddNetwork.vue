<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-8 is-offset-2">
                <h1 class="title">+ ข้อมูล Network </h1>
            </div>
           
            <div class="column is-half is-offset-one-quarter">
                <form @submit.prevent="submitForm">
                    
                    <div class="field">
                        <label>สถานที่ติดตั้ง</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_install_place">
                        </div>
                    </div>
        
                    <div class="field">
                        <label>ชนิดอุปกรณ์เครือข่าย</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_type">
                        </div>
                    </div>
                    <div class="field">
                        <label>ยี่ห้ออุปกรณ์เครือข่าย</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_brand">
                        </div>
                    </div>
                    <div class="field">
                        <label>ชื่อ/รุ่นอุปกรณ์เครือข่าย</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>รุ่นเครือข่าย</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_version">
                        </div>
                    </div>
                    <div class="field">
                        <label>ชื่อระบบเครือข่าย</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_name_in_system">
                        </div>
                    </div>
                    <!-- <div class="field">
                        <label>ยี่ห้อของอุปกรณ์</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="computer_brand">
                                    <option value="Handmake">Handmake</option>
                                    <option value="Acer">Acer</option>
                                    <option value="Hp">Hp</option>
                                    <option value="SVOA">SVOA</option>
                                    <option value="Lenovo">Lenovo</option>
                                </select>
                            </div>
                        </div>
                    </div> -->
        
                    <div class="field">
                        <label>MAC Address</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_mac_address">
                        </div>
                    </div>
                    <div class="field">
                        <label>IP Address</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_ip_address">
                        </div>
                    </div>
      
                    <div class="field">
                        <label>ที่มาของอุปกรณ์(โครงการ/หน่วยจัดหา/ส่วนตัว)</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_got">
                        </div>
                    </div>
                    <div class="field">
                        <label>Serial Number</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_serial_number">
                        </div>
                    </div>
                    <div class="field">
                        <label>ผู้รับผิดชอบ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_person_responsible">
                        </div>
                    </div>
                    <div class="field">
                        <label>เบอร์โทรศัพท์ติดต่อ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="network_person_responsible_phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>สถานะเครือข่าย</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="network_status">
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
                            <input type="text" class="input" v-model="network_note">
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

        name: 'AddNetwork',

        data() {
            return {
                network_install_place: '',
                network_type: '',
                network_brand: '',
                network_name: '',
                network_version: '',
                network_name_in_system: '',
                network_mac_address: '',
                network_ip_address: '',
                network_got: '',
                network_serial_number: '',
                network_person_responsible: '',
                network_person_responsible_phone: '',
                network_status: '',
                network_note: '',

            }
        },
       
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const network = {
                    network_install_place: this.network_install_place,
                    network_type: this.network_type,
                    network_brand: this.network_brand,
                    network_name: this.network_name,
                    network_version: this.network_version,
                    network_name_in_system: this.network_name_in_system,
                    network_mac_address: this.network_mac_address,
                    network_ip_address: this.network_ip_address,
                    network_got: this.network_got,
                    network_serial_number: this.network_serial_number,
                    network_person_responsible: this.network_person_responsible,
                    network_person_responsible_phone: this.network_person_responsible_phone,
                    network_status: this.network_status,
                    network_note: this.network_note,
                }
                await axios
                    .post('/api/dict/networks/', network)
                    .then(response => {
                        toast({
                            message: 'เพิ่มข้อมูลเรียบร้อย',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/dashboard/networks')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>