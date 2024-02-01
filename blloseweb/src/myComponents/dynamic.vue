<script>
let count = 11;
let localCat = []
let localCat2 = []
let localData = []
let localData2 = []

export default {
    props: ["id", "data"], //接受从父组件传回的值
    mounted() {
        this.drawBar(this.data)
    },
    methods: {
        drawBar({
            categories = [],
            categories2 = [],
            data = [],
            data2 = [],
        } = {}  //作为一个整体的参数
        ) {
            localCat = categories;
            localCat2 = categories2;
            localData = data;
            localData2 = data2;
            let myChart = this.$echarts.init(document.getElementById(this.id));
            let option = {
                title: {
                    text: 'Dynamic Data'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        label: {
                            backgroundColor: '#283b56'
                        }
                    }
                },
                legend: {},
                toolbox: {
                    show: true,
                    feature: {
                        dataView: { readOnly: false },
                        restore: {},
                        saveAsImage: {}
                    }
                },
                dataZoom: {
                    show: false,
                    start: 0,
                    end: 100
                },
                xAxis: [
                    {
                        type: 'category',
                        boundaryGap: true,
                        data: localCat
                    },
                    {
                        type: 'category',
                        boundaryGap: true,
                        data: localCat2
                    }
                ],
                yAxis: [
                    {
                        type: 'value',
                        scale: true,
                        name: 'Price',
                        max: 30,
                        min: 0,
                        boundaryGap: [0.2, 0.2]
                    },
                    {
                        type: 'value',
                        scale: true,
                        name: 'Order',
                        max: 1200,
                        min: 0,
                        boundaryGap: [0.2, 0.2]
                    }
                ],
                series: [
                    {
                        name: 'Dynamic Bar',
                        type: 'bar',
                        xAxisIndex: 1,
                        yAxisIndex: 1,
                        data: localData
                    },
                    {
                        name: 'Dynamic Line',
                        type: 'line',
                        data: localData2
                    }
                ]
            };

            myChart.setOption(option, true);

            setInterval(function () {
                let axisData = new Date().toLocaleTimeString().replace(/^\D*/, '');
                localData.shift();
                localData.push(Math.round(Math.random() * 1000));
                localData2.shift();
                localData2.push(+(Math.random() * 10 + 5).toFixed(1));
                localCat.shift();
                localCat.push(axisData);
                localCat2.shift();
                localCat2.push(count++);
                myChart.setOption({
                    xAxis: [
                        {
                            data: localCat
                        },
                        {
                            data: localCat2
                        }
                    ],
                    series: [
                        {
                            data: localData
                        },
                        {
                            data: localData2
                        }
                    ]
                });
            }, 2100);
        }
    }
}
</script>

<template>
    <div class="box">
        <!--    子组件需要得到的值  id 和 data-->
        <div v-bind:id=id style="width: 600px;height: 400px"></div>
    </div>
</template>

<style></style>