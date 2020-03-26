<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex flex-center" style="font-family: Lato;">
        <!--        <div id="particles-js"></div>-->
        <q-card :style="$q.platform.is.desktop ? 'width:35%;' : ''"
                class="row my-card items-center q-pa-none q-ma-none shadow-24">
          <q-card-section class="col-md-12 col-lg-12 col-sm-12 col-xs-12 q-pt-none float-left">
            <q-card-section class="items-center">
              <div>
                <div v-if="!$q.platform.is.desktop" class="text-weight-bolder text-center q-mb-md text-primary text-h6">
                  Quasar Shopping
                </div>
                <q-form :style="$q.platform.is.desktop ? 'width:100%;margin: auto;' : 'margin: auto;'"
                        class="q-gutter-md">
                  <div class="text-weight-bold q-mb-xs" style="font-size: 30px;">Log in</div>
                  <br/>
                  <span class="text-weight-bold text-grey-7">Connect with a social network</span>

                  <div class="row">
                    <div class="col-6 q-px-xs">
                    <q-btn style="background-color: #4367b0" class="full-width text-white q-py-xs text-weight-bold">
                      <q-icon left size="2em" name="img:https://cdn0.iconfinder.com/data/icons/yooicons_set01_socialbookmarks/512/social_facebook_box_white.png"/>
                      <div>Facebook</div>
                    </q-btn>
                    </div>
                    <div class="col-6 q-px-xs">
                    <q-btn style="background-color: #4585f1" class="full-width text-white q-py-xs text-weight-bold">
                      <q-icon left size="2em" name="img:https://cdn.freebiesupply.com/logos/large/2x/google-g-2015-logo-png-transparent.png"/>
                      <div>Google</div>
                    </q-btn>
                    </div>
                  </div>
                  <q-separator class="q-mt-lg q-mb-md"></q-separator>
                  <span class="text-grey-7">Log in with your Email</span>
                  <q-input
                    dense
                    outlined
                    v-model="username"
                    label="Username"
                    lazy-rules
                  />

                  <q-input
                    dense
                    type="password"
                    outlined
                    v-model="password"
                    label="Password"
                    lazy-rules
                  />
                  <q-checkbox class="text-grey-8" dense v-model="remember_me" label="Remember me"/>
                  <div>
                    <q-btn class="text-capitalize text-white text-weight-bold" size="md" style="width:75px" dense label="Login" to="/"
                           type="button"
                           color="primary"/>
                    <!--<q-btn class="float-right text-blue-9 text-capitalize" size="sm" style="width:75px;border: 1px solid #36669e;" dense label="Sign Up"-->
                    <!--type="button"/>-->
                  </div>
                </q-form>

              </div>
            </q-card-section>
          </q-card-section>

        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
  export default {
    data() {
      return {
        username: 'Nikita',
        password: 'Nikita@12345',
        remember_me: false
      }
    },
    mounted() {

    },
    computed: {
      win_width() {
        return this.$q.screen.width - 59;
      },
      win_height() {
        return this.$q.screen.height - 0;
      }
    }
  }
</script>
<style>
  .my-card {
    /*width: 55%;*/
    height: 30%;
  }

  .login-form {
    position: absolute;
  }
</style>
