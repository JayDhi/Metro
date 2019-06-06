<template>
  <el-carousel
    height="100px"
    id="switch-card"
    :loop="false"
    :autoplay="false"
    indicator-position="none"
  >
    <el-carousel-item v-for="item in 4" :key="item">
      <h3 class="small">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  name: "SwitchCard",
  props: {
    leftTop: Object,
    rightBottom: Object
  }
};
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 100px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

#switch-card {
  position: fixed;
  padding: 0;
  margin: 0;
  width: 300px;
  height: 100px;
}
</style>