<script>
export default {
    name: "barChart",
    props: ["id", "data"], //接受从父组件传回的值
    data() {
        return {}
    },
    //实时监听父组件传过来的值
    //然后执行drawBar方法 重新绘制柱状图
    watch: {
        data: {
            handler(value) {
                this.drawBar(value)
            },
            deep: true//深度监听
        }
    },
    mounted() {
        this.drawBar(this.data)
    },
    methods: {
        drawBar({
            textTile = '',  // 标题 柱状图options里需要用的数据这里作为参数从data里面取值
            totalText = '',//标签
            nameArray = [],//x轴的数据
            series = [],//series的数据
        } = {}  //作为一个整体的参数
        ) {   //现在是真正开始画图表的时候
            let barBox = this.$echarts.init(document.getElementById(this.id));
            //给图表一个指定的容器dom
            let option = { //设置图表的options
                //1.先设置图表的标题
                title: {
                    text: textTile,//使用父组件传过来的数据
                    textStyle: {
                        color: '#00CAB1',
                        fontsize: 20
                    }
                },
                //2.直角坐标系绘图区域
                grid: {
                    top: '25%',
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                //3.x轴相关结构
                xAxis:
                {
                    type: "category",
                    data: nameArray,
                    axisLine: {
                        show: true,
                        lineStyle: {
                            // color: 'white',
                        }
                    },
                    axisLabel: {
                        interval: 0,
                        fontSize: 10,
                        rotate: 40
                    },
                    boundaryGap: true,
                    axisTick: {
                        alignWithLabel: true
                    },
                },
                //4.y轴相关结构
                yAxis:
                {
                    type: "value",
                    axisLine: {
                        show: true,
                        lineStyle: {
                            // color: 'white'
                        }
                    },
                    splitLine: {
                        show: false
                    },
                    // boundaryGap: true,
                },
                //5.固定说明文字
                graphic: [{
                    type: 'group',
                    id: 'textGroup1',
                    left: '1%',
                    top: '15%',

                    // bounding: 'raw',
                    children: [
                        {
                            type: 'text',
                            z: 100,
                            top: 'middle',
                            left: 'center',
                            style: {
                                // text: ['注册总人数为'+totalNumber],
                                text: totalText,
                                fontSize: 15,
                                fill: '#000',
                            }
                        }

                    ]
                }],
                //6.图表的相关series设置
                series: series,
            };
            //柱状图的相关结构已经定义好了调用setoption
            barBox.setOption(option, true);
            console.log(option)
            window.addEventListener("resize", function () {
                barBox.resize();
            })
        }
    }
}
</script>

<template>
    <div class="box">
        <!--    子组件需要得到的值  id 和 data-->
        <div v-bind:id=id ref="data" style="width: 300px;height: 300px"></div>
    </div>
</template>

<style></style>
