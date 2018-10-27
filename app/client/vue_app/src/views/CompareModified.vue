<template>
  <div class="full-screen">

    <v-toolbar fixed dark color="primary">
      <v-icon @click="$router.go(-1)">keyboard_backspace</v-icon>
      <v-toolbar-title>d-DeViS</v-toolbar-title>

    </v-toolbar>


    <div class="visualization">
      <div class="image-zoom">
        <div class="component">
          <original-image :title="'original prediction'" :hash="hash" :digit="digit" :link-template="linkTemplate"></original-image>
          <br>
          <original-image :title="'prediction on modified features'" :waveform-title="'waveform, modified prediction'" :hash="hash2" :digit="digit2" :link-template="linkTemplate"></original-image>
        </div>
      </div>

      <div>
        <h3 STYLE="text-align: center">LAYERS</h3>
        <v-tabs fixed-tabs v-model="activeLayer">
          <v-tab v-for="n in 3" :key="n">
            Layer {{ n }}
          </v-tab>
          <v-tab>All Layers</v-tab>

          <v-tab-item v-for="n in 3" :key="n">
            <div class="title ma-4 text-uppercase" style="text-align: center;">Original Prediction {{digit}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="n"></sound-layer>
            <div class="title ma-4 text-uppercase" style="text-align: center;">Modified Prediction {{digit2}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash2" :current-layer="n"></sound-layer>
          </v-tab-item>

          <v-tab-item>
            <div class="group-odd">
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 1, Original Prediction {{digit}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="1"></sound-layer>
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 1, Modified Prediction {{digit2}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash2" :current-layer="1"></sound-layer>
            <br>
              </div>
            <v-divider></v-divider>
            <br>
            <div class="group-even">
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 2, Original Prediction {{digit2}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash2" :current-layer="2"></sound-layer>
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 2, Modified Prediction {{digit}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="2"></sound-layer>
            <br>
              </div>
            <v-divider></v-divider>
            <br>
            <div class="group-odd">
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 2, Original Prediction {{digit}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="3"></sound-layer>
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 3, Modified Prediction {{digit2}}</div>
            <sound-layer :link-template="linkTemplate" :hash="hash2" :current-layer="3"></sound-layer>
           </div>
          </v-tab-item>

        </v-tabs>


      </div>

    </div>
  </div>
</template>

<script>
    import LayerComponent from '../components/LayerComponent'
    import UploadForm from '../components/AudioUploadOptions'
    import OriginalImage from '../components/ImageOriginal'
    import LayerImage from '../components/SoundLayer'
    import $backend from '../backend'

    const print = console.log;

    export default {
        name: "VisualizeLayer",
        components: {
            layerComponent: LayerComponent,
            uploadForm: UploadForm,
            originalImage: OriginalImage,
            soundLayer: LayerImage,
        },
        created() {
            let response = localStorage.getItem('serverResponse');
            let response2 = localStorage.getItem('serverResponse2');
            if (!response || !response2) {
                alert("The model was not loaded successfully. Try uploading the file again.");
                // this.$router.push('/')
            } else {
                response = JSON.parse(response);
                response2 = JSON.parse(response2);
                this.digit = parseInt(response.data);
                this.digit2 = parseInt(response2.data);
                this.linkTemplate = $backend.domain + response['link_template'];
                this.hash = response.hash;
                this.hash2 = response2.hash;
            }
        },
        data() {
            return {
                activeLayer: 0,
                digit: '',
                linkTemplate: "",
                hash: "",
                digit2: '',
                hash2: "",


            }
        }
    }
</script>

<style scoped>
  .full-screen {
    height: 100vh;
    padding-top: 20px;
  }

  .v-tabs__wrapper {
    box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12) !important;
  }

  .v-card__text {
    text-align: center;
    min-height: 350px;
    padding-top: 50px;
  }

  .layer-divider {
    display: block;
    align-self: center;
    margin: 0 -16px;
    flex: 1 1 0px;
    max-width: 100%;
    height: 0px;
    max-height: 0px;
    border: solid;
    border-width: thin 0 0 0;
    transition: inherit;
  }

  .layer {
    transition: none !important;
  }

  .layer__step--active {
    border-bottom: 2px solid white;
    font-weight: 700;
  }

  .visualization {
    margin: 4% auto;
    display: flex;
    height: 40%;
    width: 80%;
  }

  .image-zoom {
    flex: 1;
    margin: 10px
  }

  .image-zoom .component {
    width: 350px;
    height: 400px;
    float: left;
  }

  .group-odd{
    background-color: #f3f5f7;
    padding: 10px 0;
  }




</style>