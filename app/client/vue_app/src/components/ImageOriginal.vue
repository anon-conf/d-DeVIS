<template>
  <div>
    <h2 class="headline mb-2 text-md-center text-uppercase">PREDICTED DIGIT: {{digit}}</h2>
    <img :src="imageSrc" alt="">
    <audio ref="originalAudio">
      <source :src="audioSrc" type="audio/wav">
    </audio>
    <div>
    <v-btn @click="$refs.originalAudio.play().catch()"><v-icon>play_arrow</v-icon>play</v-btn>
    <v-btn @click="waveformDialog = true">WAVEFORM</v-btn>

    </div>
    <div>
      <v-dialog v-model="waveformDialog" width="80%">
        <v-card>
          <v-card-title>
            <div  class="headline text-center">WAVEFORM, DIGIT {{digit}}</div>
          </v-card-title>
          <v-card-text>
            <img :src="waveformSrc" alt="" class="waveform-img">
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
    export default {
        name: "ImageOriginal",
        props: {
            hash: String,
            linkTemplate: String,
            digit: Number
        },
        data() {
            return {
                waveformDialog: false,

            }
        },
        computed: {
            imageSrc() {
                let filename = `${this.hash}original_spectogram.png`;
                return this.linkTemplate.replace('dummy', filename);
            },
            waveformSrc(){
                let filename = `${this.hash}original.png`;
                return this.linkTemplate.replace('dummy', filename);
            },
            audioSrc() {
                let filename = `${this.hash}original.wav`;
                return this.linkTemplate.replace('dummy', filename);
            }
        }
    }
</script>

<style scoped>
  img{
    width: 100%;
    height: 100%;
  }


  .play-button, .waveform {
    display: inline-block;
    position: relative;
    height: 54px;
    width: 54px;
    left: 0;
    bottom: 55px;
    z-index: 99;
    background-color: #3c3c3c;
    color: white;
    padding: 7px 10px;
    text-align: center;
  }

  .waveform {
    width: auto;
    border-left: 1px solid #595a5b;
    bottom: 53px;
  }

  .waveform-img {
    width: 100%;
  }

  .play-button .icon {
    width: 36px;
    height: 36px;
  }



</style>