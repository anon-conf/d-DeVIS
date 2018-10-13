<template>
  <div class="full-screen">

    <v-toolbar fixed dark color="primary">
      <v-toolbar-title>d-DeViS</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn @click="modify = true" flat>Modify</v-btn>
        <v-btn @click="newAudio = true" flat>Compare</v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <div>
      <v-dialog v-model="newAudio" width="500">
        <v-card>
          <v-card-text>
            <upload-form @upload="onUpload"></upload-form>
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>

    <div>
      <v-dialog v-model="imageDialog" width="500">
        <v-card>
          <v-card-text>
            <layer-component :index="currentIndex" :layer="currentLayer" :hash="hash"
                             :link-template="link_template"></layer-component>
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
    <div>
      <v-dialog v-model="weightDialog" width="760px">
        <v-card>
          <v-card-text>
            <img :src="weightImageSrc" alt="">
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>



    <div>
      <v-dialog v-model="modify" fullscreen hide-overlay transition="dialog-bottom-transition">
        <v-card>
          <v-toolbar dark color="primary">
            <v-btn icon dark @click.native="modify = false">
              <v-icon>keyboard_backspace</v-icon>
            </v-btn>
            <v-toolbar-title>Modify Sound</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark flat @click.native="dialog = false">Apply</v-btn>
            </v-toolbar-items>
          </v-toolbar>

          <!--Modification Panel-->

        </v-card>
      </v-dialog>
    </div>

    <div class="visualization">
      <div class="image-zoom">
        <div class="component">
          <original-image :hash="hash" :link-template="link_template"></original-image>
        </div>
      </div>

      <div>
        <h3 STYLE="text-align: center">LAYERS</h3>
        <v-tabs fixed-tabs v-model="activeLayer">
          <v-tab v-for="n in 3" :key="n">
            Layer {{ n }}
          </v-tab>
        </v-tabs>

        <div class="image-grid">
          <img :src="imageSrc(i)" @click="display" v-for="i in 16" :data-index="i"
               :data-layer="activeLayer + 1" alt="">
        </div>
        <div style="text-align: center">
          <v-btn @click="weightDialog = true">Weight Distribution</v-btn>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
    import LayerComponent from '../components/LayerComponent'
    import UploadForm from '../components/AudioUploadOptions'
    import OriginalImage from '../components/ImageOriginal'
    import $backend from '../backend'

    const print = console.log;
    const layers = ['first', 'second', 'third'];

    export default {
        name: "VisualizeLayer",
        components: {
            layerComponent: LayerComponent,
            uploadForm: UploadForm,
            originalImage: OriginalImage,
        },
        created() {
            let response = localStorage.getItem('serverResponse');
            if (!response) {
                alert("The model was not loaded successfully. Try uploading the file again.");
                // this.$router.push('/')
            } else {
                response = JSON.parse(response);
                console.log(response);
                this.digit = parseInt(response.data);
                this['link_template'] = $backend.domain + response['link_template'];
                this.hash = response.hash
            }
        },
        data() {
            return {
                activeLayer: 0,
                digit: '',
                link_template: "",
                hash: "",
                dialog: false,
                currentIndex: 1,
                currentLayer: 1,
                modify: false,
                newAudio: false,
                imageDialog: false,
                weightDialog: false,
            }
        },
        methods: {
            onUpload(data) {

            },
            display(event) {
                let target = event.target;
                this.currentLayer = parseInt(target.dataset.layer);
                this.currentIndex = parseInt(target.dataset.index);
                this.imageDialog = true;
            },
            imageSrc(index) {
                let filename = `${this.hash}${layers[this.activeLayer]}${index}.png`;
                return this['link_template'].replace('dummy', filename);
            }
        },
        computed: {
            weightImageSrc() {
                let filename = `${this.hash}${layers[this.activeLayer]}_distribution.png`;
                return this['link_template'].replace('dummy', filename);
            },


        }
    }
</script>

<style scoped>
  .full-screen {
    height: 100vh;
    padding-top: 20px;
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



  .v-tabs {
    box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
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
    margin: 10% auto;
    display: flex;
    height: 40%;
    width: 80%;
  }

  .image-grid {
    margin: 10px;
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: 100px 100px;
    grid-gap: 30px 30px;
    flex: 2

    /*background-color: #0c5460;*/
  }

  .image-grid img {
    width: 100px;
    height: 100px;
    align-self: start;
    cursor: pointer;
  }

  .image-grid img:hover {
    border: 3px solid #2979e3
  }

  .image-grid .item {
    /*background-color: rgba(255, 255, 255, 0.8);*/
    border: 1px solid rgba(0, 0, 0, 0.8);
    padding: 20px;
    font-size: 30px;
    text-align: center;
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



</style>