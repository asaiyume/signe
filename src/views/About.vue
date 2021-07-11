<template>
  <div class="about">
    <div class="col-sm-12 main2">
      <div class="row settings-div">
        <p class="settings-title-text">App Settings</p>

      </div>
      <div class="row settings-div">
        <div class="col-sm-6 settings-camera-title">
          <p class="settings-camera-title-text">Video Settings</p>
        </div>
        <div class="col-sm-6 settings-camera-select">
          <p class="settings-camera-select-text">Camera input</p>
          <p id="selectedelement" >temp</p>
          <select @click="onClick()" class="camera-input" v-model="selected">
            <option @click="onClick()" class="camera-input" v-for="option in videoinputs" v-bind:key="option.name">
              {{ option.name }}
            </option>
          </select>

        </div>
        

      </div>


    </div>
  </div>
</template>


<script>
  export const eel = window.eel;
  eel.set_host( 'ws://localhost:9000' );


  function findWithAttr(array, attr, value) {
    for(let i = 0; i < array.length; i += 1) {
        if(array[i][attr] === value) {
            return i;
        }
    }
    return -1;
  }

  
  // eel.cameravalue( findWithAttr(this.videoinputs, 'name', this.selected) );

  function getCameraValue(current) {
    // this.selected = current;
    const elem = document.getElementById('selectedelement');
    console.log('getmareavalue' + current)
    elem.innerHTML = current
  }
  window.eel.expose(getCameraValue);

  export default {
    name: 'settings',
    components: {
      
    },
    data: function () {
      return {
        selected: "Select input",
        videoinputs: [{ name: "Select input"}],

      }
    },
    mounted: async function () {
      if (!navigator.mediaDevices || !navigator.mediaDevices.enumerateDevices) {
        console.log("enumerateDevices() not supported.");
        return;
      }

      // List cameras and microphones.

      navigator.mediaDevices.enumerateDevices()
      .then( (devices) => {
        devices.forEach( (device) => {
          if(device.kind === 'videoinput'){
            // console.log(device.kind + ": " + device.label + " id = " + device.deviceId);
            this.videoinputs.push({ name: device.label})

          }



        });
      })
      .catch(function(err) {
        console.log(err.name + ": " + err.message);
      });
      // console.log(this.videoinputs);
      eel.getcamera()
      await new Promise(r => setTimeout(r, 100));

      console.log(document.getElementById('selectedelement').innerHTML)
      console.log('asdasd  ' + this.videoinputs[document.getElementById('selectedelement').innerHTML].name)
      this.selected = this.videoinputs[document.getElementById('selectedelement').innerHTML].name

      console.log(findWithAttr(this.videoinputs, 'name', this.selected));
      eel.cameravalue( findWithAttr(this.videoinputs, 'name', this.selected) );
      
    },
    computed: {
      
      
      
    },
    methods: {
      onClick(){
        console.log(findWithAttr(this.videoinputs, 'name', this.selected));
        eel.cameravalue( findWithAttr(this.videoinputs, 'name', this.selected) );
      }



      // getCameraValue(current) {
      //   this.selected = current;
      // }
      

    },
  }


</script>