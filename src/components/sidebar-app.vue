<template>
  <div class=" sidebar sidebar-homepage"  >
    
    
    

    
    
    <button class="accordion">Chapter 1</button>
    <div class="panel">
      <div>
        <div class="sidebar-app-panel-header">
          <p>Vowels: a,e,i,o,u</p>
        </div>
        <div>

        </div>
      </div>
      <button @click="updateValue('chapter1')" class="sidebar-app-accordion-btn">Play</button>

    </div>

    <button class="accordion">Chapter 2</button>
    <div class="panel">
      <div>
        <div class="sidebar-app-panel-header">
          <p>Numbers: 1-9</p>
        </div>
        <div>

        </div>
      </div>
      <button @click="updateValue('chapter2')" class="sidebar-app-accordion-btn">Play</button>

    </div>

    <button class="accordion">Chapter 3</button>
    <div class="panel">
      <div>
        <div class="sidebar-app-panel-header">
          <p>Words: Banana</p>
        </div>
        <div>

        </div>
      </div>
      <button @click="updateValue('chapter3')" class="sidebar-app-accordion-btn">Play</button>

    </div>

    <button class="accordion">Others</button>
    <div class="panel">
      <div>
        <div class="sidebar-app-panel-header">
          <p>Free Play</p>
        </div>
        <div>

        </div>
      </div>
      <button @click="updateValue('freeplay')" class="sidebar-app-accordion-btn">Play</button>

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
    name: 'sidebar-app',
    data: function () {
      return {
        // display: 'none',
        maxHeight: '30px'

      }
    },
    props: ['chapter'],
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
      updateValue: function (chapter) {
      this.$emit('input', chapter);
    }
     

    },
    
    
  }
</script>

<style>
  @import '../assets/style.css';
</style>

