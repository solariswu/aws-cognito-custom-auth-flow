<template>
  <div class="container">
    <div class="modal-dialog">
      <div
        class="modal-content background-customizable modal-content-mobile visible-xs visible-sm"
      >
        <div>
          <div class="banner-customizable">
            <center></center>
          </div>
        </div>
        <div class="modal-body">
          <div>
            <center>
              <b-spinner variant="primary" label="Spinning" />
              <p></p>
              <span>
                Loading
                <b-icon icon="three-dots" animation="cylon"></b-icon>
              </span>
            </center>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {Auth} from '@aws-amplify/auth';
import {Hub} from '@aws-amplify/core';

export default {
  name: 'Landing',
  mounted: function() {

    Hub.listen('auth', ({payload: {event, data}}) => {
      console.log('auth hosted ui Hub event', event);
      switch (event) {
        case 'cognitoHostedUI':
          Auth.currentAuthenticatedUser().then((userData) => {
            console.log('user', userData);
            this.$router.push('/userinfo');
          });
          break;
        case 'signOut':
          this.$$router.push('/');
          break;
        case 'signIn_failure':
        case 'cognitoHostedUI_failure':
          console.log('Sign in failure', data);
          this.$router.push('/');
          break;
      }
    });
  },
  methods: {
  },
};
</script>
