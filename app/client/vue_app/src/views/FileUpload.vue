<template>
    <v-content>
        <v-container fluid fill-height>

            <v-layout align-center justify-center>
                <v-flex xs12 sm8 md4>
                    <v-card class="elevation-12">
                        <v-card-text>
                            <upload-form @upload="onUploaded"></upload-form>
                        </v-card-text>

                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import UploadForm from '../components/FormUpload'

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
    }


</style>
