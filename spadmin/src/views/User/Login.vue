<template>
    <div id='login'>
        <!-- ]<el-row>
            <el-col :span="24"><div></div></el-col>
        </el-row> -->
        <el-row type="flex" justify="center">
            <el-col :span="8">
                <div>
                    <el-card shadow="always">
                        <div slot="header">
                            <span sytle="text-align:center">SparePart Admin</span>
                        </div>
                        <el-form stauts-icon :rules="rules" label-position="left" label-width="80px" ref="form" :model="form">
                            <el-form-item label="用户名" prop="username">
                                <el-input v-model="form.username" autocomplete="off">abc</el-input>
                            </el-form-item>
                            <el-form-item label="密码" prop="password">
                                <el-input v-model="form.password" type="password" autocomplete="off">abc</el-input>
                            </el-form-item>
                            <!-- <el-form-item label="确认密码" prop="checkpassword">
                                <el-input v-model="form.checkpassword" type="password"></el-input>
                            </el-form-item> -->
                            <el-form-item >
                                <el-col :span="12">
                                    <el-button type="primary" @click="onLogin('form')" @keyup.enter="onLogin('form')">登录</el-button>
                                </el-col>
                                <!-- <el-col :span="8">
                                    <el-button type="primary" @click="onRegister">注册</el-button>
                                </el-col> -->
                                <el-col :span="12">
                                    <el-button @click="onReset('form')">重置</el-button>
                                </el-col>
                            </el-form-item>
                        </el-form>
                    </el-card>
                </div>
            </el-col>                         
        </el-row>
    </div>
</template>

<style scoped>
    #login {
        padding-top:10%;
    }
    #app {
        background-image: url('timg.jpg');
        background-repeat: no-repeat;
    }
</style>
<script>
import axios from "axios";
// import qs from 'qs';

// var data = qs.stringify();

export default {
    data(){
        var validateUsername = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入用户名'));
            } else {
                callback();
            }
        };
        var validatePassword = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                callback();
            }
        };
        return {
            form: {
                username: '',
                password: '',
            },
            rules: {
                password: [
                    { validator: validatePassword, trigger: 'blur' }
                ],
                username: [
                    { validator: validateUsername, trigger: 'blur' }
                ]
            }
        };
    },
    methods: {
        onLogin(formName) {
            var params = new URLSearchParams();
            var that = this;
            params.append('username', this.form.username);
            params.append('password', this.form.password);
            const path = "/api/login";
            console.log('login');
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    // alert('submit!');
                    axios.post(path, params).then(function (response) {
                        console.log(response.data);
                        if (response.data == 'invalidUser') {
                            that.$message({
                                message: "用户不存在，请确认用户名。",
                                type: 'warning'
                            })
                        }
                        if (response.data == 'invalidPassword') {
                            that.$message.error('密码错误，请确认密码！')
                        }
                        if (response.data == 'validUser') {
                            that.$router.push('/')
                        }
                    });
                } else {
                    console.log('error');
                    return false;
                }
            });
 
        },      // onRegister() {
        //     console.log('register');
        // },
        onReset(formName) {
            console.log(formName);
            // this.$nextTick(function(formName){
            //     this.$refs[formName].resetFields();
            // })
            // this.$nextTrick(()=>{
                this.$refs[formName].resetFields();
            // })
        }
    }
}
</script>
