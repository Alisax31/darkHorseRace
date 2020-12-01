<template>
    <div>
        <el-row>
            <el-col :span="24">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">备件库存消耗分析</el-breadcrumb-item>
                    <el-breadcrumb-item>时间预测分析</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="24">
                <el-card>
                    <div slot="header" class="clearfix">
                        <el-row>
                            <el-col :span="24"><span>时间预测分析</span></el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="8" style="margin-left:50px"><el-input type="text" v-model="sno" placeholder="请输入备件号"></el-input></el-col>
                            <el-col :span="8"></el-col>
                            <el-col :span="8"><el-button type="primary" @click="showTimeAnalysis()">查询预测</el-button></el-col>
                        </el-row>
                        
                        <!-- <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button> -->
                    </div>
                    <div class="timeAnalysisChart" ref="timeAnalysis" v-loading="loading">

                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            sno:'',
            loading:false
        }
    },
    mounted() {
        // this.showTimeAnalysis()
    },
    methods: {
        showTimeAnalysis() {
            this.loading = true;
            let that = this;
            console.log("showTimeAnalysis");
            axios.get("/api/analysis/timeanalysis/get/" + that.sno).then((response) => {
                var sno = that.sno
                if(response.data['msg'] == 'nodata') {
                    that.$notify.error({
                        title: "查询结果",
                        message: this.sno + "没有对应数据，请检查输入备件号是否准确。"
                    })
                }
                else {
                    var actual_quantity = [];
                    var predict_quantity = [];
                    var month = [];
                    var actual_value = response.data['actual_value'];
                    var predict_value = response.data['predict_value'];
                    for(var k in actual_value) {
                        month.push(actual_value[k][1])
                        actual_quantity.push(actual_value[k][2])
                    }
                    for(var i in predict_value) {
                        predict_quantity.push(predict_value[i][2])
                    }
                    console.log(actual_quantity)
                    console.log(predict_quantity)
                    //     var date = new Date(response.data[k].month);
                    //     date = date.getFullYear() + "-" + (Number(date.getMonth())+1) ;
                    //     month.push(date);
                    //     quantity.push(response.data[k].quantity);
                    // }
                    let timeAnalysis = that.$echarts.init(that.$refs.timeAnalysis, 'light');
                    timeAnalysis.setOption({
                        title: {
                            text: sno + " 下月消耗量预测",
                            left: "center",
                        },
                        legend: {
                            data: ["实际值","预测值"],
                            orient: 'vertical',
                            left: 'left'
                        },
                        xAxis: {
                            type: 'category',
                            name: '月份',
                            data: month
                        },
                        yAxis: {
                            type: 'value',
                            name: '备件消耗量'
                        },
                        series: [
                        {
                            name: '实际值',
                            data: actual_quantity,
                            type: 'line',
                            label: {
                                show: true,
                                position: 'top'
                            }
                        },
                        {
                            name: '预测值',
                            data: predict_quantity,
                            type: 'line',
                            label: {
                                show:true,
                                position: 'bottom'
                            }
                        }
                        ]
                    })
                }
            }).finally(() => {
                this.loading = false;
            });
            }
    }
}
</script>

<style>
    .timeAnalysisChart {
        width:100%;
        height:600px;
    }
    .el-row {
        margin-bottom: 20px;
    }
</style>