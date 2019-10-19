<template>
<div id="nav">
  <b-navbar toggleable="sm" type="light" variant="white">
    <b-navbar-brand to="/">
      <img src="@/assets/img/Insight-Supply-Logo.png" alt="BV">
    </b-navbar-brand>

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-collapse is-nav id="nav_collapse">
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-navbar-nav>
          <b-nav-item to="/categories">Categories</b-nav-item>
          <b-nav-item to="/contact">Contact</b-nav-item>
          <b-nav-item to="/about">About</b-nav-item>
        </b-navbar-nav>

          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
import bNavbar from 'bootstrap-vue/es/components/navbar/navbar';
import bNavbarNav from 'bootstrap-vue/es/components/navbar/navbar-nav';
import bNavbarBrand from 'bootstrap-vue/es/components/navbar/navbar-brand';
import bNavbarToggle from 'bootstrap-vue/es/components/navbar/navbar-toggle';

import bNavForm from 'bootstrap-vue/es/components/nav/nav-form';
import bNavItem from 'bootstrap-vue/es/components/nav/nav-item';
import bNavItemDropdown from 'bootstrap-vue/es/components/nav/nav-item-dropdown';

import bCollapse from 'bootstrap-vue/es/components/collapse/collapse';
import bForm from 'bootstrap-vue/es/components/form/form';
import bFormGroup from 'bootstrap-vue/es/components/form-group/form-group';
import bFormInput from 'bootstrap-vue/es/components/form-input/form-input';
import bButton from 'bootstrap-vue/es/components/button/button';

import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown';
import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item';


export default {
  name: 'NavBar',
  components: {
    bNavbar,
    bNavbarNav,
    bNavbarBrand,
    bNavbarToggle,
    bNavForm,
    bNavItem,
    bNavItemDropdown,
    bCollapse,
    bDropdown,
    bDropdownItem,
  }
}

</script>

<style lang="scss">
@import "@/scss/styles.scss";


</style>
