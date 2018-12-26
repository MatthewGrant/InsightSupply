<template>
  <!-- <div class="about"> -->
    <b-container>
        <b-row class="text-center">
            <b-col class="p-3">
            <h2 class="page-title">About</h2>
            </b-col>
        </b-row>
        <hr></hr>
        <b-row class="text-center">
            <b-col class="p-3" md="6" offset-md="3">
            <p> <b>Insight Supply</b> is a resource for insights and facts to faciltate change
                and positively impact the world.
            </p>
            </b-col>
        </b-row>
        <b-row class="text-center">
            <b-col>
            <p> Just connect the dots.</p>
            </b-col>
        </b-row>
        <b-row class="text-center">
            <b-col class="p-3" md="6" offset-md="3">
            <p style="font-size: 12px"> We strive to curate information with reliable
             to avoid inaccuracy of misinformation sources. Please review all sources
            for credibility and further information.
            Reach out if you have any questionsor concerns about an insight.</p>
            </b-col>
        </b-row>
    </b-container>
  <!-- </div> -->
</template>
<script>
export default {
  name: 'about',
  components: {

  },
  props: {},
  data: function(){
    return {

    }
  }
}

</script>
<style scoped type="scss">
@import "../scss/utilities/_variables.scss";
h1 {
  color: $bg-accent;
}
</style>
