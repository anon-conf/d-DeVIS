<template>
    <div>
        <b-row align-h="center">
            <img class="image" :src="originalSrc" alt="">
        </b-row>
        <b-row class="mt-3 p-3">
            <b-col>
                <div class="card-holder">
                    <div class="back" :style="backTransformationObject">
                        <img class="modified-image" :src="modifiedSrc" alt="">
                        <button @click="reapply" class="btn btn-success float-right"
                                style="margin: 20px 150px 20px 0px">ReApply
                        </button>
                    </div>
                    <div class="front" :style="frontTransformationObject">
                        <modification-panel :parameters="parameters"></modification-panel>
                        <br>
                        <button @click="applyModification" class="btn btn-primary m-1 float-right">Apply</button>
                        <button @click="reset" class="btn btn-light m-1 float-right">Reset</button>
                    </div>

                </div>

                <!--</b-row>-->
            </b-col>

        </b-row>
    </div>
</template>

<script>
    import $backend from '../backend'

    import ModificationPanel from '../components/ModificationPanel'

    const frontVisibleTransformation = 'perspective(600px) translateX(-50%) rotateX(0deg)'
    const backVisibleTransformation = 'perspective(600px) rotateX(0deg)'

    const frontInvisibleTransformation = 'perspective(600px) translateX(-50%) rotateX(-180deg)'
    const backInvisibleTransformation = 'perspective(600px) rotateX(180deg)'

    const original = {
        slicing: 0,
        loudness: 0,
        crossfading: 0,
        fade: 0,
        repeat: 0,
        invert: false
    }

    export default {
        name: 'VisualizationPage',
        components: {
            modificationPanel: ModificationPanel
        },
        methods: {
            applyModification() {
                const parameters = this.parameters
                $backend.get('resources/waveform', {
                    params: parameters
                }).then(response => console.log(response))
                this.frontTransformationObject.transform = frontInvisibleTransformation
                this.backTransformationObject.transform = backVisibleTransformation
            },
            reapply() {
                this.frontTransformationObject.transform = frontVisibleTransformation
                this.backTransformationObject.transform = backInvisibleTransformation
            },
            reset() {
                Object.assign(this.parameters, original)
            },
            fetchOriginalImageSrc() {
                $backend.get('resources/waveform').then(response => {
                    console.log(response)
                    this.originalSrc = response.data.link
                })
            }
        },

        created() {
            this.fetchOriginalImageSrc()
        },

        data() {
            return {
                parameters: {
                    slicing: 0,
                    loudness: 0,
                    crossfading: 0,
                    fade: 0,
                    repeat: 0,
                    invert: false
                },
                originalSrc: '',
                modifiedSrc: '',
                frontTransformationObject: {
                    transform: frontVisibleTransformation
                },
                backTransformationObject: {
                    transform: backInvisibleTransformation
                }

            }
        }
    }

</script>

<style scoped>

    *,
    *:after,
    *:before {
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }

    .image, .modified-image {
        height: 200px;
    }

    .modified-image {
        margin-left: -35px;
    }

    body {
        font-family: Avenir, 'Helvetica Neue', 'Lato', 'Segoe UI', Helvetica, Arial, sans-serif;
        color: #4b0f31;
        background-color: #f1e5e6;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    .front {
        color: #fff;
        background-color: #fff;
        /* transform: perspective(600px) rotateX(0deg); */
        transition: transform 0.5s linear 0s;
        backface-visibility: hidden;
        position: absolute;
        width: 80%;
        left: 50%;
        /*top: 0; right: 0; left: 0; bottom: 0;*/
        border: 1px solid dimgray;
        -webkit-box-shadow: 1px 0px 14px 0px rgba(0, 0, 0, 0.87);
        -moz-box-shadow: 1px 0px 14px 0px rgba(0, 0, 0, 0.87);
        box-shadow: 1px 0px 14px 0px rgba(0, 0, 0, 0.87);
        padding: 20px;
    }

    .back {
        color: #fff;
        position: absolute;
        /* transform: perspective(600px) rotateY(180deg); */
        backface-visibility: hidden;
        transition: transform 0.5s linear 0s;

    }

</style>
