<template>
    <el-header style="text-algin:right">
        <!-- <el-button type="primary" icon="el-icon-menu" @click="isCollapse != isCollapse"></el-button> -->
        <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>个人信息</el-dropdown-item>
                <el-dropdown-item>修改密码</el-dropdown-item>
                <el-dropdown-item>登出</el-dropdown-item>
            </el-dropdown-menu>
        </el-dropdown> 
        <span>{{msg}}</span>
    </el-header>
</template>

<script>
export default {
    data() {
        return {
            msg : "AlisaX"
        }
    }
}
</script>