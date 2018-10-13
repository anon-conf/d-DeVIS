<template>
  <div>
    <h3 STYLE="text-align: center">ORIGINAL SOUND</h3>
    <img src="../assets/spectogram.png" alt="">
    <audio ref="originalAudio">
      <source :src="audioSrc" type="audio/wav">
    </audio>
    <div class="play-button">
      <svg class="icon" fill="#fff" version="1.1" viewBox="0 0 24 24" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <g id="info"></g>
              <g id="icons">
                  <path d="M3.9,18.9V5.1c0-1.6,1.7-2.6,3-1.8l12,6.9c1.4,0.8,1.4,2.9,0,3.7l-12,6.9C5.6,21.5,3.9,20.5,3.9,18.9z" id="play">
                  </path>
              </g>
            </svg>
    </div>
    <button @click="waveformDialog = true" class="waveform">WAVEFORM</button>
    <div>
      <v-dialog v-model="waveformDialog" width="80%">
        <v-card>
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
            linkTemplate: String
        },
        data() {
            return {
                waveformDialog: false
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
                return "";
            }
        }
    }
</script>

<style scoped>
  img{
    width: 100%;
    height: 100%;
  }
</style>