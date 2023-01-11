<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <!-- <h2 class="title">Computers RTAF    :{{personal.department}} </h2> -->
                <!-- <h2 class="title">ข้อมูลของ :{{personal.rank}} {{ personal.first_name }} {{personal.last_name}} </h2> -->

                <div class="buttons">
                    <!-- <h1 class="title">{{ team.team_name }}</h1> -->

                    <router-link :to="{ name: 'EditComputer', param: { id: computer.id }}" class="button is-light">แก้ไข</router-link>
                    <!-- <router-link to="/" class="button is-light">แก้ไข</router-link> -->
                    <!-- <button @click="convertToClient" class="button is-info">Convert to client</button> -->
                    <!-- <button @click="deletePersonal" class="button is-danger">ลบ</button> -->
                </div>
            </div>

            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle" is-info>Details</h2>

                    <!-- <template v-if="personal.assigned_to">
                        <p><strong>Assigned to: </strong>{{ personal.assigned_to.first_name }} {{ personal.assigned_to.last_name }}</p>
                    </template> -->
                    <p><strong>Status: </strong>{{ computer.status_computer }}</p>
                    <p><strong>สถานที่ติดตั้งอุปกรณ์           : </strong>{{ computer.computer_install_place }}</p>
                    <p><strong>ชนิดคอมพิวเตอร์           : </strong>{{ computer.computer_type }}</p>
                    <p><strong>ชื่อคอมพิวเตอร์       : </strong>{{ computer.computer_name }}</p>
                    <p><strong>ยี่ห้อของอุปกรณ์ : </strong>{{ computer.computer_brand }}</p>
                    <p><strong>รุ่นของอุปกรณ์  : </strong>{{ computer.computer_series }}</p>
                    <p><strong>หมายเลขพัสดุ ทอ.  : </strong>{{ computer.computer_number_rtaf }}</p>
                    <p><strong>Serial number  : </strong>{{ computer.computer_series_number }}</p>
                    <p><strong>MAC Address  : </strong>{{ computer.computer_mac_address }}</p>
                    <p><strong>เครื่องข่ายที่ใช้(ภายใน ทอ./ภายนอก ทอ.)  : </strong>{{ computer.computer_use_network }}</p>
                    <p><strong>คอมพิวเตอร์จากโครงการ  : </strong>{{ computer.computer_acquisition }}</p>
                    <p><strong>คอมพิวเตอร์ปีที่ติดตั้ง  : </strong>{{ computer.computer_start_use_year }}</p>
                    <p><strong>ผู้รับผิดชอบ  : </strong>{{ computer.person_responsible }}</p>
                    <p><strong>โทรศัพท์ติดต่อผู้ที่รับผิดชอบเครื่อง   : </strong>{{ computer.person_responsible_phone }}</p>
                </div>
            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle" is-info>อุปกรณ์ภายใน </h2>
                    <p><strong>ยี่ห้อ CPU  : </strong>{{ computer.cpu_brand }}</p>
                    <p><strong>รุ่น CPU  : </strong>{{ computer.cpu_model }}</p>
                    <p><strong>ความเร็วสัญญาณนาฬิกา  : </strong>{{ computer.cpu_speed_clock }}</p>
                    <p><strong>หน่วยความเร็วสัญญาณนาฬิกา  : </strong>{{ computer.cpu_unit_speed_clock }}</p>
                    <p><strong>ประเภทของ RAM           : </strong>{{ computer.ram_type }}</p>
                    <p><strong>ความจุของ RAM        : </strong>{{ computer.ram_capacity }}</p>
                    <p><strong>หน่วยความจุของ RAM    : </strong>{{ computer.email_public }}</p>
                    <p><strong>ประเภท Harddisk Primary : </strong>{{ computer.harddisk_type_1 }}</p>
                    <p><strong>ความจุของ Harddisk Primary : </strong>{{ computer.harddisk_capacity_1 }}</p>
                    <p><strong>หน่วยความจุของ Harddisk Primary : </strong>{{ computer.harddisk_unit_1 }}</p>
                    <p><strong>ประเภท Harddisk Secondary : </strong>{{ computer.harddisk_type_2 }}</p>
                    <p><strong>ความจุของ Harddisk Secondary : </strong>{{ computer.harddisk_capacity_2 }}</p>
                    <p><strong>หน่วยความจุของ Harddisk Secondary : </strong>{{ computer.harddisk_unit_2 }}</p>
                </div>
            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Software ในอุปกรณ์</h2>
                    <p><strong>ชื่อระบบปฏิบัติการ  : </strong>{{ computer.os_computer }}</p>
                    <p><strong>ลิขสิทธิ์ของระบบปฏิบัติการ  : </strong>{{ computer.os_copyright }}</p>
                    <p><strong>ชื่อโปรแกรมสำนักงาน  : </strong>{{ computer.office_name }}</p>
                    <p><strong>รุ่นปีโปรแกรมสำนักงาน  : </strong>{{ computer.office_model_year }}</p>
                    <p><strong>ลิขสิทธิ์ของโปรแกรมสำนักงาน  : </strong>{{ computer.office_copyright }}</p>
                    <p><strong>ชื่อโปรแกรมป้องกันไวรัส  : </strong>{{ computer.antivirus_name }}</p>
                    <p><strong>ลิขสิทธิ์ของโปรแกรมป้องกันไวรัส  : </strong>{{ computer.antivirus_copyright }}</p>
                    <p><strong>หมายเหตุ  : </strong>{{ computer.note }}</p>
                    <p><strong>ผู้บันทึกข้อมูล       : </strong>{{ $store.state.user.username }}</p>
                </div>
            </div>
        </div>
            <!-- <hr> -->
        <div class="columns is-multiline is-mobile">
            <div class="column is-12">
                <h2 class="subtitle" >Update Status Computer</h2>
            <!-- </div> -->
            <router-link :to="{ name: 'AddUpgradeComputer', param: { id: computer.id }}" class="button is-success mt-6">Add Update Status Computer</router-link>
                <div class="columns is-12">
                    <div
                        class="box"
                        v-for="upgradecomputer in upgradecomputers"
                        v-bind:key="upgradecomputer.id"
                        >
                        <h3 class="is-size-4">{{ upgradecomputer.computer_install_place }}</h3>
                        <p>
                            {{ upgradecomputer.computer_upgrade_year }}                   

                        </p>
                        <p>
                            {{ upgradecomputer.created_at }} 
                        </p>
                        <!-- <router-link :to="{ name: 'EditNote', params: { id: client.id, note_id: note.id }}" class="button is-success mb-6">Edit Note</router-link> -->
                        <div class="column">
                            <div class="box">
                                <h2 class="subtitle" is-info>Details</h2>

                                <!-- <template v-if="personal.assigned_to">
                                    <p><strong>Assigned to: </strong>{{ personal.assigned_to.first_name }} {{ personal.assigned_to.last_name }}</p>
                                </template> -->
                                <p><strong>Status: </strong>{{ computer.status_computer }}</p>
                                <p><strong>สถานที่ติดตั้งอุปกรณ์           : </strong>{{ upgradecomputer.computer_install_place }}</p>
                                <p><strong>ชื่อคอมพิวเตอร์       : </strong>{{ upgradecomputer.computer_name }}</p>
                                <!-- <p><strong>เครื่องข่ายที่ใช้(ภายใน ทอ./ภายนอก ทอ.)  : </strong>{{ upgradecomputer.computer_use_network }}</p>
                                <p><strong>ผู้รับผิดชอบ  : </strong>{{ upgradecomputer.person_responsible }}</p>
                                <p><strong>โทรศัพท์ติดต่อผู้ที่รับผิดชอบเครื่อง   : </strong>{{ upgradecomputer.person_responsible_phone }}</p> -->
                            </div>
                        </div>
                        <!-- <div class="column">
                            <div class="box">
                                <h2 class="subtitle" is-info>อุปกรณ์ภายใน </h2>
                                <p><strong>ยี่ห้อ CPU  : </strong>{{ upgradecomputer.cpu_brand }}</p>
                                <p><strong>รุ่น CPU  : </strong>{{ upgradecomputer.cpu_model }}</p>
                                <p><strong>ความเร็วสัญญาณนาฬิกา  : </strong>{{ upgradecomputer.cpu_speed_clock }}</p>
                                <p><strong>หน่วยความเร็วสัญญาณนาฬิกา  : </strong>{{ upgradecomputer.cpu_unit_speed_clock }}</p>
                                <p><strong>ประเภทของ RAM           : </strong>{{ upgradecomputer.ram_type }}</p>
                                <p><strong>ความจุของ RAM        : </strong>{{ upgradecomputer.ram_capacity }}</p>
                                <p><strong>หน่วยความจุของ RAM    : </strong>{{ upgradecomputer.email_public }}</p>
                                <p><strong>ประเภท Harddisk Primary : </strong>{{ upgradecomputer.harddisk_type_1 }}</p>
                                <p><strong>ความจุของ Harddisk Primary : </strong>{{ upgradecomputer.harddisk_capacity_1 }}</p>
                                <p><strong>หน่วยความจุของ Harddisk Primary : </strong>{{ upgradecomputer.harddisk_unit_1 }}</p>
                                <p><strong>ประเภท Harddisk Secondary : </strong>{{ upgradecomputer.harddisk_type_2 }}</p>
                                <p><strong>ความจุของ Harddisk Secondary : </strong>{{ upgradecomputer.harddisk_capacity_2 }}</p>
                                <p><strong>หน่วยความจุของ Harddisk Secondary : </strong>{{ upgradecomputer.harddisk_unit_2 }}</p>
                            </div>
                        </div>
                        <div class="column">
                            <div class="box">
                                <h2 class="subtitle">Software ในอุปกรณ์</h2>
                                <p><strong>ชื่อระบบปฏิบัติการ  : </strong>{{ computer.os_computer }}</p>
                                <p><strong>ลิขสิทธิ์ของระบบปฏิบัติการ  : </strong>{{ computer.os_copyright }}</p>
                                <p><strong>ชื่อโปรแกรมสำนักงาน  : </strong>{{ computer.office_name }}</p>
                                <p><strong>รุ่นปีโปรแกรมสำนักงาน  : </strong>{{ computer.office_model_year }}</p>
                                <p><strong>ลิขสิทธิ์ของโปรแกรมสำนักงาน  : </strong>{{ computer.office_copyright }}</p>
                                <p><strong>ชื่อโปรแกรมป้องกันไวรัส  : </strong>{{ computer.antivirus_name }}</p>
                                <p><strong>ลิขสิทธิ์ของโปรแกรมป้องกันไวรัส  : </strong>{{ computer.computer_acquisition }}</p>
                                <p><strong>หมายเหตุ  : </strong>{{ computer.note }}</p>
                                <p><strong>ผู้บันทึกข้อมูล       : </strong>{{ $store.state.user.username }}</p>
                            </div>
                        </div> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
                          
