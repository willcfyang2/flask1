<template>
    <el-form :model="form" status-icon :rules="rules" ref="form" label-width="100px" class="login-container">
        <h3 class="login_title">system login view</h3>
        <el-form-item label="username" label-width="80px" prop="username" class="username">
            <el-input type="input" v-model='form.username' autocomplete="off" placeholder="please enter your username"></el-input>
        </el-form-item>
        <el-form-item label="password" label-width="80px" prop="password" class="username">
            <el-input type="password" v-model="form.password" autocomplete="off" placeholder="please enter your password"></el-input>
        </el-form-item>
        <el-form-item class="login_submit">
            <el-button type="primary" @click="login" class="login_submit">login</el-button>
            <el-button type="primary" @click="to_register" class="login_submit">register</el-button>
            
        </el-form-item>

    </el-form>
</template>

<script>
import axios from 'axios'

export default {
    name: 'login',
    data() {
        return {
            form: {

            },
            rules: {
              username: [
                  {required: true, message: 'please enter your username', tigger: 'blur'},
                  {

                      tigger: "blur"
                  }
              ],
              password: [
                  {required: true, message:'please enter your password', tigger: "blur"}
              ]
            }
        }
    },
    methods:{
        login(){
            let api = 'api/user/login'
            const data = `username=${this.form.username}&password=${this.form.password}`
            // data = {username: this.form.username, password: this.form.password}
            axios.post(api, data).then(res =>{
                if(res.data.status == 200){
                    let user_id = res.data.data.id
                    let user_status = res.data.data.status
                    let email = res.data.data.email
                    const data = user_id
                    this.$store.commit('setToken', data)
                    this.$router.push('/')
                    }
                else{
                    alert('username or password error')
                }
 
        })

            // this.$store.commit('setToken', token)
        },
        to_register(){
            this.$router.push('/register')
        }
    }
}
</script>

<style lang="less" scoped>
.login-container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px 15px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6ca;
}

.login_title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
}

.login_submit {
    margin: 10px auto 0px auto;
}



</style>