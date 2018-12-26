<template>
  <b-container fluid>
   <b-carousel id="carousel" v-on:left="slideNum--" v-on:right="slideNum++"
      controls
      background="#FFFFFF"
      :interval="5000"
      img-width="90vw"
      img-height="40vw"
      v-model="slideNum"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd">
    <template v-if="searchFilteredInsights.length > 0">
      <template v-for="insight in searchFilteredInsights">
        <b-carousel-slide id="fact"
          :key="insight.id"
          :id="insight.id"
          :caption="insight.caption"
          img-blank
          :img-blank-color="insight.category.color"
          img-alt="Blank image">
            <a target="_blank" :href="insight.source_url">Source</a>
        </b-carousel-slide>
      </template>
    </template>
    <template v-else-if="insights.length > 0">
      <template v-for="insight in insights">
        <b-carousel-slide id="fact"
            :key="insight.id"
            :id="insight.id"
            :caption="insight.caption"
            img-blank
            :img-blank-color="insight.category.color"
            img-alt="Blank image">
              <a target="_blank" :href="insight.source_url">Source</a>
        </b-carousel-slide>
      </template>
    </template>
    <template v-else>
      <b-carousel-slide id="fact"
          caption="No Results..."
          img-blank
          img-blank-color="black"
          img-alt="Blank image">
            <a target="_blank" href="http://erinevon.com">Source</a>
        </b-carousel-slide>
    </template>
  </b-carousel>
  <div id="category-list">
    <b-row class="pt-3 ml-3 mr-3">
      <b-form-checkbox-group buttons button-variant="link" size="sm" id="checkboxes" name="categories" v-model="selectedCategories">
      <template v-for="category in categories">
        <b-form-checkbox :value="category.name">{{category.name}}</b-form-checkbox>
      </template>
    </b-form-checkbox-group>
    </b-row>
  </div>
  <b-row class="mt-3 ml-3 mr-3 pt-3 pb-3">
    <b-input-group>
      <b-form-input v-model="searchFilter" size="md" type="text" placeholder="Search"/>
      <!-- <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button> -->
    </b-input-group>
  </b-row>

</b-container>
</template>

<script>
  import axios from 'axios';
  import Vue from 'vue';
  import bCarousel from 'bootstrap-vue/es/components/carousel/carousel';
  import bCarouselSlide from 'bootstrap-vue/es/components/carousel/carousel-slide';

export default {
  name: 'HelloWorld',
  components: {
    bCarousel,
    bCarouselSlide,
  },
  props: {
    msg: String
  },
  data: function(){
    return {
      slideNum: 0,
      sliding: null,
      loading: true,
      errored: false,
      categories: [],
      selectedCategories: null,
      searchFilter: '',
      insights: [],
    }
  },
  created: function () {
    axios.all([this.getCategories(), this.getInsights()])
      .then(axios.spread((categories, insights) => {
        // Both requests are now complete
        console.log(categories.data.results)
        console.log(insights.data.results)
        this.categories = categories.data.results
        this.insights = insights.data.results
      }))
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(()=> this.loading = false);
  },
  mounted() {
    // set random active category or display all in carousel

  },
  computed: {
    searchFilteredInsights() {
      this.selectedCategories = []
      return this.insights.filter(fact => {
        return fact.caption.toLowerCase().indexOf(this.searchFilter.toLowerCase())>=0;});
    },
    // selectedCategoryInsights(){
    //   console.log(this.insights.filter(cat => this.selectedCategories.includes(cat.name)))
    //   return this.categories.filter(cat => this.selectedCategories.includes(cat.name)).insights;
    // }
  },
  methods: {
    getCategories(){
      return axios.get('api/v1/categories/?format=json')
    },
    getInsights(){
      return axios.get('api/v1/insights/?format=json')
    },
    getInsightsByCategory(categoryName){
      axios
        .get(`api/v1/insights/?category=${categoryName}`)
        .then(response => {
          var catergory = this.categories.find(cat => cat.name === categoryName)
          Vue.set(catergory, 'insights', response.data.results)
        })
        .catch(error => {
          console.log(error)
          this.errored = true
        })
        .finally(() => this.loading = false)
    },
    getRandomCategoryName(arr){
      var randomNum = Math.floor(Math.random() * (+arr.length - +0)) + +0;
      var category = arr.find(cat => cat.id === randomNum)
      return category ? category.name : null
    },
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    filterBy(evt){
      console.log(evt.target.text.toLowerCase())
      this.filteredFacts = this.facts.filter(fact => fact.category.toLowerCase() === evt.target.text.toLowerCase())
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.carousel-inner {
  max-width:1440px;
  max-height:500px !important;
  a {
    color: white;
  }
}

.btn-group{
  display: -webkit-inline-box;
}

.btn-link {
  color: #000;
  &.active {
    border-color: gray;
  }
  &:hover{
    color: pink;
  }
}

</style>
