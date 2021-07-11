  
<template>
    <div class="titlebar">
        <img v-bind:src="ico" class="icon">
        <div class="bar">
            <slot></slot>
            <div class="dragregion">
                <span>{{title}}</span>
            </div>
            
            <div class="button close" @click="onClose"><svg class="svgthing" aria-hidden="false" width="12" height="12" viewBox="0 0 12 12"><polygon fill="currentColor" fill-rule="evenodd" points="11 1.576 6.583 6 11 10.424 10.424 11 6 6.583 1.576 11 1 10.424 5.417 6 1 1.576 1.576 1 6 5.417 10.424 1"></polygon></svg></div>
        </div>
    </div>
</template>

<script>

export default {
    props: [ 'title', 'ico' ],
    methods: {
        onClose() {
            close()
        }
    }
}
</script>

<style scoped>
.titlebar {
    
    color: var(--vue-electron-titlebar-color);
    background-color: var(--vue-electron-titlebar-background-color);
    height: var(--vue-electron-titlebar-height);
}
img {
    height: var(--vue-electron-titlebar-height);
}
.bar {
    top:0;
    position:fixed;
    height:30px;
}
.dragregion {
    text-align: center;
    vertical-align: middle;
    margin: 3px 3px 0px 0px;
    -webkit-app-region: drag;
    display: flex;
    align-items: center;  
    left:0;
    height: 30px;
    width: calc(100% - 150px);
    position: fixed;
}
.dragregion>span {
    flex-grow: 1;   
    margin-top: -3px;        
}
.button {
    width: 50px;
    height:30px;
    position:fixed;
    right:0;
    top:0;
          
    cursor: pointer;
}
.button>span {
    flex-grow: 1;   
    margin-top: -3px;
    user-select: none;
}
.button:hover {
    background-color: var(--vue-electron-titlebar-button-hover-color);
}
.close:hover {
    background-color: #ed4245;
    color: white;
}
.button>span.dash {
    vertical-align: sub;
    margin-top: 0px;
}

.icon{
    position:fixed;
    top: 5px;
    left: 8px;
    max-width:20%;
    height:auto;
}

.svgthing{
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
}

</style>