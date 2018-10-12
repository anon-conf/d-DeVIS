<template>
    <div class="layer-component">
        <div class="img-container">
            <img :src="imgSrc" alt=""/>
            <audio ref="audio">
                <source :src="audioSrc" type="audio/wav">
            </audio>
            <div class="play-button" @click="playAudio">
                <svg class="icon" fill="#fff" version="1.1" viewBox="0 0 24 24" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                    <g id="info"></g>
                    <g id="icons">
                        <path d="M3.9,18.9V5.1c0-1.6,1.7-2.6,3-1.8l12,6.9c1.4,0.8,1.4,2.9,0,3.7l-12,6.9C5.6,21.5,3.9,20.5,3.9,18.9z" id="play">
                        </path>
                    </g>
                </svg>
            </div>
        </div>
        <p>Layer {{layer}}: {{index}}</p>

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
                this.$refs['audio'].play();
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