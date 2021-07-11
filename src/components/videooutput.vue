<template>
  <div class="videoOutput">

    
    <img id="bg" src="" alt="">

  </div>
</template>

<script>
  export const eel = window.eel;
  eel.set_host( 'ws://localhost:9000' );

    // Expose the `sayHelloJS` function to Python as `say_hello_js`
  function sayHelloJS(x) {
    console.log( 'Hello from ' + x )
  }
  // WARN: must use window.eel to keep parse-able eel.expose{...}
  window.eel.expose( sayHelloJS, 'say_hello_js' );

  // Test calling sayHelloJS, then call the corresponding Python function
  sayHelloJS( 'Javascript World!' );
  eel.say_hello_py( 'Javascript World!' );
  function updateImageSrc(val) {
    const elem = document.getElementById('bg');
    elem.src = "data:image/jpeg;base64," + val
  }
  window.eel.expose(updateImageSrc);
  export default {
    name: 'videoOutput',
    data: function () {
      return {
        message: "",
        inputValue: "",
        response: ""
      }
    },
    mounted: function () {
      window.eel.video_feed()()
    },
    methods: {
      onClick() {
        // Passing values to Python
        eel.print_string(this.inputValue)((val) => {
          // Return response from Python
          this.response = val
        })
      },
      onClick2(){
        window.eel.video_feed()()

      }

    }
  }
</script>

<style>
  @import '../assets/style.css';
</style>

