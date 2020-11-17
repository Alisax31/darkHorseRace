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
        <el-row type="flex" justify="center">
            <el-table :data="tableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" stripe="true">
                <el-table-column prop="uid" label="uid" width="100"></el-table-column>
                <el-table-column prop="username" label="用户名" width="170"></el-table-column>
                <el-table-column prop="email" label="电子邮件" width="170"></el-table-column>
                <el-table-column prop="department" label="部门" width="170"></el-table-column>
                <el-table-column prop="phone" label="电话号码" width="170"></el-table-column>
                <el-table-column prop="create_time" label="创建时间" width="260"></el-table-column>
                <el-table-column prop="op" label="操作" width="250">
                    <el-button type='primary'>编辑</el-button>
                    <el-button type='danger'>删除</el-button>
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
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            currentPage: 1,
            pageSize: 5,
            tableData: []
        }
    },
    methods: {
        handleInitialData() {
            let that = this
            console.log("start-link")
            const path = "/api/user/get"
            axios.get(path).then(function(response){
                console.log(response.data)
                that.tableData = response.data
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
</style>