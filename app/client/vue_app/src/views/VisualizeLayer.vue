<template>
    <div class="full-screen">
        <v-toolbar fixed>
            <v-toolbar-title>Image Layers</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items class="hidden-sm-and-down">
                <v-btn @click="activateLayer(1)" :class="layerOneClass" flat>Layer 1</v-btn>
                <v-btn @click="activateLayer(2)" :class="layerTwoClass" flat>Layer 2</v-btn>
                <v-btn @click="activateLayer(3)" :class="layerThreeClass">Layer 3</v-btn>

            </v-toolbar-items>
            <v-spacer></v-spacer>
            <v-toolbar-items class="hidden-sm-and-down">
                <v-btn @click="dialog = true" flat>Compare</v-btn>

            </v-toolbar-items>

        </v-toolbar>
        <div>
            <v-dialog
                    v-model="dialog"
                    width="500"
            >

                <v-card>
                    <v-card-title
                            class="headline grey lighten-2"
                            primary-title
                    >
                       Upload New File
                    </v-card-title>
                    <v-card-text>
                    <upload-form @upload="onUpload"></upload-form>

                    </v-card-text>


                </v-card>
            </v-dialog>
       </div>


        <div class="image-grid">
            <layer-component v-for="i in 16" v-bind:index="i" :key="i" :layer="activeLayer" :hash="hash" :link-template="link_template"></layer-component>
        </div>
    </div>
</template>

<script>
    import LayerComponent from '../components/LayerComponent'
    import UploadForm from '../components/FormUpload'

    const print = console.log;

    export default {
        name: "VisualizeLayer",
        components: {
            layerComponent: LayerComponent,
            uploadForm: UploadForm
        },
        created() {
            let response = localStorage.getItem('serverResponse');
            if (! response) {
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
                dialog:false
            }
        },
        methods: {
            activateLayer(layer) {
                this.activeLayer = parseInt(layer);
            },
            onUpload(data){

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

    .layer__step--active {
        border-bottom: 1px solid blue;
    }

    .image-grid {
        margin-top: 2%;
        display: grid;
        grid-template-columns: auto auto auto auto;
        grid-template-rows: auto auto auto auto;
        grid-gap: 10px 10px;
        height: 80%;
        /*background-color: #0c5460;*/
    }

    .image-grid .item {
        /*background-color: rgba(255, 255, 255, 0.8);*/
        border: 1px solid rgba(0, 0, 0, 0.8);
        padding: 20px;
        font-size: 30px;
        text-align: center;
    }

</style>