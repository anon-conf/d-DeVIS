<template>
    <v-content>
        <v-container fluid fill-height>

            <v-layout align-center justify-center>
                <v-flex xs12 sm8 md4>
                    <v-card class="elevation-12" :height="'400px'">
                        <v-card-text>
                            <div class="form-holder">
                            <upload-form @upload="onUploaded"></upload-form>
                            </div>
                        </v-card-text>

                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import UploadForm from '../components/AudioUploadOptions'

    export default {
        name: "Login",
        components: {
            uploadForm: UploadForm
        },
        methods: {
            onUploaded(data){
                console.log(data);
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
    
    .v-card__text {
        text-align: center;
        height: 100%;
    }

    /*.v-card {*/
        /*min-height: 400px;*/
    /*}*/

    .form-holder {
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
    }


</style>
