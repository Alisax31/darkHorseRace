<template>
    <div class="analysiswarp">
        <el-row>
            <el-col :span="24">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/' }">Dashboard</el-breadcrumb-item>
                    <el-breadcrumb-item>总览</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-row>
        <el-row  :gutter="20">
            <el-col :span="8">
                <el-card>
                    <div class="myChart" ref="barChart"></div>   
                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card>
                    <div class="myChart" ref="areaStackChart"></div>   
                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card>
                    <div class="myChart" ref="nightingaleChart"></div>   
                </el-card>
            </el-col>        
        </el-row>
        <el-row>
            <el-card>
                <div class="myChart2" ref="scatterChart"></div>
            </el-card>
        </el-row>
        <el-row><router-view></router-view></el-row>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    mounted() {
        this.showBarChart();
        this.showAreaStackChart();
        this.showNightingaleChart();
        this.showScatterChart();
    },
    methods: {
        showBarChart() {
            // var that = this
            // var barData
            console.log('111')
            // axios.get('/api/get_sp_dashboard_data').then(function(response){
                // var barData = response.data;
                // console.log(barData)
                // var xAxisData = [];
                // var yAxisData = []; 
                // for (var k in barData) {
                //     xAxisData.push(barData[k].sno);
                //     yAxisData.push(barData[k].sum);
                // }
                // let barChart = that.$echarts.init(that.$refs.barChart);
                // barChart.setOption({
                //     theme: "light",
                //     title: {text:'柱状图'},
                //     tooltip: {},
                //     xAxis:{
                //         data: xAxisData
                //     },
                //     yAxis:{},
                //     series:[{
                //         name:'count',
                //         type:'bar',
                //         data: yAxisData
                //     }]
                // });
            // })
        },
        showAreaStackChart() {
            let areaStackChart = this.$echarts.init(this.$refs.areaStackChart);
            areaStackChart.setOption({
                title: {text:'堆叠区域图'},
                tooltip: {},
                legend: {
                    data: ['a','b','c','d','e']
                },
                xAxis: {
                    data:['第一季度','第二季度','第三季度','第四季度']
                },
                yAxis: {},
                series: [
                    {
                        name: 'a',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [100,200,300,400]
                    },
                    {
                        name: 'b',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [238,123,222,310]
                    },                    {
                        name: 'c',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [150,232,30,400]
                    },                    {
                        name: 'd',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [120,132,90,210]
                    },                    {
                        name: 'e',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [230,120,334,301]
                    },
                ]
            })
        },
        showNightingaleChart() {
            let nightingaleChart = this.$echarts.init(this.$refs.nightingaleChart);
            nightingaleChart.setOption({
                title: {
                    text: '南丁格尔玫瑰图',
                    left: 'center'
                },
                legend: {
                    left: 'center',
                    top: 'bottom',
                    data: ['a','b','c','d','e']
                },
                series: {
                    name: '面积模式',
                    type: 'pie',
                    radius: [30,100],
                    center: ['50%','50%'],
                    roseType: 'area',
                    data: [
                        {value:Math.floor(Math.random()*100), name:'a'},
                        {value:Math.floor(Math.random()*100), name:'b'},
                        {value:Math.floor(Math.random()*100), name:'c'},
                        {value:Math.floor(Math.random()*100), name:'d'},
                        {value:Math.floor(Math.random()*100), name:'e'}
                    ]
                }
            })
        },
        showScatterChart() {
            var that = this
            axios.get('/api/get_sp_dashboard_data').then(function(response){
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
                // console.log("AXIOS:",typeof response.data['PFW'])
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
                console.log(dataPFW)
                // dataPFW.push(response.data['PFW']);
                // dataPFS.push(response.data['PFS']);
                // dataPFE.push(response.data['PFE']);
                var schema = [
                    {name: 'date', index: 0, text: '月份'},
                    {name: 'count_sno', index: 2, text: '消耗备件种类'},
                    {name: 'sum_sno', index: 1, text: '备件消耗总量'} 
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
                        text: "2017年各工厂备件消耗总量以及消耗种类总量图",
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
                        data: ['PFA1', 'PFA2', 'PFA3', 'PFE', 'PFS', 'PFN', 'PFY', 'PFH', 'PFW' ,'PFC'],
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
                        type: 'value',
                        name: '月份',
                        nameGap: 16,
                        nameTextStyle: {
                            color: '#fff',
                            fontSize: 14
                        },
                        max: 12,
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
                        name: '消耗备件种类',
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
                            max: 1500,
                            itemWidth: 30,
                            itemHeight: 120,
                            calculable: true,
                            precision: 0.1,
                            text: ['圆形大小：备件总消耗量'],
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
                let scatterChart = that.$echarts.init(that.$refs.scatterChart);   
                scatterChart.setOption(option);            
                });
        }
    }
}
</script>

<style>
    .el-row {
        margin-bottom: 20px;
    }
    .myChart {
        height: 400px;
        width: 400px;
    }
    .myChart2 {
        height: 600px;
        width: 1300px;
    }
    .analysiswrap {
        padding: 0px;
    }
</style>