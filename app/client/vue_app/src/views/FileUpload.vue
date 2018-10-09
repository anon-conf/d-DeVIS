<template>
    <v-content>
        <v-container fluid fill-height>

            <v-layout align-center justify-center>
                <v-flex xs12 sm8 md4>
                    <v-card class="elevation-12">
                        <v-card-text>
                            <form enctype="multipart/form-data">
                                <input type="file" name="file" id="file-4" @change="uploadFile"
                                       class="inputfile inputfile-4"/>
                                <label for="file-4">
                                    <figure>
                                        <svg xmlns="http://www.w3.org/2000/svg" width="5" height="5"
                                             viewBox="0 0 20 17">
                                            <path
                                                    d="M10 0l-5.2 4.9h3.3v5.1h3.8v-5.1h3.3l-5.2-4.9zm9.3 11.5l-3.2-2.1h-2l3.4 2.6h-3.5c-.1 0-.2.1-.2.1l-.8 2.3h-6l-.8-2.2c-.1-.1-.1-.2-.2-.2h-3.6l3.4-2.6h-2l-3.2 2.1c-.4.3-.7 1-.6 1.5l.6 3.1c.1.5.7.9 1.2.9h16.3c.6 0 1.1-.4 1.3-.9l.6-3.1c.1-.5-.2-1.2-.7-1.5z"></path>
                                        </svg>
                                    </figure>
                                    <span>Choose a file&hellip;</span></label>
                                <br>
                                <div v-if="uploading">
                                    <v-progress-circular v-model="uploadProgress" :size="50" :rotate="-90"
                                                         :color="'#0101d5'"></v-progress-circular>
                                    <br>
                                    <br>
                                    <p>Uploading</p>
                                </div>
                            </form>

                        </v-card-text>

                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import $backend from '../backend'

    export default {
        name: "Login",
        data() {
            return {
                uploading: false,
                uploadProgress: 0
            }
        },
        methods: {
            uploadFile(event) {
                const formData = new FormData();
                const file = event.target.files[0];

                if (!file) {
                    console.log("no file");
                    return;
                }

                formData.append('file', file)
                this.uploading = true;

                let options = {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    },
                    onUploadProgress: progress => {
                        this.uploadProgress = progress.loaded;
                    }
                };

                $backend.post(`/resources/audio`, formData, options)
                    .then(response => response.data)
                    .then(response => {
                        if (response.success) {
                            localStorage.setItem('serverResponse', JSON.stringify(response));
                            this.$router.push('visualize')
                        }
                    })
                    .catch(error => console.log(error))

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

    .inputfile {
        width: 0.1px;
        height: 0.1px;
        opacity: 0;
        overflow: hidden;
        position: absolute;
        z-index: -1;
        outline: none;
    }

    .inputfile + label {
        max-width: 80%;
        font-size: 1.25rem;
        /* 20px */
        font-weight: 700;
        text-overflow: ellipsis;
        white-space: nowrap;
        cursor: pointer;
        display: inline-block;
        overflow: hidden;
        padding: 0.625rem 1.25rem;
        outline: none;
        /* 10px 20px */
    }

    .no-js .inputfile + label {
        display: none;
    }

    .inputfile:focus + label,
    .inputfile.has-focus + label {
        outline: 1px dotted #000;
        outline: -webkit-focus-ring-color auto 5px;
    }

    .inputfile + label * {
        /* pointer-events: none; */
        /* in case of FastClick lib use */
    }

    .inputfile + label svg {
        width: 1em;
        height: 1em;
        vertical-align: middle;
        fill: currentColor;
        margin-top: -0.25em;
        /* 4px */
        margin-right: 0.25em;
        /* 4px */
    }

    /* style 4 */

    .inputfile-4 + label {
        color: #0c0c40;
    }

    .inputfile-4 + label figure {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #0101d5;
        display: block;
        padding: 20px;
        margin: 0 auto 10px;
    }

    .inputfile-4:focus + label figure,
    .inputfile-4.has-focus + label figure,
    .inputfile-4 + label:hover figure {
        background-color: #1616ab;
        outline: none;
    }

    .inputfile-4 + label svg {
        width: 100%;
        height: 100%;
        fill: #fff;
    }

    @media screen and (max-width: 50em) {
        .inputfile-6 + label strong {
            display: block;
        }
    }
</style>
