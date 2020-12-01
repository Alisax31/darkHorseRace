<template>
    <el-container>
        <SideMenu></SideMenu>
        <el-container class="is-vertical">
            <el-header height="30px">
                <Header></Header>
            </el-header>
            <el-main class="main">
                <router-view></router-view>
            </el-main>
            <el-footer height="30px">
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
    }
}
</script>

<style>
.main {
    background-color:rgb(246,246,246);
}
</style>