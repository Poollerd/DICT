<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-8 is-offset-2">
                <h1 class="title">+ ข้อมูล Computer </h1>
            </div>
           
            <!-- <div class="column is-half is-offset-one-quarter"> -->
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                        <div class="field">
                            <label>สถานที่ติดตั้ง</label>
                            <div class="control">
                                <input type="text" class="input" v-model="computer_install_place">
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
                                    <select v-model="computer_type">
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
                                <input type="text" class="input" v-model="computer_name">
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
                                    <select v-model="computer_brand">
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
                                <input type="text" class="input" v-model="computer_series">
                            </div>
                        </div>
                        <div class="field">
                            <label>หมายเลขพัสดุ ทอ.</label>
                            <div class="control">
                                <input type="text" class="input" v-model="computer_number_rtaf">
                            </div>
                        </div>
                        <div class="field">
                            <label>Serial number</label>
                            <div class="control">
                                <input type="text" class="input" v-model="computer_series_number">
                            </div>
                        </div>
                        <div class="field">
                            <label>ยี่ห้อ CPU</label>
                            <div class="control">
                                <input type="text" class="input" v-model="cpu_brand">
                            </div>
                        </div>
                        <div class="field">
                            <label>รุ่น CPU</label>
                            <div class="control">
                                <input type="text" class="input" v-model="cpu_model">
                            </div>
                        </div>
                        <div class="field">
                            <label>ความเร็วสัญญาณนาฬิกา</label>
                            <div class="control">
                                <input type="text" class="input" v-model="cpu_speed_clock">
                            </div>
                        </div>
                        <div class="field">
                            <label>หน่วยความเร็วสัญญาณนาฬิกา</label>
                            <div class="control">
                                <input type="text" class="input" v-model="cpu_unit_speed_clock">
                            </div>
                        </div>
                        <div class="field">
                            <label>MAC Address</label>
                            <div class="control">
                                <input type="text" class="input" v-model="computer_mac_address">
                            </div>
                        </div>
                        <div class="field">
                            <label>เครื่องข่ายที่ใช้(ภายใน ทอ./ภายนอก ทอ.)</label>
                            <div class="control">
                                <input type="text" class="input" v-model="computer_use_network">
                            </div>
                        </div>
                        <div class="field">
                            <label>ประเภทของ RAM</label>
                            <div class="control">
                                <input type="text" class="input" v-model="ram_type">
                            </div>
                        </div>
                        <div class="field">
                            <label>ความจุของ RAM</label>
                            <div class="control">
                                <input type="text" class="input" v-model="ram_capacity">
                            </div>
                        </div>

                        <div class="field">
                            <label>หน่วยความจุของ RAM</label>
                            <div class="control">
                                <input type="text" class="input" v-model="ram_unit_capacity">
                            </div>
                        </div>
                        <div class="field">
                            <label>ประเภท Harddisk Primary</label>
                            <div class="control">
                                <input type="text" class="input" v-model="harddisk_type_1">
                            </div>
                        </div>
                        <div class="field">
                            <label>ความจุของ Harddisk Primary</label>
                            <div class="control">
                                <input type="text" class="input" v-model="harddisk_capacity_1">
                            </div>
                        </div>
                        <div class="field">
                            <label>หน่วยความจุของ Harddisk Primary</label>
                            <div class="control">
                                <input type="text" class="input" v-model="harddisk_unit_1">
                            </div>
                        </div>
                        <div class="field">
                            <label>ประเภท Harddisk Secondary</label>
                            <div class="control">
                                <input type="text" class="input" v-model="harddisk_type_2">
                            </div>
                        </div>
                        <div class="field">
                            <label>ความจุของ Harddisk Secondary</label>
                            <div class="control">
                                <input type="text" class="input" v-model="harddisk_capacity_2">
                            </div>
                        </div>
                        <div class="field">
                            <label>หน่วยความจุของ Harddisk Secondary</label>
                            <div class="control">
                                <input type="text" class="input" v-model="harddisk_unit_2">
                            </div>
                        </div>
                        <div class="field">
                            <label>ชื่อระบบปฏิบัติการ</label>
                            <div class="control">
                                <input type="text" class="input" v-model="os_computer">
                            </div>
                        </div>
                        <div class="field">
                            <label>ลิขสิทธิ์ของระบบปฏิบัติการ</label>
                            <div class="control">
                                <input type="text" class="input" v-model="os_copyright">
                            </div>
                        </div>
                        <div class="field">
                            <label>ชื่อโปรแกรมสำนักงาน</label>
                            <div class="control">
                                <input type="text" class="input" v-model="office_name">
                            </div>
                        </div>
                        <div class="field">
                            <label>รุ่นปีของโปรแกรมสำนักงาน</label>
                            <div class="control">
                                <input type="text" class="input" v-model="office_model_year">
                            </div>
                        </div>
                        <div class="field">
                            <label>ลิขสิทธิ์ของโปรแกรมสำนักงาน</label>
                            <div class="control">
                                <input type="text" class="input" v-model="office_copyright">
                            </div>
                        </div>
                        <div class="field">
                            <label>ชื่อโปรแกรมป้องกันไวรัส</label>
                            <div class="control">
                                <input type="text" class="input" v-model="antivirus_name">
                            </div>
                        </div>
                        <div class="field">
                            <label>ลิขสิทธิ์ของโปรแกรมป้องกันไวรัส</label>
                            <div class="control">
                                <input type="text" class="input" v-model="antivirus_copyright">
                            </div>
                        </div>
                        <div class="field">
                            <label>คอมพิวเตอร์จากโครงการ</label>
                            <div class="control">
                                <input type="text" class="input" v-model="computer_acquisition">
                            </div>
                        </div>
                        <div class="field">
                            <label>ปีที่ติดตั้ง</label>
                            <div class="control">
                                <input type="text" class="input" v-model="computer_start_use_year">
                            </div>
                        </div>
                        <div class="field">
                            <label>ผู้รับผิดชอบ</label>
                            <div class="control">
                                <input type="text" class="input" v-model="person_responsible">
                            </div>
                        </div>
                        <div class="field">
                            <label>โทรศัพท์ติดต่อผู้ที่รับผิดชอบเครื่อง</label>
                            <div class="control">
                                <input type="text" class="input" v-model="person_responsible_phone">
                            </div>
                        </div>

                        <div class="field">
                            <label>สถานะเครื่องคอมพิวเตอร์</label>
                            <div class="control">
                                <div class="select">
                                    <select v-model="status_computer">
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
                                <input type="text" class="input" v-model="note">
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

        name: 'AddComputer',

        data() {
            return {
                computer_install_place: '',
                computer_type: 'PC',
                computer_name: '',
                computer_brand: 'Handmake',
                computer_series: '',
                computer_number_rtaf: '',
                computer_series_number: '',
                cpu_brand: '',
                cpu_model: '',
                cpu_speed_clock: '',
                cpu_unit_speed_clock: '',
                computer_mac_address: '',
                computer_use_network: '',
                ram_type: '',
                ram_capacity: '',
                ram_unit_capacity: '',
                harddisk_type_1: '',
                harddisk_capacity_1: '',
                harddisk_unit_1: '',
                harddisk_type_2: '',
                harddisk_capacity_2: '',
                harddisk_unit_2: '',
                os_computer: '',
                os_copyright: '',
                office_name: '',
                office_model_year: '',
                office_copyright: '',
                antivirus_name: '',
                antivirus_copyright: '',
                computer_acquisition: '',
                computer_start_use_year: '',
                person_responsible: '',
                person_responsible_phone: '',
                status_computer: 'ใช้ราชการ',
                note: '',


            }
        },

        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const computer = {
                    computer_install_place: this.computer_install_place,
                    computer_type: this.computer_type,
                    computer_name: this.computer_name,
                    computer_brand: this.computer_brand,
                    computer_series: this.computer_series,
                    computer_number_rtaf: this.computer_number_rtaf,
                    computer_series_number: this.computer_series_number,
                    cpu_brand: this.cpu_brand,
                    cpu_model: this.cpu_model,
                    cpu_speed_clock: this.cpu_speed_clock,
                    cpu_unit_speed_clock: this.cpu_unit_speed_clock,
                    computer_mac_address: this.computer_mac_address,
                    computer_use_network: this.computer_use_network,
                    ram_type: this.ram_type,
                    ram_capacity: this.ram_capacity,
                    ram_unit_capacity: this.ram_unit_capacity,
                    harddisk_type_1: this.harddisk_type_1,
                    harddisk_capacity_1: this.harddisk_capacity_1,
                    harddisk_unit_1: this.harddisk_unit_1,
                    harddisk_type_2: this.harddisk_type_2,
                    harddisk_capacity_2: this.harddisk_capacity_2,
                    harddisk_unit_2: this.harddisk_unit_2,
                    os_computer: this.os_computer,
                    os_copyright: this.os_copyright,
                    office_name: this.office_name,
                    office_model_year: this.office_model_year,
                    office_copyright: this.office_copyright,
                    antivirus_name: this.antivirus_name,
                    antivirus_copyright: this.antivirus_copyright,
                    computer_acquisition: this.computer_acquisition,
                    computer_start_use_year: this.computer_start_use_year,
                    person_responsible: this.person_responsible,
                    person_responsible_phone: this.person_responsible_phone,
                    status_computer: this.status_computer,
                    note: this.note,
                }
                await axios
                    .post('/api/dict/computers/', computer)
                    .then(response => {
                        toast({
                            message: 'เพิ่มข้อมูลเรียบร้อย',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/dashboard/computers')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>