<template>
  <div>
    <nav-bar />

    <div class="container section">
      <div class="columns">
        <div class="column is-8">
          <slot />
        </div>
      </div>
    </div>

    <footer-bar />
  </div>
</template>
<script>
import NavBar from "@/components/NavBar";
// import FooterBar from "@/components/FooterBar";
export default {
  components: {
    NavBar,
    // FooterBar
  }
};
</script>

