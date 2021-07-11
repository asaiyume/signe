<template>
  <div class=" sidebar sidebar-homepage" >
    
    
    <div class="sidebar-homepage-header">
      <div class="sidebar-homepage-header-contents ">

        <p class="sidebar-homepage-header-contents-text1">Welcome</p>
        <p class="sidebar-homepage-header-contents-text2">Li Zibin</p>
      </div>
      
    </div>

    
    
    <button class="accordion">About us</button>
    <div class="panel">
      <p>Lorem ipsum...</p>
    </div>

    <!-- <button class="accordion"></button>
    <div class="panel">
      <p>Lorem ipsum...</p>
    </div> -->

    <button class="accordion">Contact us</button>
    <div class="panel">
      <p>Lorem ipsum...</p>
    </div>


    

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
  
  const acc = document.getElementsByClassName("accordion");
  let i;

  




  export default {
    name: 'sidebar-homepage',
    data: function () {
      return {
        // display: 'none',
        maxHeight: '30px'
      }
    },
    mounted: function () {
      for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        const panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      });
  }
    },
    computed: {
      
      
      
    },
    methods: {
     

    },
    
    
  }
</script>

<style>
  @import '../assets/style.css';
</style>

