<template>
    <div>
        <el-menu class="el-menu-side-menu" :default-openeds="['1']" style="height:100%" :collapse="isCollapse" router>
            <li class="foldmenu"><i :class="isCollapse? 'el-icon-s-unfold' : 'el-icon-s-fold'" @click="foldMenu"></i></li>
            <el-submenu index="1">
                <template slot="title"><i class="el-icon-s-promotion"></i><span slot="title">Dashboard</span></template>
                <el-menu-item-group>
                    <el-menu-item index="/dashboard/analysis">总览</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title"><i class="el-icon-data-analysis"></i><span slot="title">备件库存消耗分析</span></template>
                <el-menu-item-group>
                    <el-menu-item index="2-1">Option2-1</el-menu-item>
                    <el-menu-item index="2-2">Option2-2</el-menu-item>
                    <el-menu-item index="2-3">Option2-3</el-menu-item>
                </el-menu-item-group>                    
            </el-submenu>
            <el-submenu index="3">
                <template slot="title"><i class="el-icon-s-tools"></i><span slot="title">系统配置</span></template>
                <el-menu-item-group>
                    <el-menu-item index="/user/manage">用户管理</el-menu-item>
                    <el-menu-item index="/system/fileupload">后台数据上传</el-menu-item>
                    <el-menu-item index="/system/jobsmanage">定时任务管理</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
        </el-menu>
    </div>
</template>
<script>
export default {
    data() {
        return {
            isCollapse: false,
        }
    },
    methods: {
        foldMenu() {
            console.log(this.isCollapse)
            this.isCollapse = !this.isCollapse
            console.log(this.isCollapse)
        } 
    }
}
</script>

<style>
  .el-menu-side-menu:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
  .foldmenu {
    font-size: 24px;
    text-align: center;
    padding: 0;
  }

</style>