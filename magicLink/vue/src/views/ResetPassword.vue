<template>
  <div class="container">
    <div class="modal-dialog">
      <div class="modal-content background-customizable modal-content-mobile">
        <div>
          <div class="banner-customizable">
            <center></center>
          </div>
        </div>
        <div class="modal-body">
          <div>
            <div>
              <form
                name="confirmforgotpasswordform"
                @submit.prevent="changepassword"
              >
                <br />
                <label for="new_password">New Password</label>
                <input
                  id="new_password"
                  v-model="newpassword"
                  class="form-control inputField-customizable"
                  type="password"
                  name="password"
                  required=""
                />

                <label for="confirm_password">Enter New Password Again</label>
                <input
                  id="confirm_password"
                  v-model="newpwddup"
                  class="form-control inputField-customizable"
                  type="password"
                  name="confirmPassword"
                  required=""
                />
                <br />
                <b-button variant="success" v-if="loading">
                  <span
                    class="spinner-border spinner-border-sm"
                    role="status"
                    aria-hidden="true"
                  ></span>
                  Changing...
                </b-button>
                <b-button
                  v-else
                  name="reset_password"
                  type="submit"
                  variant="success"
                >
                  Change Password
                </b-button>
                <p></p>
                <a class="redirect-customizable" href="/"> Return to login</a>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Auth } from "@aws-amplify/auth";

export default {
  name: "ResetPassword",
  data() {
    return {
      username: this.$route.query.username,
      code: this.$route.query.code,
      newpassword: "",
      newpwddup: "",
      loading: false,
      toastmsg: "",
    };
  },
  methods: {
    toast(msg, type = 'info', autoHide = true) {
          this.$bvToast.toast(msg, {
            title: type,
            toaster: "b-toaster-top-center",
            solid: true,
            static: true,
            appendToast: true,
            noAutoHide: !autoHide,
            variant: type === "info"? "success" : "warning",
          });
        },
    changepassword() {
      if (this.code.length < 6) {
        console.log("Incorrect code!");
      } else if (this.newpassword.length < 5) {
        alert("input valid password!");
      } else if (this.newpassword !== this.newpwddup) {
        alert("password not match!");
      } else {
        this.loading = true;
        Auth.forgotPasswordSubmit(this.username, this.code, this.newpassword)
          .then(() => {
            this.toast(`New password applied, please sign-in.`, "info", false);
            this.loading = false;
            this.$router.push("/");
          })
          .catch((err) => {
            this.toast(err.message, "warning", false);
            this.loading = false;
          });
      }
    },
  },
};
</script>