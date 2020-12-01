<template>
    <div>
        <el-row>
            <el-col :span="24">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">备件库存消耗分析</el-breadcrumb-item>
                    <el-breadcrumb-item>FBProphet时间预测分析</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="24">
                <el-card>
                    <div slot="header" class="clearfix">
                        <el-row>
                            <el-col :span="24"><span>FBProphet时间预测分析</span></el-col>
                        </el-row>
                        <el-row gutter="20">
                            <el-col :span="6"><el-input type="text" v-model="fbp.sno" placeholder="请输入备件号"></el-input></el-col>
                            <el-col :span="6"><el-input type="text" v-model="fbp.periods" placeholder="请输入预测周期"></el-input></el-col>
                            <el-col :span="6">
                                <el-select v-model="fbp.freq" placeholder="请选择预测频次">
                                    <el-option label="年" value="Y"></el-option>
                                    <el-option label="月" value="M"></el-option>
                                    <el-option label="日" value="D"></el-option>
                                </el-select>
                            </el-col>
                            <el-col :span="6"><el-button type="primary" @click="showFBPAnalysis()">查询预测</el-button></el-col>
                        </el-row>
                        
                        <!-- <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button> -->
                    </div>
                    <div class="block" v-loading="loading">
                        <el-carousel height="600px" v-show="isShow" autoplay="false" style="width:100%">
                            <el-carousel-item style="width:100%">
                                <div class="fbpChart" ref="fbpAnalysis"></div>
                            </el-carousel-item>
                            <!-- <el-carousel-item><h2>1</h2></el-carousel-item>
                            <el-carousel-item><h2>2</h2></el-carousel-item>
                            <el-carousel-item><h2>3</h2></el-carousel-item> -->
                        </el-carousel>
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
            loading: false,
            isShow: false,
            fbp: {
                sno:  '',
                freq: '',
                periods: ''
            }
        }
    },
    methods: {
        showFBPAnalysis() {
            this.loading = true;
            let that = this;
            var param = this.$data.fbp;
            console.log("showFBPAnalysis");
            axios.get("/api/analysis/fbp/get", {params:param}).then((response) => {
                if(response.data['msg'] == 'nodata') {
                    that.$notify.error({
                        title: "查询结果",
                        message: this.sno + "没有对应数据，请检查输入备件号是否准确。"
                    });
                }
                else {
                    var data = response.data;
                    var trend = [];
                    // var trendLower = data['trend_lower'];
                    // var trendUpper = data['trend_upper'];
                    var yHat = data['yhat'];
                    var yHatLower = data['yhat_lower'];
                    var temp = data['yhat_upper'];
                    var yHatUpper = [];
                    var datetime = data['ds'];
                    var k=0;
                    while(k <= datetime.length - 1) {
                        trend.push([datetime[k], data['trend'][k]]);
                        k += 1;
                    }
                    var i=0;
                    while(i <= temp.length - 1) {
                        yHatUpper.push(temp[i] - yHatLower[i]);
                        i += 1;
                    }
                    console.log(trend);
                    console.log(yHatUpper);
                    var option = {
                        title: {
                            text: this.fbp.sno + '--FBP备件消耗量预测'
                        },
                        legend: {
                            data: ['预测下限', '预测值', '预测上限']
                        },
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            }
                        },
                        xAxis: [
                            {
                                type: 'category',
                                boundaryGap: false,
                                data: datetime
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value'
                            }
                        ],
                        series: [
                            {
                                name: '预测下限',
                                type: 'line',
                                stack: 'y',
                                areaStyle: {
                                    color:'rgb(255,255,255)'
                                },
                                data: yHatLower
                            },
                            {
                                name: '预测值',
                                type: 'line',
                                stack: 'yhat',
                                // areaStyle: {},
                                data: yHat
                            },
                            {
                                name: '预测上限',
                                type: 'line',
                                stack: 'y',
                                areaStyle: {},
                                data: yHatUpper
                            },
                            {
                                name: 'trend',
                                type: 'scatter',
                                data: trend
                            }
                        ]
                    };
                    that.$echarts.init(that.$refs.fbpAnalysis, 'light').setOption(option);
                }
            }).finally(() => {
                this.loading = false;
                this.isShow = true;
            });
        }
    }
}
</script>

<style>
.fbpChart {
    width:1200px;
    height:600px;
}
.el-row {
    margin-bottom: 20px;
}
.block {
    width: 1200px;
    height: 600px;
    display: flex;
    align-content: center;
}
</style>