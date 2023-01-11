<template>
    <div class="contrainer">
        <div class="columns is-multiline">
            <div class="colume is-12">
                <h1 class="title">ปฏิบัติงานในหน่วยงาน</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>สังกัด</label>
                        <!-- <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                        <div class="field">
                        <label>Status</label> -->
                        <div class="control">
                            <div class="select">
                                <select  v-model="team_name">
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
                        <label>นขต.หน่วยงาน</label>
                        <div class="control">
                            <input type="text" class="input" v-model="subteam_name">
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

    import { toast} from 'bulma-toast'

    export default {

        name: 'AddTeam',

        data() {
            return {
                team_name: '--',
                subteam_name: '',
            }
        },

        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const team = {
                    team_name: this.team_name,
                    subteam_name: this.subteam_name,
                }
                await axios
                    .post('/api/dict/teams/', team)
                    .then(response => {
                        toast({
                            message: 'อยู่ในหน่วยงานที่จะปฏิบัติเรียบร้อย',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 3000,
                            position: 'bottom-right',
                            
                        })
                        console.log(response.data)
                        this.$store.commit('setTeam', {'teamid': response.data.id, 'team_name': this.team_name, 'subteam_name': this.subteam_name})
                        this.$router.push('/dashboard')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>

