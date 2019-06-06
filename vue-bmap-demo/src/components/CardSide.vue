<template>
  <el-aside id="card-side">
    <InfoCard v-for="(infoCard, index) in infoCards" :infoCard="infoCard" :key="index"></InfoCard>
  </el-aside>
</template>

<script>
import InfoCard from "./InfoCard.vue";
import axios from "axios";

export default {
  name: "CardSide",
  components: { InfoCard },
  props: {},
  data() {
    return {
      infoCards: []
    };
  },
  mounted() {
    axios
      .get("demo.mhtt1123.cn/infoCards")
      .then(response => (this.infoCards = response.data));
  }
};
</script>

<style scoped>
#card-side {
  float: right;
  right: 0%;
  width: 300px;
}
</style>
