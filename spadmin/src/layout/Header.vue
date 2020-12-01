<template>
    <div>
    <el-header style="text-align: right; font-size: 18px; line-height: 30px;">
        <!-- <el-button type="primary" icon="el-icon-menu" @click="isCollapse != isCollapse"></el-button> -->
        <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px; font-size:24px"><el-badge :value="msg_count" class="item" v-show="isValid"></el-badge></i>
            <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>个人信息</el-dropdown-item>
                <el-dropdown-item> 
                    <span @click="table = true">站内信</span><el-badge :value="msg_count" class="item" v-show="isValid"></el-badge>
                </el-dropdown-item>
                <el-dropdown-item><el-link href="/#/user/login">登出</el-link></el-dropdown-item>
            </el-dropdown-menu>
        </el-dropdown>
        <span>{{msg}}</span>
    </el-header>
    <el-drawer title="站内信" :visible.sync="table" direction="rtl" size="35%">
        <div style="display:flex;justify-items:center">
        <el-table :data="msgData">
            <el-table-column property="mid" label="MID" width="80"></el-table-column>
            <el-table-column property="message" label="信息内容" width="200"></el-table-column>
            <el-table-column property="create_time" label="时间" width="150"></el-table-column>
            <el-table-column property="is_read" label="是否已读" width="100">
                <template slot-scope="scope">
                    <el-switch
                    style="display: block"
                    v-model="scope.row.is_read"
                    active-color="#13ce66"
                    inactive-color="#ff4949"
                    active-value="1"
                    inactive-value="0"
                    @change="handleRead(scope.row)">
                    </el-switch>
                </template>
            </el-table-column>
        </el-table>
        </div>
    </el-drawer>
    </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
export default {
    data() {
        return {
            msg : "Admin",
            msg_count: 0,
            // isValid: false,
            table: false,
            msgData: []
        }
    },
    methods: {
        getMsg() {
            axios.get('/api/system/msg/get').then(response => {
                this.msg_count = Number(response.data['msg_count'])
                if(this.msg_count > 0) {
                    this.isValid = true
                    this.msgData = response.data['msg_result']
                }
            })
        },
        handleRead(row) {
            console.log(row) 
            var param = {'mid':row.mid,'is_read':row.is_read}
            axios.get('/api/system/msg/update', {params:param}).then(response => {
                if (response.data['msg'] == 'success') {
                    this.getMsg()
                }
            })
        }
    },
    mounted() {
        this.getMsg()
    }
}
</script>