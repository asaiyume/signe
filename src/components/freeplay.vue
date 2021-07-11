<template>
  <div class="freeplay">
    
    
    <div class="row">
    
      <div class="cvvideo-div chapter-divs">
          
          <!-- <cvvideo/> -->

      </div>

    </div>
    <div class="row chaptervideo-div chapter-divs">

      <div class="chaptervideo-freeplay">
        <div class="cvvideo-div-div-freeplay">
            <cvvideo/>

          </div>
      </div>

    </div>
    <div class="row chaptervideo-outputbox chapter-divs">

      <p>Free Play</p>

    </div>
    

  </div>
  
</template>

<script>
// @ is an alias to /src
import cvvideo from '@/components/cvvideo.vue'

export default {
  name: 'chapter3',
  components: {
    cvvideo
  }
}
</script>
<style>
  @import '../assets/style.css';

  /* #bg{
    height: 100% !important;
    max-height: 100% !important;
  }

  .cvvideo{
    height:100%;
  } */
</style>