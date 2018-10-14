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
          <original-image :hash="hash" :digit="digit" :link-template="link_template"></original-image>
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
            <sound-layer :link-template="link_template" :hash="hash" :current-layer="n"></sound-layer>
          </v-tab-item>

          <v-tab-item>
            <sound-layer :link-template="link_template" :hash="hash" :current-layer="1"></sound-layer>
            <v-divider></v-divider>
            <sound-layer :link-template="link_template" :hash="hash" :current-layer="2"></sound-layer>
            <v-divider></v-divider>
            <sound-layer :link-template="link_template" :hash="hash" :current-layer="3"></sound-layer>
            <v-divider></v-divider>

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
            onUpload(response) {
                localStorage.setItem('serverResponse2', JSON.stringify(response));
                this.$router.push('/compare')

            },

        },
        computed: {
            waveformSrc() {
                let filename = `${this.hash}original.png`;
                return this.linkTemplate.replace('dummy', filename);
            },

        }
    }
</script>

<style scoped>
  .full-screen {
    height: 100vh;
    padding-top: 20px;
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