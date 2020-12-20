<template>
  <div>
    <el-row>
        <el-col :span="24">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/' }">系统配置</el-breadcrumb-item>
                <el-breadcrumb-item>用户管理</el-breadcrumb-item>
            </el-breadcrumb>
        </el-col>
    </el-row>
    <el-row>
        <el-card>
            <div slot="header" style="display:flex; justify-content:space-between">
                <el-button style="float: right;" type="primary" @click="isVisible = true;isEdit = false;">新增用户</el-button>
            </div>
            <div>            
                <el-row type="flex" justify="center" v-loading="loading">
                    <el-table :data="tableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" stripe>
                        <el-table-column prop="uid" label="uid" width="100"></el-table-column>
                        <el-table-column prop="username" label="用户名" width="170"></el-table-column>
                        <el-table-column prop="email" label="电子邮件" width="170"></el-table-column>
                        <el-table-column prop="department" label="部门" width="170"></el-table-column>
                        <el-table-column prop="phone" label="电话号码" width="170"></el-table-column>
                        <el-table-column prop="create_time" label="创建时间" width="260"></el-table-column>
                        <el-table-column prop="op" label="操作" width="250">
                            <template slot-scope="scope">
                                <el-button type='primary' @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                                <el-button type='danger' @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>   
                </el-row>
                <el-row type="flex" justify="center">
                    <el-pagination
                        @size-change="hanldeSizeChange"
                        @current-change="handleCurrentChange"
                        :current-page="currentPage"
                        :page-sizes="[5, 15, 25, 50]"
                        :page-size="pageSize"
                        layout="total, sizes, prev, pager, next, jumper"
                        :total="tableData.length"
                    ></el-pagination>
                </el-row>
            </div>
        </el-card>
    </el-row>
    <div>
        <el-dialog title="" :visible.sync="isVisible" @close='closeUserDialog'>
            <el-form :model="userForm" ref="userForm" :rules="rules">            
                <el-form-item label="用户ID" prop="uid" :label-width="formLabelWidth" v-show="isEdit">
                    <el-input v-model="userForm.uid" autocomplete="off" :disabled="isEdit" v-show="isEdit"></el-input>
                </el-form-item>
                <el-form-item label="用户名" prop="username" :label-width="formLabelWidth">
                    <el-input v-model="userForm.username" autocomplete="off" :disabled="isEdit"></el-input>
                </el-form-item>
                <div v-show="!isEdit">
                    <el-form-item label="密码" prop="password" :label-width="formLabelWidth">
                        <el-input v-model="userForm.password" type="password" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="passwordConfirm" :label-width="formLabelWidth">
                        <el-input v-model="userForm.passwordConfirm" type="password" autocomplete="off"></el-input>
                    </el-form-item>
                </div>                
                <el-form-item label="电子邮件" prop="email" :label-width="formLabelWidth">
                    <el-input v-model="userForm.email" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="部门" prop="department" :label-width="formLabelWidth">
                    <el-input v-model="userForm.department" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="电话号码" prop="phone" :label-width="formLabelWidth">
                    <el-input v-model="userForm.phone" autocomplete="off" placeholder=""></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="handleDialogUserFormClose">取 消</el-button>
                <el-button type="primary" @click="handleDialogUserFormSubmit">确 定</el-button>
            </div>
        </el-dialog>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import qs from 'qs';
export default {
    data() {
        var validatorPass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('密码不能为空'));
            } else {
                if (this.userForm.passwordConfirm !== '') {
                    this.$refs.userForm.validateField('passwordConfirm');
                }
                callback();
            }
        };
        var validatePass2 = (rule, value, callback) => {
            if (value === '') {
            callback(new Error('请再次输入密码'));
            } else if (value !== this.userForm.password) {
            callback(new Error('两次输入密码不一致!'));
            } else {
            callback();
            }
        };
        // var validatorPassSame = (rule, value, callback) => {
        //     console.log('confirmpass')
        //     if (value === '') {
        //         callback(new Error('请再次输入密码'));
        //     } else if (value !== this.userForm.password) {
        //         callback(new Error('请确认密码是否一致'));
        //     } else {
        //         callback();
        //     }
        // };
        return {
            currentPage: 1,
            pageSize: 5,
            tableData: [],
            isVisible: false,
            isEdit: false,
            loading: true,
            userForm: {
                uid: '',
                username: '',
                password: '',
                passwordConfirm: '',
                email: '',
                department: '',
                phone: ''
            },
            rules: {
                password: [
                    {validator: validatorPass, trigger: 'blur'}
                ],
                passwordConfirm: [
                    {validator: validatePass2, trigger: 'blur'}
                ]
            },
            formLabelWidth: '120px'
        }
    },
    methods: {
        handleInitialData() {
            let that = this
            this.loading = true
            console.log("start-link")
            const path = "/api/user/get"
            axios.get(path).then(function(response){
                console.log(response.data)
                that.tableData = response.data
                that.loading = false
            })
        },
        handleCurrentChange(val) {
            console.log(val);
            this.currentPage = val
            console.log(this.currentPage)
        },
        hanldeSizeChange(val) {
            console.log(val);
            this.pageSize = val
            console.log(this.pageSize)
        },
        handleEdit(index, row) {
            this.isVisible = true;
            this.isEdit = true;
            this.$nextTick(() => {
                this.userForm['uid'] = row.uid;
                this.userForm['username'] = row.username;
                this.userForm['email'] = row.email;
                this.userForm['department'] = row.department;
                this.userForm['phone'] = row.phone;
            })
        },
        handleDelete(index, row) {
            console.log(row['department']);
            var uid = row['uid'];
            var username = row['username'];
            axios.get('/api/user/delete/' + uid).then(response => {
                var data = response.data
                console.log(data)
                this.$notify({
                    title: "删除用户结果",
                    message: "删除用户" + username + "成功",
                    type: "success"
                })
            });
        },
        handleDialogUserFormClose() {
            this.isVisible = false;
            this.$refs['userForm'].resetFields();
        },
        handleDialogUserFormSubmit() {
            var path = '';
            var datas = qs.stringify(this.userForm);
            if (this.isEdit) {
                path = '/api/user/modify';
            } else {
                path = '/api/user/insert';
            }
            this.$refs['userForm'].validate((valid) => function() {
                if (valid) {
                    axios.post(path, datas, {headers:{'Content-Type':'application/x-www-form-urlencoded'}}).then(() => {
                        if (this.isEdit) {
                            this.$notify({
                                title: "修改用户信息",
                                message: "修改用户" + this.userForm.username + "信息成功。",
                                type: "success"
                            })
                            this.isEdit = false;
                        } else {
                            this.$notify({
                                title: "新增用户",
                                message: "新增用户" + this.userForm.username + "成功。",
                                type: "success"
                            })
                        } 
                        this.isVisible = false;
                        this.handleInitialData();
                    }).finally(() => {
                        this.$refs['userForm'].resetFields();
                    });
                } else {
                    return false;
                }
                
            })
            
        },
        closeUserDialog() {
            this.$refs['userForm'].resetFields()
        }
    },
    mounted() {
        this.handleInitialData()
    }
};
</script>

<style>
    .el-row {
        margin-bottom: 20px;
    }
    .el-table td, .el-table th {
        text-align: center
    }
    .el-card__body {
        display: flex;
        align-content: center;
        justify-content: center;
    }
</style>