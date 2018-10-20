<template>
    <div class="layer-component">
        <div class="img-container">
            <div class="text-uppercase title text-md-center mb-3">Layer {{layer}}: {{index}}</div>
            <img :src="imgSrc" alt=""/>
            <audio ref="audio" controls>
                <source :src="audioSrc" type="audio/wav">
            </audio>
            <!--<div>-->
                <!--<v-btn  @click="playAudio"><v-icon>play_arrow</v-icon>play</v-btn>-->
            <!--</div>-->
        </div>


    </div>
</template>

<script>
    const layers = {1: 'first', 2: 'second', 3: 'third'};

    export default {
        name: "LayerComponent",
        props: {
            index: {type: Number, required: true},
            layer: {type: Number, required: true},
            hash: {type: String, default: ""},
            linkTemplate: {type: String, required: true, default: ""},
        },
        computed: {
            imgSrc() {
                if (! this.linkTemplate){
                    return "";
                }
                else {
                    let filename = `${this.hash}${layers[this.layer]}${this.index}.png`;
                    return this.linkTemplate.replace('dummy', filename);
                }
            },
            audioSrc() {
                if (! this.linkTemplate) {
                    return "";
                }
                else {
                    let filename = `${this.hash}${layers[this.layer]}${this.index}.wav`;
                    return this.linkTemplate.replace('dummy', filename);
                }
            }
        },

        methods: {
            playAudio() {
                this.$refs['audio'].play().catch(e => console.log(e));
            }
        }
    }
</script>

<style scoped>
    img {
        width: 100%;
        max-height: 250px;
        object-fit: fill;
    }

    .img-container {
        position: relative;
        cursor: pointer;
    }

    .play-button {
        display: block;
        position: absolute;
        height: 54px;
        width: 54px;
        left: 0;
        bottom: 0;
        z-index: 99;
        background-color: #3c3c3c;
        color: white;
        padding: 7px 10px;
        text-align: center;
    }

    .play-button .icon {
        width: 36px;
        height: 36px;
    }



    p {
        text-align: center;
        font-size: 16px;
        font-weight: bolder;
    }

</style>