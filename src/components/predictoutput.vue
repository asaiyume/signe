<template>
  <div class="predictoutput">

    <p id="b1g">dddd</p>

  </div>
</template>

<script>
  export const eel = window.eel;
  eel.set_host( 'ws://localhost:9000' );

  
  function updateTextSrc(val) {
    const elem = document.getElementById('b1g');
    console.log(val)
    elem.innerHTML = val
  }
  window.eel.expose(updateTextSrc);
  export default {
    name: 'predictoutput',
    data: function () {
      return {
        message: "",
        inputValue: "",
        response: ""
      }
    },
    mounted: function () {
      window.eel.predict_output()()
    },
    methods: {
      onClick() {
        // Passing values to Python
        eel.print_string(this.inputValue)((val) => {
          // Return response from Python
          this.response = val
        })
      },
      

    }
  }
</script>

<style>
  @import '../assets/style.css';
</style>

