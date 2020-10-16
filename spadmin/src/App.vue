<template>
    <div id='app'>
        <el-row>
            <el-col :span="24"><div class="grid-content"></div></el-col>
        </el-row>
        <el-row type="flex" justify="center">
            <el-col :span="12"><div class="grid-content"></div></el-col>                         
        </el-row>
        <el-row>
            <el-col :span="24"><div class="grid-content"></div></el-col>
        </el-row>
    </div>
</template>

<style>
    .grid-content {
        background-color: rgb(204, 204, 204);
        border-radius: 4px;
        min-height: 230px;
        min-width: 100px;
    }
</style>
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
