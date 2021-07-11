<template>
  <div class="progresscircle" >
    <svg
      class="progress-ring-bg"
      width="60"
      height="60">
      <circle
        class="progress-ring__circle-bg"
        
        stroke="white"
        stroke-width="4"

        fill="transparent"
        r="26"
        cx="30"
        cy="30"/>
    </svg>
    <svg
      class="progress-ring"
      width="60"
      height="60">
      <circle
        class="progress-ring__circle"
        id="circleid"
        stroke="white"
        stroke-width="4"

        fill="transparent"
        r="26"
        cx="30"
        cy="30"/>
    </svg>
    <p class="progress-ring-innertext" id="progress-ring-innertext-id">...</p>
    
    

  </div>
</template>

<script>



  



  
  

  try{
    const circle = document.getElementById('circleid');
    
    const radius = circle.r.baseVal.value;
    const circumference = radius * 2 * (22/7);
    document.getElementById('circleid').style['stroke-dasharray'] = `${circumference} ${circumference}`;
    document.getElementById('circleid').style['stroke-dashoffset'] = `10`;

    // console.log(circumference)
    // console.log(circle)

    // console.log(circle.style.strokeDasharray)
  }
  catch(err){
    console.log(err)
  }
  
  function increment(questionBufferCounter, currentChar){
    document.getElementById('circleid').style.strokeDashoffset =  ((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7)) - parseInt(questionBufferCounter) / 100 * ((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7));
    document.getElementById('circleid').style.strokeDasharray =  ((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7));
    document.getElementById('progress-ring-innertext-id').innerHTML = currentChar
    // console.log(questionBufferCounter)
    // console.log(currentChar)

  }
  window.eel.expose(increment)
  
  export default {
    name: 'progresscircle',
    
    data: function () {
      return {
        
      }
    },
    mounted: function () {
      // window.eel.predict_output()()
    },
    methods: {
      
      
     

    },
    
  }
</script>

<style>
  @import '../assets/style.css';
</style>



