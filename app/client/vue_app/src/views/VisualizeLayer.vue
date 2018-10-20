<template>
  <div class="full-screen">

    <v-toolbar fixed dark color="primary">
      <v-toolbar-title>d-DeViS</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-divider vertical></v-divider>
        <v-btn @click="modify = true" flat>Modify</v-btn>
        <v-divider vertical></v-divider>
        <v-btn @click="newAudio = true" flat>Compare</v-btn>
        <v-divider vertical></v-divider>
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
              <v-btn dark flat @click.native="predict">Predict</v-btn>
            </v-toolbar-items>
          </v-toolbar>

          <!--Modification Panel-->
          <div class="original-image">
            <img :src="waveformSrc" alt="">
          </div>
          <div class="sliders">
            <v-range-slider :thumb-label="'always'" v-model="parameters.slicing"
                            v-if="modifier === 'slice'"></v-range-slider>
            <v-range-slider :thumb-label="'always'" v-model="parameters.crossfading"
                            v-if="modifier === 'crossfade'"></v-range-slider>
            <v-slider :thumb-label="'always'" v-model="parameters.fade" v-if="modifier === 'fade'"></v-slider>
            <v-menu
                    v-model="menu.loudness"
                    absolute
                    :position-x="x"
                    :position-y="y"
                    style="max-width: 600px"
            >

              <v-list>
                <v-list-tile
                        v-for="value in 7"
                        :key="value"
                        @click="applyLoudness(value)"
                >
                  <v-list-tile-title>{{ value }} dB</v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-menu>
            <v-menu
                    v-model="menu.repeat"
                    absolute
                    :position-x="x"
                    :position-y="y"
                    style="max-width: 600px"
            >

              <v-list>
                <v-list-tile
                        v-for="value in 3"
                        :key="value"
                        @click="applyRepeat(value)"
                >
                  <v-list-tile-title>{{ value }}</v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-menu>
          </div>

          <div class="actions">

            <div class="modifiers" v-if="modifier === ''">
              <v-btn @click="play"><v-icon>play_arrow</v-icon>Play</v-btn>
              <v-btn @click="modifier = 'slice'">Slice</v-btn>
              <v-btn @click="modifier = 'crossfade'">Crossfade</v-btn>
              <v-btn @click="modifier = 'fade'">Fade</v-btn>
              <v-btn @click="showLoudnessMenu">Loudness</v-btn>
              <v-btn @click="showRepeatMenu">Repeat</v-btn>
            </div>
            <div class="prompt" v-else>
              <v-btn @click="modifier = ''"><i
                      class="btn-icon">&#x274C;</i>
                Discard
              </v-btn>
              <v-btn @click="apply"><i
                      class="btn-icon">&#x2705;</i>
                Apply
              </v-btn>
            </div>
          </div>

        </v-card>
      </v-dialog>
    </div>

    <div class="visualization">
      <div class="image-zoom">
        <div class="component">
          <original-image :hash="hash" :digit="digit" :link-template="linkTemplate"></original-image>
        </div>
      </div>

      <div>
        <h3 class="headline mb-2 text-md-center text-uppercase">LAYERS</h3>
        <v-tabs fixed-tabs v-model="activeLayer">
          <v-tab v-for="n in 3" :key="n">
            Layer {{ n }}
          </v-tab>
          <v-tab>All Layers</v-tab>

          <v-tab-item v-for="n in 3" :key="n">
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="n"></sound-layer>
          </v-tab-item>

          <v-tab-item>
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 1</div>
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="1"></sound-layer>
            <v-divider></v-divider>
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 2</div>
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="2"></sound-layer>
            <v-divider></v-divider>
            <div class="title ma-4 text-uppercase" style="text-align: center;">Layer 3</div>
            <sound-layer :link-template="linkTemplate" :hash="hash" :current-layer="3"></sound-layer>
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
            print(response);
            if (!response) {
                alert("The model was not loaded successfully. Try uploading the file again.");
                // this.$router.push('/')
            } else {
                response = JSON.parse(response);
                console.log(response);
                this.digit = parseInt(response.data);
                this['linkTemplate'] = $backend.domain + response['link_template'];
                this.hash = response.hash
            }
        },
        data() {
            return {
                newAudio: false,
                activeLayer: 0,
                digit: '',
                linkTemplate: "",
                hash: "",
                dialog: false,
                currentIndex: 1,
                currentLayer: 1,
                originalFileName: 'original',
                modify: false,
                modifier: '',
                x: 0,
                y: 0,
                menu: {
                    repeat: false,
                    loudness: false,

                },
                parameters: {
                    slicing: [0, 100],
                    crossfading: [50, 52],
                    loudness: 0,
                    fade: 0,
                    repeat: 0,
                },
            }
        },

        watch: {
            originalFileName(newval, oldval) {
                print(newval, oldval);
            }
        },
        methods: {
            onUpload(response) {
                localStorage.setItem('serverResponse2', JSON.stringify(response));
                this.$router.push('/compare')

            },
            showLoudnessMenu(e) {
                e.preventDefault();
                this.menu.loudness = false;
                this.x = e.clientX;
                this.y = e.clientY;
                this.$nextTick(() => {
                    this.menu.loudness = true
                })
            },
            showRepeatMenu(e) {
                e.preventDefault();
                this.menu.repeat = false;
                this.x = e.clientX;
                this.y = e.clientY;
                this.$nextTick(() => {
                    this.menu.repeat = true
                })
            },
            sendModificationRequest(data) {
                data.hash = this.hash;
                data.filename = this.originalFileName;
                $backend.get('resources/waveform', {
                    params: data
                }).then(response => {
                    console.log(response);
                    this.originalFileName = response.data.filename;
                    this.modifier = '';
                }).catch(error => console.log(error))
            },
            apply() {
                const data = {};
                switch (this.modifier) {
                    case 'slice':
                        data.sliceStart = this.parameters.slicing[0];
                        data.sliceEnd = this.parameters.slicing[1];
                        break;
                    case 'crossfade':
                        data.crossfadingStart = this.parameters.crossfading[0];
                        data.crossfadingEnd = this.parameters.crossfading[1];
                        break;
                    case 'fade':
                        data.fade = this.parameters.fade;
                        break;
                }

                if (Object.keys(data).length !== 0)
                    this.sendModificationRequest(data);

            },
            applyLoudness(value) {
                const data = {
                    loud: value,
                };

                this.sendModificationRequest(data);

            },
            applyRepeat(value) {
                const data = {
                    repeat: value,
                };

                this.sendModificationRequest(data);
            },
            predict() {
                const data = {
                    fname: this.originalFileName,
                    hash: this.hash,
                };
                const vm = this;
                $backend.post(`/resources/audio`, data)
                    .then(response => response.data)
                    .then(response => {
                        console.log(response);
                        localStorage.setItem('serverResponse', JSON.stringify(response));
                        vm.digit = response.data;
                        vm.linkTemplate = $backend.domain + response['link_template'];
                        vm.hash = response.hash;
                        this.originalFileName = 'original';
                        this.modify = false;
                        vm.$forceUpdate();
                    })
                    .catch(error => console.log(error))
            },
            play(){
               let filename = `${this.hash}${this.originalFileName}.wav`;
               const link = this.linkTemplate.replace('dummy', filename);
               console.log(link);
               const ad = new Audio(link);
               ad.play().catch(e => console.log(e));
            }

        },
        computed: {
            waveformSrc() {
                let filename = `${this.hash}${this.originalFileName}.png`;
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

  .original-image img {
    width: 100%;
  }

  .actions {
    position: relative;
    margin-top: 10%;
  }

  .modifiers, .prompt {
    display: flex;
    justify-content: center;
  }

  .sliders {
    width: 80%;
    margin: auto;
    padding-left: 42px;
  }

</style>