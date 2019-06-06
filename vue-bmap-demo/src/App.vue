<template>
  <div id="top-app">
    <router-view id="top-router"/>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
body,
html {
  margin: 0;
  display: flex;
  height: 100%;
  width: 100%;
}

#top-router {
  height: 100%;
  width: 100%;
}

#top-app {
  width: 100%;
  height: 100%;
  right: 0;
}
</style>
