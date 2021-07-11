<template>
  <div class="chapter1">
    
    <div class="row">
    
      <div class="chaptergame-prompt-div chapter-divs">
          
          <p class="chaptergame-text">Sign out the letters shown below to complete their progress bars!</p>

      </div>

    </div>
    
    <div class="row chaptergame-camera-div chapter-divs">

      <cvvideo/>

    </div>
    <div class="row chaptergame-outputbox chapter-divs">
      <div class="chaptergame-outputtext">
        
        <predictoutputgame :key="componentKey" class="chaptergame-outputtext-output"/>
        <!-- <p id="gamecounter">placeholder</p> -->
      </div>
      

    </div>
    
    <div class="row chapter-buttoncontainer chapter-divs">

      <div class="row chapter-buttondiv chapter-divs">

        <div class="col-sm-12 footer-buttons-div">
          <button class="footer-buttons" @click="forceRerender()">Reset</button>
        </div>
        
      </div>


    </div>
  </div>
  
</template>

<script>
// @ is an alias to /src
import cvvideo from '@/components/cvvideo.vue'
// import videoOutput from '@/components/videooutput.vue'
import predictoutputgame from '@/components/predictoutputgame.vue'

export default {
  name: 'chaptergame',
  components: {
    cvvideo,
    predictoutputgame,
    // videoOutput
  },
  data() {
    return {
      componentKey: 0,
    };
  },
  methods: {
    forceRerender() {
      this.componentKey += 1;
    }
  }
}
</script>
<style>
  @import '../assets/style.css';
</style>