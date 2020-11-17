<template>
    <div>
        <el-row>
            <el-col :span="24">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">系统管理</el-breadcrumb-item>
                    <el-breadcrumb-item>后台数据上传</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-row>
        <el-row type="flex" justify="left">
            <el-col :span="10">
                <el-card class="box-card">
                    <div slot="header" class="clearfix">
                        <span>上传文件</span>
                        <!-- <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button> -->
                    </div>
                    <div>
                        <el-upload
                            ref="upload"
                            action="/api/file/upload"
                            accept=".xls,.xlsx"
                            :limit= "1"
                            :on-preview="handlePreview"
                            :on-remove="handleRemove"
                            :on-change="handleChange"
                            :on-success="handleSuccess"
                            :file-list="fileList"
                            :auto-upload="false">
                        <el-button slot="trigger" type="primary">选取文件</el-button>
                        <el-button style="margin: 10px" type='success' @click="submitUpload">点击上传</el-button>
                        <div slot="tip" class="el-upload__tip">只能上传EXCEL文件</div>
                        </el-upload>
                    </div>
                </el-card>
                
            </el-col>
        </el-row>

    </div>
</template>

<style>
    .el-row {
        margin-bottom: 20px;
    }
</style>

<script>
export default {
    data() {
        return {
            fileList: []
        }
    },
    methods: {
        submitUpload() {
            this.$refs.upload.submit();
        },
        handlePreview(file) {
            console.log(file);
        },
        handleRemove(file, fileList) {
            let index = this.fileList.findIndex(
                fileItem => {
                    return fileItem.uid === file.uid
            })
            this.fileList.splice(index, 1) 
            console.log(file, fileList);
        },
        handleChange(file) {
            console.log(file.raw.name);
            var fileType = file.raw.name.substring(file.raw.name.lastIndexOf('.')+1);
            console.log(fileType.toUpperCase());
            if ((fileType.toUpperCase() != "XLS") && (fileType.toUpperCase() != "XLSX") && (fileType.toUpperCase() != "CSV")) {
                this.$message.error("上传的文件不是EXCEL");
                this.handleRemove(file);
            }
        },
        handleSuccess(response, file) {
            if (response.msg === "success") {
                console.log(file.raw.name);
                this.$notify({
                    title: "上传结果",
                    message: "上传文件" + file.raw.name + "成功",
                    type: "success"
                });
            }else if (response.msg === "failure") {
                console.log(file.raw.name);
                this.$notify.error({
                    title: "上传结果",
                    message: "上传文件" + file.raw.name + "失败",
                });
            }
        }
    }
}
</script>