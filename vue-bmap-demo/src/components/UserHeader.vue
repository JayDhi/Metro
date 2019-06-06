<template>
  <el-header>
    <el-dropdown>
      <i class="el-icon-view" style="margin-right: 15px"></i>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>回放</el-dropdown-item>
        <el-dropdown-item divided>线路</el-dropdown-item>
        <el-dropdown-item divided>拥堵</el-dropdown-item>
        <el-dropdown-item divided>收藏</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <el-dropdown>
      <i class="el-icon-setting" style="margin-right: 15px"></i>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>退出</el-dropdown-item>
        <el-dropdown-item divided>详细</el-dropdown-item>
        <el-dropdown-item divided>我的</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <span>
      <el-button type="primary" size="small" @click="login">登录</el-button>
    </span>
  </el-header>
</template>

<script>
export default {
  name: "UserHeader",
  methods: {
    login() {
      this.$router.replace("/login");
    }
  }
};
</script>

<style scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
  text-align: right;
  font-size: 12px;
}
</style>
