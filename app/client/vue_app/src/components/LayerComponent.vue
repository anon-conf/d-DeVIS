<template>
    <div class="layer-component">
        <p>{{index}}</p>
        <img src="" alt=""/>
        <span class="play-button"></span>

    </div>
</template>

<script>
    export default {
        name: "LayerComponent",
        props: {
            index: {type: Number, required: True},
            layer: {type: Number, required: True},
        },
        data(){
            return {
                hash: localStorage.getItem('fileResponse')['hash']
            }
        }
    }
</script>

<style scoped>

</style>