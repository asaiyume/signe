<template>
  <div class="chapter1">
    
    
    <div class="row">
    
      <div class="cvvideo-div chapter-divs">
          <div class="cvvideo-div-div">
            <cvvideo/>

          </div>

      </div>

    </div>
    <div class="row chaptervideo-div chapter-divs">

    <iframe class="chaptervideo"
    src="https://www.youtube.com/embed/tgbNymZ7vqY">
    </iframe>

    </div>
    <div class="row chaptervideo-outputbox chapter-divs">

      <p>asd</p>

    </div>
    <div class="row chapter-buttoncontainer chapter-divs">

      <div class="row chapter-buttondiv chapter-divs">

        <div class="col-sm-4 footer-buttons-div">
          <button class="footer-buttons">Back</button>
        </div>
        <div class="col-sm-4 footer-buttons-div">
          <button class="footer-buttons">Restart</button>
        </div>
        <div class="col-sm-4 footer-buttons-div">
          <button class="footer-buttons">Continue</button>
        </div>
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