<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="title">สังกัด    :{{personal.department}} </h2>
                <h2 class="title">ข้อมูลของ :{{personal.rank}} {{ personal.first_name }} {{personal.last_name}} </h2>

                <div class="buttons">
                    <router-link :to="{ name: 'EditPersonal', param: { id: personal.id }}" class="button is-light">แก้ไข</router-link>
                    <!-- <router-link to="/" class="button is-light">แก้ไข</router-link> -->
                    <!-- <button @click="convertToClient" class="button is-info">Convert to client</button> -->
                    <!-- <button @click="deletePersonal" class="button is-danger">ลบ</button> -->
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle" is-info>Details</h2>
                    <p><strong>Status: </strong>{{ personal.status }}</p>
                    <p><strong>ยศ           : </strong>{{ personal.rank }}</p>
                    <p><strong>ชื่อ           : </strong>{{ personal.first_name }}</p>
                    <p><strong>นามสกุล       : </strong>{{ personal.last_name }}</p>
                    <p><strong>Created at   : </strong>{{ personal.created_at }}</p>
                    <p><strong>Modified at  : </strong>{{ personal.modified_at }}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>

                    <p><strong>ตำแหน่ง           : </strong>{{ personal.position }}</p>
                    <p><strong>Email ทอ.        : </strong>{{ personal.email_rtaf }}</p>
                    <p><strong>Email สาธารณะ    : </strong>{{ personal.email_public }}</p>
                    <p><strong>เบอร์โทรศัพท์เคลื่อนที่ : </strong>{{ personal.mobile }}</p>
                    <p><strong>เบอร์โทรศัพท์ภายใน  : </strong>{{ personal.phone_rtaf }}</p>
                    <p><strong>เบอร์โทรศัพท์ภายใน  : </strong>{{ personal.department }}</p>
                    <p><strong>ผู้บันทึกข้อมูล       : </strong>{{ $store.state.user.username }}</p>
                </div>
            </div>
        </div>
        <!-- <div class="columns is-multiline is-mobile">
            <div class="column is-12">
                <h2 class="subtitle" >Update Status Computer</h2>
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
                        <div class="column is-12">
                            <div class="box">
                                <h2 class="subtitle" is-info>Details</h2>
                                <p><strong>Status: </strong>{{ computer.status_computer }}</p>
                                <p><strong>สถานที่ติดตั้งอุปกรณ์           : </strong>{{ upgradecomputer.computer_install_place }}</p>
                                <p><strong>ชื่อคอมพิวเตอร์       : </strong>{{ upgradecomputer.computer_name }}</p>
                                <p><strong>เครื่องข่ายที่ใช้(ภายใน ทอ./ภายนอก ทอ.)  : </strong>{{ upgradecomputer.computer_use_network }}</p>
                                <p><strong>ผู้รับผิดชอบ  : </strong>{{ upgradecomputer.person_responsible }}</p>
                                <p><strong>โทรศัพท์ติดต่อผู้ที่รับผิดชอบเครื่อง   : </strong>{{ upgradecomputer.person_responsible_phone }}</p>
                            </div>
                        </div>
                        <div class="column is-12">
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
                        <div class="column is-12">
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
                        </div>
                    </div>
                </div>
            </div>
        </div> -->
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Personal',
        data() {
            return {
                personal: {},
                // upgradecomputers: [],

            }
        },
        mounted() {
            this.getPersonal()
        },
        methods: {
            // async deletePersonal() {
            //     this.$store.commit('setIsLoading', true)
            //     const personalID = this.$route.params.id
            //     await axios
            //         .post(`/api/dict/personals/delete_personal/${personalID}/`)
            //         .then(response => {
            //             console.log(response.data)
            //             this.$router.push('/dashboard/personals')
            //         })
            //         .catch(error => {
            //             console.log(error)
            //         })
            //     this.$store.commit('setIsLoading', false)
            // },
            async getPersonal() {
                this.$store.commit('setIsLoading', true)
                const personalID = this.$route.params.id
                await axios
                    .get(`/api/dict/personals/${personalID}/`)
                    .then(response => {
                        this.personal = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                    // await axios
                    // .get(`/api/dict/upgradecomputers/?computer_id=${computerID}`)
                    // .then(response => {
                    //     this.upgradecomputers = response.data
                    // })

                    // .catch(error => {
                    //     console.log(error)
                    // })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>