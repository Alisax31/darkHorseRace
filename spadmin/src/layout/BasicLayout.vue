<template>
    <el-container>
        <SideMenu></SideMenu>
        <el-container class="is-vertical">
            <!-- <el-header style="text-align:right"> -->
                 <!-- <i class="el-icon-s-fold" style="text-align:left"></i> -->
                <Header></Header>
            <!-- </el-header> -->
            <el-main>
                <!-- <el-table :data="tableData">
                    <el-table-column prop="date" label="date" width="150"></el-table-column>
                    <el-table-column prop="name" label="name" width="150"></el-table-column>
                    <el-table-column prop="address" label="address" width="150"></el-table-column>
                </el-table> -->
                <router-view></router-view>
            </el-main>
            <el-footer>
                <Footer></Footer>
            </el-footer>
        </el-container>
    </el-container>
</template>

<script>
import Header from './Header';
import SideMenu from './SideMenu';
import Footer from './Footer';
export default {
    components: {
        Header,
        SideMenu,
        Footer
    },
    data(){
        const item = {
            date: '2020-10-15',
            name: 'Alisax',
            address: 'IMB II '
        };
        return {
            collapsed: false,
            msg: '123',
            tableData: Array(10).fill(item)
        };
    }
}
</script>