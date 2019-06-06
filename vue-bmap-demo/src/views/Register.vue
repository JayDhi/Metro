<template>
  <div class="body">
    <div class="header">
      <div class="container">
        <div class="row">
          <div class="logo span4">
            <h1>
              <a href>
                Register
                <span class="red">.</span>
              </a>
            </h1>
          </div>
          <div class="links span8">
            <a class="home" href rel="tooltip" data-placement="bottom" data-original-title="Home"></a>
            <a class="blog" href rel="tooltip" data-placement="bottom" data-original-title="Blog"></a>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="copyrights">Collect from <a href="http://www.cssmoban.com/"  title="网站模板">网站模板</a></div> -->

    <div class="register-container container">
      <div class="row">
        <!-- <div class="iphone span5">
                    <img src="img/iphone.png" alt="">
        </div>-->
        <div class="register span6">
          <form action method="post">
            <h2>
              REGISTER TO
              <span class="red">
                <strong>iAPP</strong>
              </span>
            </h2>
            <label for="firstname">First Name</label>
            <input
              type="text"
              id="firstname"
              name="firstname"
              placeholder="enter your first name..."
            >
            <label for="lastname">Last Name</label>
            <input type="text" id="lastname" name="lastname" placeholder="enter your first name...">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="choose a username...">
            <label for="email">Email</label>
            <input type="text" id="email" name="email" placeholder="enter your email...">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="choose a password...">
            <button type="submit">REGISTER</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped src="../assets/css/reg_style.css"></style>
<style scoped src="../assets/bootstrap/css/bootstrap.min.css"></style>




