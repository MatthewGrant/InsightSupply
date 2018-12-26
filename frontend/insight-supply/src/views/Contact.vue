<template>
  <div class="contact">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <b-container>
      <b-row class="text-center">
        <b-col class="p-3">
            <h2 class="page-title">Contact</h2>
        </b-col>
      </b-row>
      <hr></hr>
      <b-row class="text-center">
        <b-col class="p-3">
            <p>These insights are forever changing.</p>
            <p>If you would like to add an insight, please don't hesitate to reach out!</p>
        </b-col>
      </b-row>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-row align-v="end">
          <b-col cols="6">
            <b-form-group id="exampleInputGroup2"
                            label="Name *"
                            label-for="exampleInput2"
                            description="First Name">
              <b-form-input id="exampleInput2"
                              type="text"
                              v-model.trim="form.firstname"
                              required
                              placeholder="">
              </b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="6">
            <b-form-group id="exampleInputGroup2"
                            label=""
                            label-for="exampleInput2"
                            description="Last Name">
              <b-form-input id="exampleInput2"
                              type="text"
                              v-model.trim="form.lastname"
                              required
                              placeholder="">
              </b-form-input>
            </b-form-group>
          </b-col>
      </b-row>
        <b-form-row>
          <b-col cols="12">
              <b-form-group id="exampleInputGroup1"
                            label="Email address *"
                            label-for="exampleInput1"
                            description="We'll never share your email with anyone else.">
                <b-form-input id="exampleInput1"
                              type="email"
                              v-model="form.email"
                              required
                              placeholder="Enter email">
                </b-form-input>
              </b-form-group>
          </b-col>
      </b-form-row>
      <b-form-row>
        <b-col cols="12">
          <b-form-group id="subjectInputGroup"
                        label="Subject *"
                        label-for="subject"
                        description="">
              <b-form-textarea id="subject"
                               v-model="form.subject"
                               required
                               placeholder="">
              </b-form-textarea>
            </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row>
        <b-col cols="12">
          <b-form-group id="messageInputGroup"
                        label="Message *"
                        label-for="message"
                        description="">
              <b-form-textarea id="message"
                               v-model="form.message"
                               required
                               :rows="3"
                               placeholder="Say Hello!">
              </b-form-textarea>
            </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row>
        <b-button-group>
         <b-button type="submit" variant="primary">Submit</b-button>
         <b-button type="reset" variant="danger">Reset</b-button>
     </b-button-group>
      </b-form-row>
      </b-form>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import bForm from 'bootstrap-vue/es/components/form/form';
import bFormGroup from 'bootstrap-vue/es/components/form-group/form-group';
import bFormInput from 'bootstrap-vue/es/components/form-input/form-input';
import bFormTextarea from 'bootstrap-vue/es/components/form-textarea/form-textarea';
import bButton from 'bootstrap-vue/es/components/button/button';
import bContainer from 'bootstrap-vue/es/components/layout/container';
import bFormRow from 'bootstrap-vue/es/components/layout/form-row';
import bRow from 'bootstrap-vue/es/components/layout/row';
import bCol from 'bootstrap-vue/es/components/layout/col';

export default {
  name: 'contact',
  components: {
    bForm,
    bFormGroup,
    bFormInput,
    bFormTextarea,
    bButton,
  },
  props: {},
  data: function(){
    return {
        show: true,
        form: {
            firstname: '',
            lastname: '',
            email: '',
            subject: '',
            message: '',
        }
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset (evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.firstname = '';
      this.form.lastname = '';
      this.form.email = '';
      this.form.subject = '';
      this.form.message = '';
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => { this.show = true });
    }
  }
}
</script>
