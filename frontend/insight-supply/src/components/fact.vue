<template>
  <div>
    <h3>{{title}}<h3>
      <p>{{body}}<p>
      <a href="source">{{source}}</a>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    title: {
      type: String,
      required: false,
    },
    body: {
      type: String,
      required: true,
    },
    source: {
      type: String,
      required: true,
    },
    categories: {
      type: Array,
      required: true,
    },
  },
  data: function(){
    return {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
