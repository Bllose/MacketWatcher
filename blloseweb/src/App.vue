<script>
import BarChart from "./myComponents/bar.vue";
import PieChart from "./myComponents/pie.vue";
import Dynamic from "./myComponents/dynamic.vue";
import axios from 'axios';

export default {
  name: "About",
  components: { BarChart, PieChart, Dynamic },
  data() {
    return {
      flag: false,
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
      },
      objectData2: {
        categories: [],
        categories2: [],
        data: [],
        data2: []
      }
    }
  },
  mounted() {
    this.getSeries();
  },
  methods: {
    getSeries() {
      axios.defaults.crossDomain = true;
      axios.defaults.headers.common['Access-Control-Allow-Origin'] = true;
      axios.get('http://127.0.0.1:5000/volume',{headers: {'Access-Control-Allow-Origin': "true"}})
        .then(response => {
          console.log(response)
          resData = response['data']
          for (i = 0; i < 10; i++) {
            this.objectData2.categories.unshift(new Date(Number(resData[i][0])).toLocaleTimeString())
            let seller = Number(resData[i][1])
            let buyer = Number(resData[i][2])
            let total = seller + buyer
            this.objectData2.data2.unshift(buyer / total)
            this.objectData2.data.unshift(buyer)
          }
        })
        .catch(error => { });
      debugger
      this.objectData2.categories = (function () {
        let res = [];
        let len = 10;
        while (len--) {
          res.push(10 - len - 1);
        }
        return res;
      })();

      this.objectData2.categories2 = (function () {
        let res = [];
        let len = 10;
        while (len--) {
          res.push(10 - len - 1);
        }
        return res;
      })();

      this.objectData2.data = (function () {
        let res = [];
        let len = 10;
        while (len--) {
          res.push(Math.round(Math.random() * 1000));
        }
        return res;
      })();

      this.objectData2.data2 = (function () {
        let res = [];
        let len = 0;
        while (len < 10) {
          res.push(+(Math.random() * 10 + 5).toFixed(1));
          len++;
        }
        return res;
      })();
      this.flag = true;
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
    <dynamic :id="'dynamic'" :data="objectData2" v-if="flag"></dynamic>
    <bar-chart :id="'bar'" :data="objectData"></bar-chart>
    <pie-chart :id="'pie'" :data="objectData1"></pie-chart>
    <pie-chart :id="'pie1'" :data="objectData1"></pie-chart>

  </div>
</template>

<style></style>
