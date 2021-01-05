<template>
    <div class="analysiswarp">
        <el-row class="path">
            <el-col :span="24">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">Dashboard</el-breadcrumb-item>
                    <el-breadcrumb-item>总览</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-row>
        <el-row class="row" type="flex" justify="center">
            <el-col :span="4"></el-col>
            <el-col :span="16" style="display:flex;justify-content:center">
                <el-checkbox-group v-model="plantGroup" @change="fresh()">
                    <el-checkbox-button v-for="plant in plants" :label="plant" :key="plant">{{plant}}</el-checkbox-button>
                </el-checkbox-group>
            </el-col>
            <el-col :span="4"></el-col>
        </el-row>
        <el-row class="row" type="flex" justify="center">
            <el-col :span="22">
                <el-slider
                    v-model="yearSlider"
                    range
                    show-stops
                    :min="2017"
                    :max="2020"
                    :marks="{2017:'2017',2018:'2018',2019:'2019',2020:{style:{left: '95%'},label:'2020'}}"
                    @input="fresh()"> 
                </el-slider>
            </el-col>
        </el-row>
        <el-row class="row" :gutter="20">
            <el-col :span="6" v-loading="">
                <el-card body-style="padding:0 0" style="height:180px;background-color:orange">
                    <el-row>
                        <el-col class="center">
                        <span style="font-weight:bold;padding-top:10px;color:#FFF">已消耗备件种类百分比</span>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col>
                        <div class="center keyChart" ref="" v-loading="">
                            <el-progress type="dashboard" :percentage="percentage" :color="colors"></el-progress>
                        </div>
                        </el-col>
                    </el-row>   
                </el-card>
            </el-col>
            <el-col :span="6">
                <el-card body-style="padding:0 0" style="height:180px;background-color:orange">
                    <el-row>
                        <el-col class="center">
                        <span style="font-weight:bold;padding-top:10px;color:#FFF">备件库存消耗总量</span>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col>
                        <div class="center keyChart" ref="" v-loading="">
                            <span style="font-weight:bold;padding-top:20px;font-size:32px;color:#FFF">{{total_amount}}</span>
                        </div>
                        </el-col>
                    </el-row>   
                </el-card>
            </el-col>
            <el-col :span="6">
                <el-card body-style="padding:0 0" style="height:180px;background-color:orange">
                    <el-row>
                        <el-col class="center">
                        <span style="font-weight:bold;padding-top:10px;color:#FFF">备件库存消耗总金额</span>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col>
                        <div class="center keyChart" ref="" v-loading="">
                            <span style="font-weight:bold;padding-top:20px;font-size:32px;color:#FFF">{{total_price}}</span>
                        </div>
                        </el-col>
                    </el-row>   
                </el-card>
            </el-col>
            <el-col :span="6">
                <el-card body-style="padding:0 0" style="height:180px;background-color:orange">
                    <el-row>
                        <el-col class="center">
                        <span style="font-weight:bold;padding-top:10px;color:#FFF">后台任务运行状况</span>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="24">
                            <span style="font-weight:bold;font-size:24px;padding:0px 0px;color:#FFF;margin-left:30px">总量：<span style="color:#409EFF">{{job.total}}</span></span>
                            <el-progress :percentage="100" class="jobProgress"></el-progress>
                            <span style="font-weight:bold;font-size:24px;padding:0px 0px;color:#FFF;margin-left:30px">运行中：<span style="color:#67C23A">{{job.run}}</span></span>
                            <el-progress :percentage="job.run*100/job.total" class="jobProgress" status="success"></el-progress>
                        </el-col>
                    </el-row>   
                </el-card>
            </el-col>                       
        </el-row>
        <el-row class="row" :gutter="20">
            <el-col :span="12">
                <el-card body-style="padding:20px 5px;display:flex;align-content:center;">
                    <el-carousel height="550px" :autoplay="false" style="width:100%">
                        <el-carousel-item style="width:100%">
                             <div class="myChart" ref="barChart" v-loading="loading.barChart"></div>
                        </el-carousel-item>
                        <el-carousel-item>
                            <div class="myChart" ref="areaStackChart" v-loading="loading.areaStackChart"></div>
                        </el-carousel-item>
                        <el-carousel-item>
                            <div class="myChart" ref="lineChart" v-loading="loading.lineChart"></div>
                        </el-carousel-item>
                        <!-- <el-carousel-item><h2>3</h2></el-carousel-item> -->
                    </el-carousel>
                      
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card body-style="padding:20px 5px;display:flex;align-content:center;">
                        <div class="myChart" ref="polarChart" v-loading="loading.polarChart"></div>   
                </el-card>
            </el-col>
        </el-row>
        <el-row class="row">
            <el-card body-style="padding:20px 5px;display:flex;align-content:center;background-color:#404a59">
                <div class="myChart2" ref="scatterChart" v-loading="loading.scatterChart"></div>
            </el-card>
        </el-row>
        <el-row><router-view></router-view></el-row>
    </div>
