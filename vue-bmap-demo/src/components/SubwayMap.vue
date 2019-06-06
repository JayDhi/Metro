<template>
  <el-main>
    <iframe src="./map.html" frameborder="0" id="map-frame"></iframe>
  </el-main>
</template>

<script>
export default {
  name: "SubwayMap"
};
</script>

<style scoped>
#map-frame {
  height: 99%;
  width: 100%;
}

.el-main {
  margin: 0;
  padding: 0;
}
</style>
