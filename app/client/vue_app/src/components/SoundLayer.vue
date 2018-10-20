<template>
  <div>
    <div class="image-grid">
      <img :src="imageSrc(i)" @click="display" v-for="i in 16" :data-index="i">
    </div>
    <div style="text-align: center">
      <v-btn @click="weightDialog=true">Weight Distribution</v-btn>
    </div>


    <div>
      <v-dialog v-model="imageDialog" width="500">
        <v-card>
          <v-card-text>
            <layer-component :index="currentIndex" :layer="currentLayer" :hash="hash"
                             :link-template="linkTemplate"></layer-component>
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
    <div>
      <v-dialog v-model="weightDialog" width="760px">
        <v-card>
          <div class="headline text-md-center pt-4">WEIGHT DISTRIBUTION, LAYER {{currentLayer}}</div>
          <v-card-text>
            <img :src="weightImageSrc" alt="">
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
    import LayerComponent from './LayerComponent'
    const layers = [, 'first', 'second', 'third'];

    export default {
        name: "SoundLayer",
        components: {
            layerComponent: LayerComponent
        },
        props: {
            currentLayer: {
                type:Number,
                default: 1,
            },
            linkTemplate: {
                type: String,
                default: "",
                required: true
            },
            hash: String
        },
        data() {
            return {
                weightDialog: false,
                imageDialog: false,
                currentIndex: 1
            }
        },
        computed: {
            weightImageSrc() {
                let filename = `${this.hash}${layers[this.currentLayer]}_distribution.png`;
                return this.linkTemplate.replace('dummy', filename);
            },

        },
        methods: {
            display(event) {
                let target = event.target;
                this.currentIndex = parseInt(target.dataset.index);
                this.imageDialog = true;
            },
            imageSrc(index) {
                let filename = `${this.hash}${layers[this.currentLayer]}${index}.png`;
                return this.linkTemplate.replace('dummy', filename);
            }
        }
    }
</script>

<style scoped>
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

  .v-card__text {
    text-align: center;
    min-height: 350px;
    padding-top: 50px;
  }

</style>