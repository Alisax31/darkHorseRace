<template>
    <div>
        <el-menu class="el-menu-side-menu" :default-active="$route.path" style="height:100%" :collapse="isCollapse" router :unique-opened="true">
            <li class="foldmenu"><i :class="isCollapse? 'el-icon-s-unfold' : 'el-icon-s-fold'" @click="foldMenu"></i></li>
            <el-submenu index="1">
                <template slot="title"><i class="el-icon-s-promotion icon"></i><span slot="title" class="title">Dashboard</span></template>
                <el-menu-item-group>
                    <el-menu-item index="/dashboard/analysis">总览</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title"><i class="el-icon-data-analysis icon"></i><span slot="title" class="title">备件消耗预测</span></template>
                <el-menu-item-group>
                    <el-menu-item index="/analysis/fbp">Fbprophet预测</el-menu-item>
                    <el-menu-item index="/analysis/timeanalysis">时间序列预测</el-menu-item>
                </el-menu-item-group>                    
            </el-submenu>
            <el-submenu index="3">
                <template slot="title"><i class="el-icon-s-tools icon"></i><span slot="title" class="title">系统配置</span></template>
                <el-menu-item-group>
                    <el-menu-item index="/user/manage">用户管理</el-menu-item>
                    <el-menu-item index="/system/fileupload">后台数据上传</el-menu-item>
                    <el-menu-item index="/system/jobsmanage">定时任务管理</el-menu-item>
                    <el-menu-item index="/system/holiday">节假日设定</el-menu-item>
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
    background-color: #409EFF;
  }
  .el-menu-side-menu {
    background-color: #409EFF;
  }
  .el-menu-item {
    color:#FEFEFE;
    background-color:#409EFF;
    font-weight: bold;
  }
  .el-menu-item.is-active {
    background-color: #FEFEFE;
  }
  .el-menu-item:focus {
    background-color: #FEFEFE;
  }
  .el-menu-item:hover {
    color:#409EFF;
  }
  .el-menu-item-group__title {
    padding-top: 0px;
    padding-bottom: 0px;
  }
  .foldmenu {
    font-size: 24px;
    text-align: center;
    padding: 0;
  }
  .foldmenu i {
    color:#FEFEFE;
  }
  .title {
    color:#FEFEFE;
    font-weight: bold; 
  }
  .el-submenu__title:hover i {
    color:#409EFF;
    font-weight: bold;
  }
  .el-submenu__title:hover .title {
    color:#409EFF;
    font-weight: bold;
  }
  .icon {
    color:#FEFEFE;
    font-size:24px;
  }
  .el-submenu__title i {
    color:#FEFEFE;
    font-size:24px;
  }

</style>