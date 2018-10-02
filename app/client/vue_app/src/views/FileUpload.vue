<template>
    <div class="body">
        <b-container>
            <b-row class="mt-5">
                <b-col class="mt-5">
                    <b-container class="mt-5">

                        <div class="content">

                            <div class="box">
                                <form action="http://localhost:5000/uploader" method="POST"
                                      enctype="multipart/form-data" @submit.prevent="uploadFile">
                                    <input type="file" name="file" id="file-4" @change="playMedia"
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
                                    <br/><input type="submit" class="btn btn-primary" value="Upload The File"/>
                                </form>
                                <div v-show="showAudio" class="mt-2">

                                    <canvas id="canvas" ref="canvas"></canvas>
                                    <audio id="audio" ref="audioControl" controls></audio>
                                </div>
                            </div>

                        </div>

                    </b-container>

                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import $backend from '@/backend'

    export default {
        name: 'uploadForm',
        data() {
            return {
                file: null,
                showAudio: false
            }
        },
        methods: {
            uploadFile() {
                const formData = new FormData();

                if (!this.file) return;

                formData.append('file', this.file);
                console.log($backend);

                $backend.post(`/resources/audio`,
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                ).then(response => response.data)
                    .then(response => {
                        if (response.success) {
                            console.log(response);
                            localStorage.setItem('fileSendResponse', response);
                            this.$router.push('visualize')
                        }
                    })
                    .catch(error => console.log(error))
            },

            playMedia(event) {
                this.file = event.target.files[0];
                const audio = this.$refs['audioControl'];
                const canvas = this.$refs['canvas'];
                this.showAudio = true;
                audio.src = URL.createObjectURL(this.file);
                audio.load();
                audio.play();
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                const src = audioContext.createMediaElementSource(audio);
                const analyser = audioContext.createAnalyser();

                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight * 0.7;
                console.log(canvas.height);
                const ctx = canvas.getContext('2d');

                src.connect(analyser);
                analyser.connect(audioContext.destination);

                analyser.fftSize = 256;

                const bufferLength = analyser.frequencyBinCount;
                console.log(bufferLength);

                const dataArray = new Uint8Array(bufferLength);

                const WIDTH = canvas.width;
                const HEIGHT = canvas.height;

                const barWidth = (WIDTH / bufferLength) * 2.5;
                let barHeight;
                let x = 0;

                function renderFrame() {
                    requestAnimationFrame(renderFrame);

                    x = 0;

                    analyser.getByteFrequencyData(dataArray);

                    ctx.fillStyle = '#000';
                    ctx.fillRect(0, 0, WIDTH, HEIGHT);

                    for (let i = 0; i < bufferLength; i++) {
                        barHeight = dataArray[i];

                        let r = barHeight + (25 * (i / bufferLength));
                        let g = 250 * (i / bufferLength);
                        let b = 50;

                        ctx.fillStyle = 'rgb(' + r + ',' + g + ',' + b + ')';
                        ctx.fillRect(x, HEIGHT - barHeight, barWidth, barHeight);

                        x += barWidth + 1
                    }
                }

                audio.play();
                renderFrame()
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

    .body {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        font-family: Avenir, 'Helvetica Neue', 'Lato', 'Segoe UI', Helvetica, Arial, sans-serif;
        color: #4b0f31;
        background-color: #f1e5e6;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    a {
        outline: none;
        color: #d3394c;
        text-decoration: none;
    }

    a:hover,
    a:focus {
        color: #722040;
    }

    .codrops-header h1 span {
        display: block;
        padding: 0.5em 0 1em;
        color: #999;
        font-weight: normal;
        font-size: 0.45em;
    }

    /* Content */

    .content {
        width: 100%;
        max-width: 800px;
        text-align: center;
        margin: 0 auto;
        padding: 0 0 3em 0;

    }

    /*.content footer {*/
        /*color: #b39295;*/
        /*margin-top: 40px;*/
    /*}*/

    /*.content footer a:hover,*/
    /*.content footer a:focus {*/
        /*color: #4b0f31;*/
    /*}*/

    .box {
        background-color: #dfc8ca;
        padding: 6.25rem 1.25rem;
         /*border: 1px solid dimgray;*/
        -webkit-box-shadow: 1px 0px 14px 0px rgba(0, 0, 0, 0.87);
        -moz-box-shadow: 1px 0px 14px 0px rgba(0, 0, 0, 0.87);
        box-shadow: 1px 0px 14px 0px rgba(0, 0, 0, 0.87);
    }

    .box + .box {
        margin-top: 2.5rem;
    }

    canvas {
        width: 100%;
        height: auto;
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

    /* style 1 */

    .inputfile-1 + label {
        color: #f1e5e6;
        background-color: #d3394c;
    }

    .inputfile-1:focus + label,
    .inputfile-1.has-focus + label,
    .inputfile-1 + label:hover {
        background-color: #722040;
    }

    /* style 2 */

    .inputfile-2 + label {
        color: #d3394c;
        border: 2px solid currentColor;
    }

    .inputfile-2:focus + label,
    .inputfile-2.has-focus + label,
    .inputfile-2 + label:hover {
        color: #722040;
    }

    /* style 3 */

    .inputfile-3 + label {
        color: #d3394c;
    }

    .inputfile-3:focus + label,
    .inputfile-3.has-focus + label,
    .inputfile-3 + label:hover {
        color: #722040;
    }

    /* style 4 */

    .inputfile-4 + label {
        color: #d3394c;
    }

    .inputfile-4:focus + label,
    .inputfile-4.has-focus + label,
    .inputfile-4 + label:hover {
        color: #722040;
    }

    .inputfile-4 + label figure {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #d3394c;
        display: block;
        padding: 20px;
        margin: 0 auto 10px;
    }

    .inputfile-4:focus + label figure,
    .inputfile-4.has-focus + label figure,
    .inputfile-4 + label:hover figure {
        background-color: #722040;
    }

    .inputfile-4 + label svg {
        width: 100%;
        height: 100%;
        fill: #f1e5e6;
    }

    /* style 5 */

    .inputfile-5 + label {
        color: #d3394c;
    }

    .inputfile-5:focus + label,
    .inputfile-5.has-focus + label,
    .inputfile-5 + label:hover {
        color: #722040;
    }

    .inputfile-5 + label figure {
        width: 100px;
        height: 135px;
        background-color: #d3394c;
        display: block;
        position: relative;
        padding: 30px;
        margin: 0 auto 10px;
    }

    .inputfile-5:focus + label figure,
    .inputfile-5.has-focus + label figure,
    .inputfile-5 + label:hover figure {
        background-color: #722040;
    }

    .inputfile-5 + label figure::before,
    .inputfile-5 + label figure::after {
        width: 0;
        height: 0;
        content: '';
        position: absolute;
        top: 0;
        right: 0;
    }

    .inputfile-5 + label figure::before {
        border-top: 20px solid #dfc8ca;
        border-left: 20px solid transparent;
    }

    .inputfile-5 + label figure::after {
        border-bottom: 20px solid #722040;
        border-right: 20px solid transparent;
    }

    .inputfile-5:focus + label figure::after,
    .inputfile-5.has-focus + label figure::after,
    .inputfile-5 + label:hover figure::after {
        border-bottom-color: #d3394c;
    }

    .inputfile-5 + label svg {
        width: 100%;
        height: 100%;
        fill: #f1e5e6;
    }

    /* style 6 */

    .inputfile-6 + label {
        color: #d3394c;
    }

    .inputfile-6 + label {
        border: 1px solid #d3394c;
        background-color: #f1e5e6;
        padding: 0;
    }

    .inputfile-6:focus + label,
    .inputfile-6.has-focus + label,
    .inputfile-6 + label:hover {
        border-color: #722040;
    }

    .inputfile-6 + label span,
    .inputfile-6 + label strong {
        padding: 0.625rem 1.25rem;
        /* 10px 20px */
    }

    .inputfile-6 + label span {
        width: 200px;
        min-height: 2em;
        display: inline-block;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
        vertical-align: top;
    }

    .inputfile-6 + label strong {
        height: 100%;
        color: #f1e5e6;
        background-color: #d3394c;
        display: inline-block;
    }

    .inputfile-6:focus + label strong,
    .inputfile-6.has-focus + label strong,
    .inputfile-6 + label:hover strong {
        background-color: #722040;
    }

    @media screen and (max-width: 50em) {
        .inputfile-6 + label strong {
            display: block;
        }
    }

</style>
