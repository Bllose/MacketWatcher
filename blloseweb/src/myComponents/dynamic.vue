<script>
let categories = (function () {
    let now = new Date();
    let res = [];
    let len = 10;
    while (len--) {
        res.unshift(now.toLocaleTimeString().replace(/^\D*/, ''));
        now = new Date(+now - 2000);
    }
    return res;
})();
let categories2 = (function () {
    let res = [];
    let len = 10;
    while (len--) {
        res.push(10 - len - 1);
    }
    return res;
})();
let data = (function () {
    let res = [];
    let len = 10;
    while (len--) {
        res.push(Math.round(Math.random() * 1000));
    }
    return res;
})();
let data2 = (function () {
    let res = [];
    let len = 0;
    while (len < 10) {
        res.push(+(Math.random() * 10 + 5).toFixed(1));
        len++;
    }
    return res;
})();
let count = 11;


export default {
    props: ["id", "data"], //接受从父组件传回的值
    methods: {
        drawBar({
            textTile = '',  // 标题 柱状图options里需要用的数据这里作为参数从data里面取值
            totalText = '',//标签
            nameArray = [],//x轴的数据
            series = [],//series的数据
        } = {}  //作为一个整体的参数
        ) {
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
                        data: categories
                    },
                    {
                        type: 'category',
                        boundaryGap: true,
                        data: categories2
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
                        data: data
                    },
                    {
                        name: 'Dynamic Line',
                        type: 'line',
                        data: data2
                    }
                ]
            };

            myChart.setOption(option, true);

            setInterval(function () {
                let axisData = new Date().toLocaleTimeString().replace(/^\D*/, '');
                data.shift();
                data.push(Math.round(Math.random() * 1000));
                data2.shift();
                data2.push(+(Math.random() * 10 + 5).toFixed(1));
                categories.shift();
                categories.push(axisData);
                categories2.shift();
                categories2.push(count++);
                myChart.setOption({
                    xAxis: [
                        {
                            data: categories
                        },
                        {
                            data: categories2
                        }
                    ],
                    series: [
                        {
                            data: data
                        },
                        {
                            data: data2
                        }
                    ]
                });
            }, 2100);
        }
    },
    mounted() {
        this.drawBar(this.data)
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