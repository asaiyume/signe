<template>
  <div class="chapter1">
    
    
    <div class="row">
    
      <div class="cvvideo-div chapter-divs">
          
          <div class="cvvideo-div-div">
            <cvvideo/>
            <!-- <videoOutput/> -->

          </div>

      </div>

    </div>
    <div class="row chaptervideo-div chapter-divs">

    <iframe class="chaptervideo"
    src="https://www.youtube.com/embed/x0OA2V35g8g">
    </iframe>

    </div>
    <div class="row chaptervideo-outputbox chapter-divs">

      <!-- <predictoutput/> -->
      <p>Watch the video to learn, and click on "Start Practice" to continue.</p>

    </div>
    <div class="row chapter-buttoncontainer chapter-divs">

      <div class="row chapter-buttondiv chapter-divs">

        <!-- <div class="col-sm-4 footer-buttons-div">
          <button class="footer-buttons">Back</button>
        </div>
        <div class="col-sm-4 footer-buttons-div">
          <button class="footer-buttons">Restart</button>
        </div>
        <div class="col-sm-4 footer-buttons-div">
          <button class="footer-buttons">Continue</button>
        </div> -->
        <div class="col-sm-12 footer-buttons-div">
          <button @click="updateValue('chaptergame')" class="footer-buttons">Start practice!</button>
        </div>
      </div>


    </div>
  </div>
  
</template>

<script>
// @ is an alias to /src
import cvvideo from '@/components/cvvideo.vue'
// import videoOutput from '@/components/videooutput.vue'
// import predictoutput from '@/components/predictoutput.vue'

export default {
  name: 'chapter2',
  components: {
    cvvideo,
    // predictoutput,
    // videoOutput
  },
  props: ['chapter'],

  methods: {
      updateValue: function (chapter) {
      this.$emit('input', chapter);
    }
     

  },
}
</script>
<style>
  @import '../assets/style.css';
</style>