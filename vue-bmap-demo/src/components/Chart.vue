<template>
  <div id="chart"></div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "Chart",
  mounted() {
    // mounted() {
    // var event = 10;
    var chart = echarts.init(document.getElementById("chart"));

    var option = {
      title: {
        text: "入站量和出站量",
        subtext: "火车东站" // TODO 替换成真实站点
      },
      tooltip: {
        trigger: "axis"
      },
      legend: {
        data: ["入站量", "出站量"]
      },
      toolbox: {
        show: true,
        feature: {
          mark: { show: true },
          dataView: { show: true, readOnly: false },
          magicType: { show: true, type: ["line", "bar"] },
          restore: { show: true }
          // saveAsImage: { show: true }
        }
      },
      calculable: true,
      xAxis: [
        {
          type: "category",
          data: [
            // TODO
            // TODO 换成真实的时间，左右各6个时间片
            "16:30",
            "16:40",
            "16:50",
            "17:00",
            "17:10",
            "17:20",
            "17:30",
            "17:40",
            "17:50",
            "18:00",
            "18:10",
            "18:20"
          ]
        }
      ],
      yAxis: [
        {
          type: "value"
        }
      ],
      series: [
        {
          name: "入站量",
          type: "bar",
          data: [
            // TODO 换成真实数据
            2.0,
            4.9,
            7.0,
            23.2,
            25.6,
            76.7,
            135.6,
            162.2,
            32.6,
            20.0,
            6.4,
            3.3
          ],
          markPoint: {
            data: [
              { type: "max", name: "最大值" }
              // { type: "min", name: "最小值" }
            ]
          },
          markLine: {
            data: [{ type: "average", name: "平均值" }]
          }
        },
        {
          name: "出站量",
          type: "bar",
          data: [
            2.6,
            5.9,
            9.0,
            26.4,
            28.7,
            70.7,
            175.6,
            182.2,
            48.7,
            18.8,
            6.0,
            2.3
          ],
          markPoint: {
            data: [
              // { type: "max", name: "最大值" },
              // { type: "min", name: "最小值" }
            ]
          }
        }
      ]
    };
    chart.setOption(option);
    window.addEventListener("message", function(e) {
      if (e.source == window.frames[0]) {
        var station_name = e.data;
        if (!station_name.endsWith("站")) {
          station_name.concat("站");
        }
        option.title.subtext = station_name;
        // use get method to get data predicted by model
        // option.xAxis// TODO
        // option.series[0] [1]// TODO
        option.series[0].data.reverse(); // test
        option.series[1].data.reverse();
        // console.log(option.series);
        chart.setOption(option);
      }
    });
  }
};
</script>
<style>
#chart {
  position: relative;
  height: 100%;
  width: 100%;
}
</style>
