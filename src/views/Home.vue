<template>
  <div class="home">
    <div class="sidebar">
      <!-- <p>Parent value: {{chaptervalue}}</p> -->

      <SidebarApp v-model="chaptervalue"></SidebarApp>
    </div>
    <div class="col-sm-12 main1" >
      <div :is="chaptervalue" v-model="chaptervalue"></div>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import chapter0 from '@/components/chapter0.vue'
import chapter1 from '@/components/chapter1.vue'
import chapter2 from '@/components/chapter2.vue'
import chapter3 from '@/components/chapter3.vue'
import freeplay from '@/components/freeplay.vue'
import chaptergame from '@/components/chaptergame.vue'


import SidebarApp from '@/components/sidebar-app.vue'

export default {
  name: 'Home',
  components: {
    chapter0,
    chapter1,
    chapter2,
    chapter3,
    freeplay,
    chaptergame,
    SidebarApp
  },
  data: function() {
    return{
      currentComponent: 'chapter0',
      chaptervalue: 'chapter0'
    }

  }
}
</script>
<style>
  @import '../assets/style.css';
</style>