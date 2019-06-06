<template>
  <!-- <div id="login">
    <h1>登录界面</h1>用户名：
    <Input/>
    <br>密码：
    <Input/>
    <br>
    <button @click="login">登录</button>
  </div>-->
  <div class="login_body">
    <!-- <script>
  $(document).ready(function(c) {
    $(".close").on("click", function(c) {
      $(".login-form").fadeOut("slow", function(c) {
        $(".login-form").remove();
      });
    });
  });
    </script>-->
    <!--SIGN UP-->
    <h1>Login</h1>
    <div class="login-form">
      <div class="close"></div>
      <div class="head-info">
        <label class="lbl-1"></label>
        <label class="lbl-2"></label>
        <label class="lbl-3"></label>
      </div>
      <div class="clear"></div>
      <div class="avtar">
        <img src="../assets/images/avtar.png">
      </div>
      <form>
        <input
          type="text"
          class="text"
          value="Username"
          onfocus="this.value = '';"
          onblur="if (this.value == '') {this.value = 'Username';}"
        >
        <div class="key">
          <input
            type="password"
            value="Password"
            onfocus="this.value = '';"
            onblur="if (this.value == '') {this.value = 'Password';}"
          >
        </div>
      </form>
      <div class="signin">
        <input type="submit" value="Login" @click="login">
      </div>
    </div>
    <div class="copy-rights"></div>
  </div>
</template>


<script>
import Axios from "axios";
export default {
  methods: {
    login() {
      Axios.get("http://127.0.0.1:8000/Station/get_station/").then(response =>
        console.log(response.data)
      );
      // this.$router.replace("/");
    }
  }
};
</script>

<style scoped src="../assets/css/login_style.css">
