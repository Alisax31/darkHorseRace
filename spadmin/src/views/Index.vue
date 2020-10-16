<template>
    <div id='app'>
        <el-container style="height: 600px; border: 1px">
            <el-aside width="200px" style="background-color:#409eff">
                <el-menu :default-openeds="['1']">
                    <el-submenu index="1">
                        <template slot="title"><i class="el-icon-s-promotion"></i>Nav1</template>
                        <el-menu-item-group>
                            <el-menu-item index="1-1">Option1-1</el-menu-item>
                            <el-menu-item index="1-2">Option1-2</el-menu-item>
                            <el-menu-item index="1-3">Option1-3</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-submenu index="2">
                        <template slot="title"><i class="el-icon-s-tools"></i>Nav2</template>
                        <el-menu-item-group>
                            <el-menu-item index="2-1">Option2-1</el-menu-item>
                            <el-menu-item index="2-2">Option2-2</el-menu-item>
                            <el-menu-item index="2-3">Option2-3</el-menu-item>
                        </el-menu-item-group>                    
                    </el-submenu>
                    <el-submenu index="3">
                        <template slot="title"><i class="el-icon-message"></i>Nav3</template>
                        <el-menu-item-group>
                            <el-menu-item index="3-1">Option3-1</el-menu-item>
                            <el-menu-item index="3-2">Option3-2</el-menu-item>
                            <el-menu-item index="3-3">Option3-3</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                </el-menu>
            </el-aside>
            <el-container>
                <el-header style="text-align:right">
                    <el-dropdown>
                        <i class="el-icon-setting" style="margin-right: 15px"></i>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item>View</el-dropdown-item>
                            <el-dropdown-item>New</el-dropdown-item>
                            <el-dropdown-item>Delete</el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown> 
                    <span>{{msg}}</span>
                </el-header>
                <el-main>
                    <el-table :data="tableData">
                        <el-table-column prop="date" label="date" width="150"></el-table-column>
                        <el-table-column prop="name" label="name" width="150"></el-table-column>
                        <el-table-column prop="address" label="address" width="150"></el-table-column>
                    </el-table>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
export default {
    data(){
        const item = {
            date: '2020-10-15',
            name: 'Alisax',
            address: 'IMB II '
        };
        return {
            msg: '123',
            tableData: Array(10).fill(item)
        };
    }
}
</script>