</template>

<script>
import axios from 'axios'
const plants = ['PFA1','PFA2','PFA3','PFC','PFE','PFH','PFN','PFS','PFW','PFY'];
export default {
    data() {
        return {
            loading: {
                barChart : false,
                polarChart : false,
                keyChart : false,
                areaStackChart : false,
                scatterChart : false,
                lineChart : false
            },
            job:{
                total: 0,
                run: 0
            },
            total_price: 0,
            total_amount: 0,
            plants: plants,
            plantGroup: ['PFA1','PFA2','PFA3','PFC','PFE','PFH','PFN','PFS','PFW','PFY'],
            yearSlider: [2017,2020],
            percentage: 10,
            colors: [
                {color: '#f56c6c', percentage: 20},
                {color: '#e6a23c', percentage: 40},
                {color: '#5cb87a', percentage: 60},
                {color: '#1989fa', percentage: 80},
                {color: '#6f7ad3', percentage: 100}
            ]
        }
    },
    mounted() {
        this.showBarChart();
        this.showLineChart();
        this.showSnoPercent();
        this.showJob();
        this.showPloarChart();
        this.showScatterChart();
    },
    methods: {
        showBarChart() {
            this.loading.barChart = true;
            var that = this;
            axios.get('/api/dashboard/bar/get').then(function(response){
                var barData = response.data;
                var xAxisData = [];
                var yAxisData = []; 
                for (var k in barData) {
                    xAxisData.push(barData[k].sno);
                    yAxisData.push(barData[k].sum);
                }
                let barChart = that.$echarts.init(that.$refs.barChart, 'light');
                barChart.setOption({
                    title: {
                        text: '备件消耗量 TOP 5',
                        left: 'center',
                    },
                    grid: {
                        // left: '10%',
                        // right: '10%',
                        // top: '18%',
                        // bottom: '10%'
                        containLabel:true
                    },
                    tooltip: {},
                    xAxis:{
                        data: xAxisData,
                        nameTextStyle: {
                            fontSize: 14
                        },
                        splitLine: {
                            show: false
                        }
                    },
                    yAxis:{
                        nameTextStyle: {
                            fontSize: 14
                        },
                        splitLine: {
                            show: true
                        }
                    },
                    series:[{
                        name:'count',
                        type:'bar',
                        label: {
                            show: true
                        },
                        data: yAxisData
                    }]
                })
                that.loading.barChart = false
            })
        },
        showLineChart() {
            this.lineChart = true;
            this.areaStackChart = true;
            axios.get('/api/dashboard/linechart/get').then((response) => {
                let lineChart = this.$echarts.init(this.$refs.lineChart, 'light');
                let areaStackChart = this.$echarts.init(this.$refs.areaStackChart, 'light');
                var data = response.data;
                lineChart.setOption({
                    title: {
                        text:'滞留备件数量趋势',
                        left: 'center',
                    },
                    grid: {
                        left: '8%',
                        // right: '10%',
                        // top: '18%',
                        // bottom: '10%'
                        containLabel:true
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    xAxis: {
                        data: data.year_i,
                        name: '年份'
                    },
                    yAxis: {
                        type: 'value',
                        name: '数量(万个)'
                    },
                    series: [{
                        type: 'line',
                        areaStyle: {},
                        data: data.amount_sum
                    }]
                });
                areaStackChart.setOption({
                    title: {
                        text:'滞留备件金额趋势',
                        left: 'center',
                    },
                    grid: {
                        left: '8%',
                        // right: '10%',
                        // top: '18%',
                        // bottom: '10%'
                        containLabel:true
                    }, 
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    xAxis: {
                        data: data.year_i,
                        name: '年份'
                    },
                    yAxis: {
                        type: 'value',
                        name: '金额(万元)'
                    },
                    series: [{
                        type: 'line',
                        areaStyle: {},
                        data: data.total_price
                    }]
                });
                this.lineChart = false;
                this.areaStackChart = false;
            })
        },        
        showPloarChart() {
            this.loading.polarChart = true;
            let that = this;
            axios.get('/api/dashboard/polar/get').then(function(response){
                var polarData = response.data;
                var top5_plant_sno_data = [];
                var top5_plant_amount_data = [];
                for (var k in polarData) {
                    top5_plant_amount_data.push(polarData[k])
                    top5_plant_sno_data.push(k)
                }
                let polarChart = that.$echarts.init(that.$refs.polarChart, 'light');
                polarChart.setOption({
                    title: {
                         text: '各工厂共用备件消耗TOP5',
                         left: 'center'
                    },
                    grid: {
                        left: "20%"
                        // right: 150,
                        // bottom: '10%'
                    },
                    angleAxis: {
                    },
                    radiusAxis: {
                        type: 'category',
                        data: ['PFA1','PFA2','PFA3','PFC','PFE','PFH','PFN','PFS','PFW','PFY'],
                        z: 10,
                        interval: 0                        
                    },
                    polar: {
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    series: [
                        {
                            type: 'bar',
                            data: top5_plant_amount_data[0],
                            coordinateSystem: 'polar',
                            name: top5_plant_sno_data[0],
                            stack: 'a'
                        }, 
                        {
                            type: 'bar',
                            data: top5_plant_amount_data[1],
                            coordinateSystem: 'polar',
                            name: top5_plant_sno_data[1],
                            stack: 'a'
                        },
                        {
                            type: 'bar',
                            data: top5_plant_amount_data[2],
                            coordinateSystem: 'polar',
                            name: top5_plant_sno_data[2],
                            stack: 'a'
                        },
                        {
                            type: 'bar',
                            data: top5_plant_amount_data[3],
                            coordinateSystem: 'polar',
                            name: top5_plant_sno_data[3],
                            stack: 'a'
                        },
                                                {
                            type: 'bar',
                            data: top5_plant_amount_data[4],
                            coordinateSystem: 'polar',
                            name: top5_plant_sno_data[4],
                            stack: 'a'
                        },
                    ],
                    legend: {
                        show: true,
                        y: "95%",
                        data: top5_plant_sno_data
                    }
                })
                that.loading.polarChart = false;
            })
        },
        showScatterChart() {
            this.loading.scatterChart = true;
            var that = this;
            var jsons = {
                'start_year': this.yearSlider[0],
                'end_year': this.yearSlider[1],
                'plants': this.plantGroup
            }
            axios.post('/api/dashboard/scatter/post', jsons, {header:{'Content-Type':'application/json'}}).then(function(response){
                var dataPFW = [];
                var dataPFS = [];
                var dataPFE = [];
                var dataPFA1 = [];
                var dataPFN = [];
                var dataPFH = [];
                var dataPFC = [];
                var dataPFY = [];
                var dataPFA2 = [];
                var dataPFA3 = [];
                dataPFW = response.data['PFW'];
                dataPFS = response.data['PFS'];
                dataPFE = response.data['PFE'];
                dataPFA1 = response.data['PFA1'];
                dataPFA2 = response.data['PFA2'];
                dataPFA3 = response.data['PFA3'];
                dataPFN = response.data['PFN'];
                dataPFH = response.data['PFH'];
                dataPFC = response.data['PFC'];
                dataPFY = response.data['PFY'];
                // dataPFW.push(response.data['PFW']);
                // dataPFS.push(response.data['PFS']);
                // dataPFE.push(response.data['PFE']);
                var schema = [
                    {name: 'date', index: 0, text: '月份'},
                    {name: 'sum_sno', index: 1, text: '备件消耗总量'},
                    {name: 'count_sno', index: 2, text: '消耗备件种类'}
                    
                ];

                var itemStyle = {
                    opacity: 0.8,
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowOffsetY: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                };

                var option = {
                    title: {
                        text: that.yearSlider[0] + "-" + that.yearSlider[1] + "年各工厂备件消耗总量以及消耗种类总量图",
                        left: "center",
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    backgroundColor: '#404a59',
                    color: [
                        '#dd4444', '#fec42c', '#80F1BE', '#2840d2', '#fc97af', '#ffffff', '#27727b', '#d4a4eb', '#d2f5a6', '#76f2f2'
                    ],
                    legend: {
                        top: 30,
                        data: that.plantGroup,
                        textStyle: {
                            color: '#fff',
                            fontSize: 16
                        }
                    },
                    grid: {
                        left: '10%',
                        right: 150,
                        top: '18%',
                        bottom: '10%'
                    },
                    tooltip: {
                        padding: 10,
                        backgroundColor: '#222',
                        borderColor: '#777',
                        borderWidth: 1,
                        formatter: function (obj) {
                            var value = obj.value;
                            return '<div style="border-bottom: 1px solid rgba(255,255,255,.3); font-size: 18px;padding-bottom: 7px;margin-bottom: 7px">'
                                + obj.seriesName + ' ' + value[0] + '月：'
                                + '</div>'
                                + schema[1].text + '：' + value[1] + '<br>'
                                + schema[2].text + '：' + value[2] + '<br>';
                                // + schema[3].text + '：' + value[3] + '<br>'
                                // + schema[4].text + '：' + value[4] + '<br>'
                                // + schema[5].text + '：' + value[5] + '<br>'
                                // + schema[6].text + '：' + value[6] + '<br>';
                        }
                    },
                    xAxis: {
                        type: 'category',
                        name: '月份',
                        nameGap: 16,
                        nameTextStyle: {
                            color: '#fff',
                            fontSize: 14
                        },
                        splitLine: {
                            show: false
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#eee'
                            }
                        }
                    },
                    yAxis: {
                        type: 'value',
                        name: '备件消耗总量 ',
                        nameLocation: 'end',
                        nameGap: 20,
                        nameTextStyle: {
                            color: '#fff',
                            fontSize: 16
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#eee'
                            }
                        },
                        splitLine: {
                            show: false
                        }
                    },
                    visualMap: [
                        {
                            left: 'right',
                            top: '10%',
                            dimension: 2,
                            min: 0,
                            max: 5000,
                            itemWidth: 30,
                            itemHeight: 120,
                            calculable: true,
                            precision: 0.1,
                            text: ['圆形大小：备件消耗种类'],
                            textGap: 30,
                            textStyle: {
                                color: '#fff'
                            },
                            inRange: {
                                symbolSize: [10, 70]
                            },
                            outOfRange: {
                                symbolSize: [10, 70],
                                color: ['rgba(255,255,255,.2)']
                            },
                            controller: {
                                inRange: {
                                    color: ['#c23531']
                                },
                                outOfRange: {
                                    color: ['#444']
                                }
                            }
                        }
                        
                    ],
                    series: [
                        {
                            name: 'PFA1',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFA1
                        },
                        {
                            name: 'PFA2',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFA2
                        },
                        {
                            name: 'PFA3',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFA3
                        },
                        {
                            name: 'PFE',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFE
                        },
                        {
                            name: 'PFS',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFS
                        },
                        {
                            name: 'PFN',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFN
                        },
                        {
                            name: 'PFY',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFY
                        },
                        {
                            name: 'PFH',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFH
                        },
                        {
                            name: 'PFW',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFW
                        },
                        {
                            name: 'PFC',
                            type: 'scatter',
                            itemStyle: itemStyle,
                            data: dataPFC
                        },
                    ]
                };
                let scatterChart = that.$echarts.init(that.$refs.scatterChart, 'light');   
                scatterChart.setOption(option);            
            }).finally(() => {
                this.loading.scatterChart = false;        
            });
        },
        showSnoPercent() {
            this.loading.keyChart = true;
            var start_year = this.yearSlider[0];
            var end_year = this.yearSlider[1];
            var jsons = {
                'start_year': start_year,
                'end_year': end_year,
                'plants': this.plantGroup
            }
            axios.post('/api/dashboard/keychart/post', jsons, {header:{'Content-Type':'application/json'}}).then(response => {
                // this.percentage = response.data['percentage'];
                this.percentage = Math.round((response.data['percentage'] / 100000)*100)
                var temp = response.data['total_price'].toString().split('.')
                this.total_price = (Math.round(temp[0]/1000) || 0).toString().replace(/(\d)(?=(?:\d{3})+$)/g, '$1,')
                this.total_amount = (Math.round(response.data['total_amount']/1000) || 0).toString().replace(/(\d)(?=(?:\d{3})+$)/g, '$1,')
                this.loading.keyChart = false;
            })
        },
        fresh() {
            this.showSnoPercent()
            this.showScatterChart()
        },
        showJob() {
            axios.get('/api/scheduler/jobs').then(response => {
                this.job.total = response.data.length
                var data = response.data
                console.log(response.data)
                var i=0
                while (i<this.job.total) {
                    if (data[i].next_run_time != null) {
                        this.job.run += 1
                    }
                    i += 1
               }
            })
        }
    }
}
</script>

<style>
    .path {
        margin-bottom:20px;
    }
    .row {
        margin-top:20px;
        margin-bottom: 20px;
    }
    .center {
        display: flex;
        justify-content: center;
    }
    .keyChart {
        padding-top:10px;
    }
    .myChart {
        height: 550px;
        width: 600px;
    }
    .myChart2 {
        height: 600px;
        width: 1300px;
    }
    .analysiswrap {
        padding: 0px;
    }
    .jobProgress {
        margin-left:30px;
        margin-top: 5px;
    }
</style>