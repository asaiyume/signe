<template>
  <div class="predictoutput" >
    <p class="chaptergame-outputtext-header" id="chaptergame-outputtext-header-id">...</p>
    <div class="progress-rings">
      <!-- <svg
        class="progress-ring"
        width="120"
        height="120">
        <circle
          class="progress-ring__circle"
          id="circleid"
          stroke="white"
          stroke-width="4"

          fill="transparent"
          r="52"
          cx="60"
          cy="60"/>
      </svg> -->
      <progresscircle ref="childComponent"/>
    </div>
    
    <span style="display: inline-block; position: fixed; color: transparent" id="b1g">dddd</span>
    <p style="display: inline-block; position: fixed; color: transparent" id="questionCounter">0</p>
    <p style="display: inline-block; position: fixed; color: transparent" id="questionBufferCounter">10</p>
    <!-- sendtoprogresscomponent(document.getElementById('questionBufferCounter')) -->

  </div>
</template>

<script>



  export const eel = window.eel;
  eel.set_host( 'ws://localhost:9000' );

  import progresscircle from '@/components/progresscircle.vue'


  let question 
  // const question = ['5','1','0']

  // try{
  //   const circle = document.getElementById('circleid');
    
  //   const radius = circle.r.baseVal.value;
  //   const circumference = radius * 2 * (22/7);
  //   document.getElementById('circleid').style['stroke-dasharray'] = `${circumference} ${circumference}`;
  //   document.getElementById('circleid').style['stroke-dashoffset'] = `50`;

  //   console.log(circumference)
  //   console.log(circle)

  //   console.log(circle.style.strokeDasharray)
  // }
  // catch(err){
  //   console.log(err)
  // }
  function updateQuestion(){
    question = JSON.parse("[" + document.getElementById('chaptergame-outputtext-header-id').innerText + "]")
    document.getElementById('chaptergame-outputtext-header-id').innerHTML = question.toString().replace(/,/g, ' ')

  }
  window.eel.expose(updateQuestion);

  function tracker(input) {
    

    // document.getElementById('circleid').style.strokeDashoffset =  ((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7)) - parseInt(document.getElementById('questionBufferCounter').innerHTML) / 100 * ((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7));
    // document.getElementById('circleid').style.strokeDasharray =  ((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7));
    document.getElementById('chaptergame-outputtext-header-id').innerHTML = question.toString().replace(/,/g, ' ')
    
    // console.log(document.getElementById('circleid').style.strokeDashoffset)
    // console.log(((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7)) - parseInt(document.getElementById('questionBufferCounter').innerHTML) / 100 * ((document.getElementById('circleid').r.baseVal.value)* 2 * (22/7)))
    // console.log(question[document.getElementById('questionCounter').innerHTML])
    if((input).toString() === (question[document.getElementById('questionCounter').innerHTML]).toString()){
      document.getElementById('questionBufferCounter').innerHTML = (parseInt(document.getElementById('questionBufferCounter').innerHTML) + 10).toString();
      window.eel.callIncrement(document.getElementById('questionBufferCounter').innerHTML, question[document.getElementById('questionCounter').innerHTML])

    }
    if(document.getElementById('questionBufferCounter').innerHTML === '100'){
      if(question.length === document.getElementById('questionCounter').innerHTML){
        document.getElementById('questionCounter').innerHTML = '-1'
      }
      else{
        document.getElementById('questionCounter').innerHTML  = (parseInt(document.getElementById('questionCounter').innerHTML) + 1).toString()
        document.getElementById('questionBufferCounter').innerHTML = '0'
        window.eel.callIncrement('0', question[document.getElementById('questionCounter').innerHTML])


      }
    }
  }
  function updateTextSrc(val) {
    const elem = document.getElementById('b1g');

    if(document.getElementById('questionCounter').innerHTML >= 0){
      tracker(val.toString())
      // console.log(question)

    }

    // console.log(val + ',' + document.getElementById('questionCounter').innerHTML  + ',' + document.getElementById('questionBufferCounter').innerHTML)

    elem.innerHTML = val
  }
  window.eel.expose(updateTextSrc);
  export default {
    name: 'predictoutputgame',
    components:{
      progresscircle
    },
    data: function () {
      return {
        message: "",
        inputValue: "",
        response: "",
        questionValue: ['5','1','2','9','0'],
        
      }
    },
    mounted: function () {
      document.getElementById('chaptergame-outputtext-header-id').innerHTML = this.questionValue
      // console.log(this.questionValue)


      window.eel.predict_output()()
      window.eel.callIncrement('0', this.questionValue[document.getElementById('questionCounter').innerHTML])
      
    },
    methods: {
      onClick: function() {
        // Passing values to Python
        eel.print_string(this.inputValue)((val) => {
          // Return response from Python
          this.response = val
        })
      },
      

    },
    
  }
  // question = document.getElementById('chaptergame-outputtext-header-id').innerText

  // document.getElementById('chaptergame-outputtext-header-id').innerText = question.toString().replace(/,/g, ' ')
  // console.log(question.toString().replace(/,/g, ' '))
</script>

<style>
  @import '../assets/style.css';
</style>



