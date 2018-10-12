<template>
    <div class="full-screen">
        <v-toolbar fixed dark color="primary">
            <v-toolbar-title>Image Layers</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items class="hidden-sm-and-down">
                <v-btn @click="modify = true" flat>Modify</v-btn>
                <v-btn @click="newAudio = true" flat>Compare</v-btn>

            </v-toolbar-items>

        </v-toolbar>
        <div>
            <v-dialog
                    v-model="newAudio"
                    width="500"
            >

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

                </v-card>
            </v-dialog>
        </div>

        <div class="visualization">
            <div class="image-zoom">
                <div class="component">
                    <layer-component :index="currentIndex" :layer="currentLayer" :hash="hash"
                                     :link-template="link_template"></layer-component>
                </div>
            </div>
            <div>
                <v-tabs fixed-tabs v-model="activeLayer">
                    <v-tab
                            v-for="n in 3"
                            :key="n"
                    >
                        Layer {{ n }}
                    </v-tab>
                </v-tabs>
                <div class="image-grid">

                <img :src="imageSrc(i)" @mouseover="display" v-for="i in 16" :data-index="i"
                     :data-layer="activeLayer" alt="">
                <!--<layer-component v-for="i in 16" v-bind:index="i" :key="i" :layer="activeLayer" :hash="hash" :link-template="link_template"></layer-component>-->
            </div>
            </div>

        </div>
    </div>
</template>

<script>
    import LayerComponent from '../components/LayerComponent'
    import UploadForm from '../components/AudioUploadOptions'

    const print = console.log;
    const layers = {1: 'first', 2: 'second', 3: 'third'};

    export default {
        name: "VisualizeLayer",
        components: {
            layerComponent: LayerComponent,
            uploadForm: UploadForm
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
                this['link_template'] = response['link_template'];
                this.hash = response.hash
            }
        },
        data() {
            return {
                activeLayer: 1,
                digit: '',
                link_template: "",
                hash: "",
                dialog: false,
                currentIndex: 1,
                currentLayer: 1,
                modify: false,
                newAudio: false
            }
        },
        methods: {
            activateLayer(layer) {
                this.activeLayer = parseInt(layer);
            },
            onUpload(data) {

            },
            display(event) {
                let target = event.target;
                this.currentLayer = parseInt(target.dataset.layer);
                this.currentIndex = parseInt(target.dataset.index);
            },
            imageSrc(index) {
                let filename = `${this.hash}${layers[this.activeLayer]}${index}.png`;
                return this['link_template'].replace('dummy', filename);
            }
        },
        computed: {
            layerOneClass() {
                return {
                    'layer': true,
                    'layer__step--active': this.activeLayer === 1,
                    'layer__step--inactive': this.activeLayer !== 1,
                }
            },
            layerTwoClass() {
                return {
                    'layer': true,
                    'layer__step--active': this.activeLayer === 2,
                    'layer__step--inactive': this.activeLayer !== 2,
                }
            },
            layerThreeClass() {
                return {
                    'layer': true,
                    'layer__step--active': this.activeLayer === 3,
                    'layer__step--inactive': this.activeLayer !== 3,
                }
            }
        }
    }
</script>

<style scoped>
    .full-screen {
        height: 100vh;
        padding-top: 20px;
    }

    .header {

        height: 72px;
        align-items: stretch;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
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
        width: 70%;
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
        width: 250px;
        height: 250px;
        float: right;
    }

</style>