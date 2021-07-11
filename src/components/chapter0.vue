<template>
  <div class="chapter0">
    
    
    <div class="row chapter-divs chapter0-header">
      <div class="col-sm-8 chapter0-headerdiv">
        <p class="chapter0-headertext">Begin Learning</p>
        <p class="chapter0-headertext2">Watch the tutorial video below to get started!</p>

      </div>
      <div class="col-sm-4 cvvideo-div2">
            <div class="cvvideo-div-div2">
            <cvvideo/>

          </div>

      </div>
      <!-- <div class="cvvideo-div chapter-divs">
          <div class="cvvideo-div-div">
            <cvvideo/>

          </div>

      </div> -->

    </div>
    <div class="row chaptervideo-div chapter-divs">

    <iframe class="chaptervideo"
    src="https://www.youtube.com/embed/dQw4w9WgXcQ">
    </iframe>

    </div>
    <!-- <div class="row chaptervideo-outputbox chapter-divs">

      <p>chapter0</p>

    </div> -->
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
      </div>


    </div>

  </div>
  
</template>

<script>
// @ is an alias to /src
import cvvideo from '@/components/cvvideo.vue'

export default {
  name: 'chapter1',
  components: {
    cvvideo
  }
}
</script>
<style>
  @import '../assets/style.css';
</style>