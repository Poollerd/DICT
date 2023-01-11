<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-8 is-offset-2">
                <h1 class="title">+ นายทหารเทคโนโลยีสารสนเทศและสงครามอิเล็คทรอนิกส์</h1>
            </div>

            <div class="column is-half is-offset-one-quarter">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>ยศ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="rank">
                        </div>
                    </div>
 
                    <div class="field">
                        <label>ชื่อ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="first_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>นามสกุล</label>
                        <div class="control">
                            <input type="text" class="input" v-model="last_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>ตำแหน่ง</label>
                        <div class="control">
                            <input type="text" class="input" v-model="position">
                        </div>
                    </div>

                    <div class="field">
                        <label>mail ทอ.</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email_rtaf">
                        </div>
                    </div>

                    <div class="field">
                        <label>mail สาธารณะ</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email_public">
                        </div>
                    </div>

                    <div class="field">
                        <label>เบอร์โทรศัพท์เคลื่อนที่</label>
                        <div class="control">
                            <input type="text" class="input" v-model="mobile">
                        </div>
                    </div>

                    <div class="field">
                        <label>เบอร์โทรศัพท์ภายใน ทอ.</label>
                        <div class="control">
                            <input type="text" class="input" v-model="phone_rtaf">
                        </div>
                    </div>
                    <div class="field">
                        <label>สังกัด</label>
                        <div class="control">
                            <div class="select">
                                <select  v-model="department">
                                    <option value="สลก.ทอ.">สลก.ทอ.</option>
                                    <option value="สบ.ทอ.">สบ.ทอ.</option>
                                    <option value="กพ.ทอ.">กพ.ทอ.</option>
                                    <option value="ขว.ทอ.">ขว.ทอ.</option>
                                    <option value="ยก.ทอ.">ยก.ทอ.</option>
                                    <option value="กบ.ทอ.">กบ.ทอ.</option>
                                    <option value="กร.ทอ.">กร.ทอ.</option>
                                    <option value="ทสส.ทอ.">ทสส.ทอ.</option>
                                    <option value="ปช.ทอ.">ปช.ทอ.</option>
                                    <option value="กง.ทอ.">กง.ทอ.</option>
                                    <option value="สตน.ทอ.">สตน.ทอ.</option>
                                    <option value="สนภ.ทอ.">สนภ.ทอ.</option>
                                    <option value="สกบ.ทอ.">สกบ.ทอ.</option>
                                    <option value="สธน.ทอ.">สธน.ทอ.</option>
                                    <option value="ศซบ.ทอ.">ศซบ.ทอ.</option>
                                    <option value=">คปอ.">คปอ.</option>
                                    <option value="อย.">อย.</option>
                                    <option value="ศปวอ.">ศปวอ.</option>
                                    <option value="รร.การบิน">รร.การบิน</option>
                                    <option value="บน.๑">บน.๑</option>
                                    <option value="บน.๒">บน.๒</option>
                                    <option value="บน.๓">บน.๓</option>
                                    <option value="บน.๔">บน.๔</option>
                                    <option value="บน.๕">บน.๕</option>
                                    <option value="บน.๖">บน.๖</option>
                                    <option value="บน.๗">บน.๗</option>
                                    <option value="บน.๒๑">บน.๒๑</option>
                                    <option value="บน.๒๓">บน.๒๓</option>
                                    <option value="บน.๔๑">บน.๔๑</option>
                                    <option value="บน.๔๖">บน.๔๖</option>
                                    <option value="บน.๕๖">บน.๕๖</option>
                                    <option value="ชอ">ชอ.</option>
                                    <option value="สอ.ทอ.">สอ.ทอ.</option>
                                    <option value="สพ.ทอ.">สพ.ทอ.</option>
                                    <option value="พ.ทอ.">พ.ทอ.</option>
                                    <option value="พ.ทอ.(รพ.ภูมิพลฯ)">พ.ทอ.(รพ.ภูมิพลฯ)</option>
                                    <option value="พ.ทอ.(รพ.จันทรุเบกษา)">พ.ทอ.(รพ.จันทรุเบกษา)</option>
                                    <option value="พ.ทอ.(รพ.ทหารอากาศ(สีกัน))">พ.ทอ.(รพ.ทหารอากาศ(สีกัน))</option>
                                    <option value="พธ.ทอ.">พธ.ทอ.</option>
                                    <option value="ชย.ทอ.">ชย.ทอ.</option>
                                    <option value="ขส.ทอ.">ขส.ทอ.</option>
                                    <option value="ศซว.ทอ.">ศซว.ทอ.</option>
                                    <option value="ยศ.ทอ">ยศ.ทอ.</option>
                                    <option value="ยศ.ทอ.(วิทยาลัยการทัพอากาศ)">ยศ.ทอ.(วิทยาลัยการทัพอากาศ)</option>
                                    <option value="ยศ.ทอ.(รร.เสนาธิการทหารอากาศ)">ยศ.ทอ.(รร.เสนาธิการทหารอากาศ)</option>
                                    <option value="ยศ.ทอ.(รร.นายทหารอากาศอาวุโส)">ยศ.ทอ.(รร.นายทหารอากาศอาวุโส)</option>
                                    <option value="ยศ.ทอ.(รร.นายทหารชั้นผู้บังคับฝูง)">ยศ.ทอ.(รร.นายทหารชั้นผู้บังคับฝูง)</option>
                                    <option value="ยศ.ทอ.(รร.นายทหารชั้นผู้บังคับหมวด)">ยศ.ทอ.(รร.นายทหารชั้นผู้บังคับหมวด)</option>
                                    <option value="ยศ.ทอ.(รร.ครูทหาร)">ยศ.ทอ.(รร.ครูทหาร)</option>
                                    <option value="ยศ.ทอ.(รร.นายทหารชั้นประทวน)">ยศ.ทอ.(รร.นายทหารชั้นประทวน)</option>
                                    <option value="ยศ.ทอ.(รร.จ่าอากาศ)">ยศ.ทอ.(รร.จ่าอากาศ)</option>
                                    <option value="ยศ.ทอ.(ศูนย์ภาษา)">ยศ.ทอ.(ศูนย์ภาษา)</option>
                                    <option value="ยศ.ทอ.(ศูนย์ทดสอบบุคคล)">ยศ.ทอ.(ศูนย์ทดสอบบุคคล)</option>
                                    <option value="ยศ.ทอ.(กองวิทยบริการ)">ยศ.ทอ.(กองวิทยบริการ)</option>
                                    <option value="ยศ.ทอ.(กองอนุศาสนาจารย์)">ยศ.ทอ.(กองอนุศาสนาจารย์)</option>
                                    <option value="ศวอ.">ศวอ.</option>
                                    <option value="สก.ทอ.">สก.ทอ.</option>
                                    <option value="ผบ.สน.ดม.">ผบ.สน.ดม.</option>
                                    <option value="สวบ.ทอ.">สวบ.ทอ.</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>สถานะ</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="status">
                                    <option value="active">Active</option>
                                    <option value="inactive">In Active</option>
                                </select>
                            </div>
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

        name: 'AddPersonal',

        data() {
            return {
                rank: '',
                first_name: '',
                last_name: '',
                position: '',
                email_rtaf: '',
                email_public: '',
                mobile: '',
                phone_rtaf: '',
                department: '--',
                status: 'active',
            }
        },

        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const personal = {
                    rank: this.rank,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    position: this.position,
                    email_rtaf: this.email_rtaf,
                    email_public: this.email_public,
                    mobile: this.mobile,
                    phone_rtaf: this.phone_rtaf,
                    department: this.department,
                    status: this.status,
                }
                await axios
                    .post('/api/dict/personals/', personal)
                    .then(response => {
                        toast({
                            message: 'เพิ่มข้อมูลเรียบร้อย',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/dashboard/personals')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>