<script>
    import axios from 'axios'
    export default {
        name: 'Computer',
        data() {
            return {
                computer: {},
                upgradecomputers: [],
            }
        },
        mounted() {
            this.getComputer()
        },
        methods: {
            // async deleteComputer() {
            //     this.$store.commit('setIsLoading', true)
            //     const computerID = this.$route.params.id
            //     await axios
            //         .post(`/api/dict/leads/delete_lead/${computerID}/`)
            //         .then(response => {
            //             console.log(response.data)
            //             this.$router.push('/dashboard/computers')
            //         })
            //         .catch(error => {
            //             console.log(error)
            //         })
            //     this.$store.commit('setIsLoading', false)
            // },
            async getComputer() {
                this.$store.commit('setIsLoading', true)
                const computerID = this.$route.params.id
                await axios
                    .get(`/api/dict/computers/${computerID}/`)
                    .then(response => {
                        this.computer = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                await axios
                    .get(`/api/dict/upgradecomputers/?computer_id=${computerID}`)
                    .then(response => {
                        this.upgradecomputers = response.data
                    })

                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            // async convertToClient() {
            //     this.$store.commit('setIsLoading', true)
            //     const leadID = this.$route.params.id
            //     const data = {
            //         lead_id: leadID
            //     }
            //     await axios
            //         .post(`/api/v1/convert_lead_to_client/`, data)
            //         .then(response => {
            //             console.log('converted to client')
            //             this.$router.push('/dashboard/clients')
            //         })
            //         .catch(error => {
            //             console.log(error)
            //         })
            //     this.$store.commit('setIsLoading', false)
            // }
        }
    }
</script>