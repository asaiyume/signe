<template>
  <div class="homepagea" >
    
    <div class="homepagedivs homepagecarousel-headerdiv row">
      <div>
        <p class='homepagecarousel-headertext'>Notices and announcements</p>
      </div>
    </div>
    <div class="homepagecarousel homepagedivs row">
      <splide :options="options">
        <splide-slide>
          
          <img class="carousel-image" src="../../public/img/test1.jpg">
        </splide-slide>
        <splide-slide>
          <img class="carousel-image" src="../../public/img/test2.jpg">
        </splide-slide>
        <splide-slide>
          <img class="carousel-image" src="../../public/img/test3.jpg">
        </splide-slide>
      </splide>
    </div>
    <div class="homepagedivs homepageupdates-headerdiv row">
      <div>
        <p class='homepageupdates-headertext'>Update logs</p>
      </div>
    </div>
    <div class="homepagedivs homepageupdates-div row">
      <div>
        <p class='homepageupdates-text'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin in dui auctor sapien elementum tincidunt. Praesent vulputate eros erat, ornare porta leo facilisis et. Phasellus sit amet purus id risus varius finibus. Donec aliquam id urna ut tincidunt. Vivamus rutrum tincidunt neque. Suspendisse sed ultricies nisi. Phasellus pretium dolor id nunc malesuada rutrum.</p>
      </div>
      <div>
        <p class='homepageupdates-text'>Cras a rutrum augue. Aliquam at eros enim. Phasellus rutrum, dolor sit amet sollicitudin bibendum, ex leo ullamcorper augue, eu porttitor ipsum ipsum quis dolor. Integer consectetur orci ipsum, quis imperdiet elit porttitor vitae. Quisque vel tincidunt urna, eget eleifend augue. Morbi lacinia nisi eget nisl facilisis commodo. Nunc eget semper ante.</p>
      </div>
      <div>
        <p class='homepageupdates-text'>Ut semper euismod pulvinar. Curabitur viverra, nunc vitae ullamcorper imperdiet, elit turpis posuere velit, in ultrices erat enim id sem. Sed a magna mi. Vestibulum ac erat sed dui molestie hendrerit at non ante. Nullam orci nisl, ultrices in odio quis, ultricies pellentesque felis. Sed suscipit nunc sed suscipit finibus. Sed at sodales enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed venenatis sodales urna, non tempor ex aliquam ut.</p>
      </div>
      <div>
        <p class='homepageupdates-text'>Donec nec efficitur arcu. Sed volutpat rhoncus lorem id viverra. Sed vehicula et augue sed condimentum. Ut vitae interdum enim. Morbi ex dui, accumsan ultrices gravida eu, maximus at neque. Cras feugiat eros ut venenatis scelerisque. Cras convallis pulvinar augue nec gravida. Nunc vulputate ante mi, sed iaculis diam suscipit nec.</p>
      </div>
    </div>

  </div>
</template>

<script>

  import { Splide, SplideSlide } from '@splidejs/vue-splide';






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
  
  export default {

    name: 'HomePage',
    components: {
      Splide,
      SplideSlide,
    },
    data: function () {
      return {
        options: {
          type: 'loop',
          autoplay: true,
          pauseOnHover: false,
          pauseOnFocus: false,
        },
      }
    },
    mounted: function () {
      eel.hello_world()((val) => {
        // Receiving a value from Python
        this.message = val
      })
    },
    
  }
</script>

<style>
  @import '../assets/style.css';

  @import '../../node_modules/@splidejs/splide/dist/css/themes/splide-default.min.css';
</style>

