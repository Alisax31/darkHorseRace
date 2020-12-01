<template>
  <div>
        <el-row>
            <el-col :span="24">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">系统配置</el-breadcrumb-item>
                    <el-breadcrumb-item>定时任务管理</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-row>
        <el-row type="flex" justify="center">
            <el-card class="box-card">
                <div slot="header" style="display:flex; justify-content:space-between">
                    <el-button style="float: right;" type="primary" @click="dialogAddJobFormVisible = true">新增定时任务</el-button>
                </div>
                <div>
                    <el-dialog title="新增定时任务" :visible.sync="dialogAddJobFormVisible">
                        <el-form :model="jobForm" ref="jobForm">
                            <el-form-item label="任务名" :label-width="formLabelWidth">
                                <el-input v-model="jobForm.jobName" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="任务方法" :label-width="formLabelWidth">
                                <el-input v-model="jobForm.funcName" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="任务参数" :label-width="formLabelWidth">
                                <el-input v-model="jobForm.args" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="触发方式" :label-width="formLabelWidth">
                                <el-select v-model="jobForm.trigger" placeholder="请选择触发方式">
                                    <el-option label="interval" value="interval"></el-option>
                                    <el-option label="date" value="date"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="固定时间周期" :label-width="formLabelWidth" v-show="jobForm.trigger == 'interval'">
                                <el-input v-model="jobForm.intervalNum" autocomplete="off" placeholder=""></el-input>
                                <el-select v-model="jobForm.intervalDate" placeholder="请选择周期">
                                    <el-option label="周" value="weeks"></el-option>
                                    <el-option label="日" value="days"></el-option>
                                    <el-option label="小时" value="hours"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="固定时间" :label-width="formLabelWidth" v-show="jobForm.trigger == 'date'">
                                <el-date-picker v-model="jobForm.dateValue" type="datetime" placeholder="请选择时间"></el-date-picker>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button @click="handleDialogJobAddFormClose">取 消</el-button>
                            <el-button type="primary" @click="handleDialogJobAddFormSubmit">确 定</el-button>
                        </div>
                    </el-dialog>                    
                </div>
                <div>
                     <el-row type="flex" justify="center">
                        <el-table :data="jobsData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" :stripe="true">
                            <el-table-column prop="id" label="任务ID" width="150"></el-table-column>
                            <el-table-column prop="name" label="任务名" width="150"></el-table-column>
                            <el-table-column prop="func" label="任务方法" width="170"></el-table-column>
                            <el-table-column prop="trigger" label="触发方式" width="170"></el-table-column>
                            <el-table-column prop="start_date" label="开始时间" width="200"></el-table-column>
                            <el-table-column prop="next_run_time" label="下次运行时间" width="200"></el-table-column>
                            <el-table-column prop="op" label="操作" width="200">
                                <template slot-scope="scope">
                                    <el-button type='primary' @click="handlePause(scope.row)" v-show="!isShow(scope.row)" style="margin-left:0px">暂停</el-button>
                                    <el-button type='primary' @click="handleResume(scope.row)" v-show="isShow(scope.row)" style="margin-left:0px">启动</el-button>
                                    <el-button type='danger' @click="handleRemove(scope.row)">删除</el-button>
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
                            :total="jobsData.length"
                        ></el-pagination>  
                     </el-row>                  
                </div>
             </el-card>
        </el-row>
  </div>
</template>

<style>
.box-card {
    margin-top:20px;
}
</style>

<script>
import axios from 'axios'
import qs from 'qs'
export default {
    data () {
        return {
            currentPage: 1,
            pageSize: 5,
            jobsData: [],
            dialogAddJobFormVisible: false,
            jobForm: {
                jobName: '',
                funcName: '',
                args: '',
                trigger: '',
                intervalNum: '',
                intervalDate: '',
                dateValue: ''
            },
            formLabelWidth: '120px'
        }
    },
    methods: {
        handleInitialData() {
            let that = this;
            const path = "/api/scheduler/jobs";
            axios.get(path).then(function(response){
                that.jobsData = response.data
            });
        },
        handleCurrentChange(val) {
            console.log(val);
            this.currentPage = val;
            console.log(this.currentPage);
        },
        hanldeSizeChange(val) {
            console.log(val);
            this.pageSize = val;
            console.log(this.pageSize);
        },
        handleDialogJobAddFormClose() {
            this.$refs['jobForm'].resetFields();
            this.dialogAddJobFormVisible = false;
        },
        handleDialogJobAddFormSubmit() {
            var datas = qs.stringify(this.jobForm);
            var that = this
            const path = "/api/system/job/add";
            axios.post(path, datas, {headers:{'Content-Type':'application/x-www-form-urlencoded'}}).then(
                (res) => {
                    console.log(res.data.msg);
                    that.$notify({
                        title: "添加任务状况",
                        message: "添加任务" + that.jobForm.jobName + "成功",
                        type: "success"
                    });
                }
            );
            this.dialogAddJobFormVisible = false;
            this.handleInitialData();
        },
        handleRemove(row) {
            axios.get('/api/system/job/remove/' + row.id).then(response => {
                console.log(response.data)
                this.handleInitialData()
            })

        },
        handlePause(row) {
            axios.get('/api/system/job/pause/' + row.id).then(response => {
                if (response.data.msg == "success") {
                    this.$notify({
                        title:"暂停任务",
                        message:"暂停任务"+row.name+"成功",
                        type:"success"
                    })
                    this.handleInitialData()
                }
            })
        },
        handleResume(row) {
            axios.get('/api/system/job/resume/' + row.id).then(response => {
                if (response.data.msg == "success") {
                    this.$notify({
                        title:"启动任务",
                        message:"启动任务"+row.name+"成功",
                        type:"success"
                    })
                    this.handleInitialData()
                }
            })
        },
        isShow(row) {
            console.log(row)
            if (row.next_run_time == null)
                return true
            else
                return false
        }
    },
    mounted() {
        this.handleInitialData();
        this.isShow();
    }
}
</script>