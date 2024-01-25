<script>
import BarChart from "./myComponents/bar.vue";
import PieChart from "./myComponents/pie.vue";
import Dynamic from "./myComponents/dynamic.vue";

export default {
  name: "About",
  components: { BarChart, PieChart, Dynamic },
  data() {
    return {
      objectData: {
        textTile: "父子组件传值echarts案例",
        totalText: '这是一个test',
        nameArray: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
        series: [],
      },
      objectData1: {
        textTile: "父子组件传值echarts案例Pie",
        totalText: '这是一个testPie',
        series: [],
      }
    }
  },
  mounted() {
    this.getSeries();
  },
  methods: {
    getSeries() {
      this.objectData.series.push({
        name: '温度',
        type: "bar",
        barWidth: "20%",
        data: ['32', '30', '28', '29', '36', '33', '25'],
        itemStyle: {
          normal: {
            //好，这里就是重头戏了，定义一个list，然后根据所以取得不同的值，这样就实现了，
            color: function (params) {
              // build a color map as your need.
              var colorList = [
                '#C1232B', '#B5C334', '#FCCE10', '#E87C25', '#27727B',
                '#FE8463', '#9BCA63', '#FAD860', '#F3A43B', '#60C0DD',
                '#D7504B', '#C6E579', '#F4E001', '#F0805A', '#26C0C0'
              ];
              return colorList[params.dataIndex]
            },
            label: {
              show: true,
              position: 'top',
              formatter: '{c}'
            }
          }
        }
      });

      this.objectData1.series.push({
            name: '数量',
            type: 'pie',
            label: {
              show: true
            },
            data: [
              {
                value: 335,
                name: '直接访问'
              },
              {
                value: 234,
                name: '联盟广告'
              },
              {
                value: 1548,
                name: '搜索引擎'
              }
            ],
            radius: ['40%', '70%']
      })
    }
  }
}
</script>

<template>
  <!-- <div>
    <Pie></Pie>
  </div> -->
  <div class="Box">
    <!--  调用子组件  对应子组件的id=bar和data=objectData数据绑定-->
    <dynamic :id="'dynamic'" :data="objectData1"></dynamic>
    <bar-chart :id="'bar'" :data="objectData"></bar-chart>
    <pie-chart :id="'pie'" :data="objectData1"></pie-chart>
    <pie-chart :id="'pie1'" :data="objectData1"></pie-chart>
    
  </div>
</template>

<style></style>
