<template>
  <div class="homepage">





    <div>
          
      <SidebarHomePage/>
    </div>
    <div class="col-sm-12 main1">
      <HomePage/>

    </div>
  </div>
</template>

<script>
  // @ is an alias to /src
  import HomePage from '@/components/homepage.vue'
  import SidebarHomePage from '@/components/sidebar-homepage.vue'
  

  export default {
    name: 'homepage',
    components: {
      HomePage,
      SidebarHomePage
    }
  }

  
</script>
<style>
  @import '../assets/style.css';
</style>