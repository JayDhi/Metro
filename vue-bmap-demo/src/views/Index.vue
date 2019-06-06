<template>
  <el-container style="width: 100%; height: 100%; solid #eee; display: flex; right:0;">
    <Sidebar></Sidebar>
    <el-container style="width: 100%" direction="vertical">
      <UserHeader></UserHeader>

      <el-container>
        <el-container>
          <SubwayMap></SubwayMap>

          <SwitchCard></SwitchCard>

          <el-footer height="250px">
            <chart></chart>
          </el-footer>
        </el-container>

        <CardSide></CardSide>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import UserHeader from "../components/UserHeader.vue";
import CardSide from "../components/CardSide.vue";
import Sidebar from "../components/Sidebar.vue";
import SubwayMap from "../components/SubwayMap.vue";
import Chart from "../components/Chart.vue";
import SwitchCard from "../components/SwitchCard.vue";

export default {
  name: "Index",
  components: {
    Sidebar,
    UserHeader,
    SubwayMap,
    Chart,
    CardSide,
    SwitchCard
  }
};
</script>

<style>
body,
html {
  margin: 0;
  display: flex;
  height: 100%;
}
</style>
