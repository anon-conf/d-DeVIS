<template>
    <div class="recorder">
        <i @click="goBack" class="back-button">←</i>
        <div class="microphone">
            <span></span>
            <svg :class="svgClass" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                 width="5" height="5" viewBox="0 0 58 60">
                <g>
                    <path d="M44,28c-0.552,0-1,0.447-1,1v6c0,7.72-6.28,14-14,14s-14-6.28-14-14v-6c0-0.553-0.448-1-1-1s-1,0.447-1,1v6   c0,8.485,6.644,15.429,15,15.949V56h-5c-0.552,0-1,0.447-1,1s0.448,1,1,1h12c0.552,0,1-0.447,1-1s-0.448-1-1-1h-5v-5.051   c8.356-0.52,15-7.465,15-15.949v-6C45,28.447,44.552,28,44,28z"
                          fill="#54a0e4"></path>
                    <path d="M29,46c6.065,0,11-4.935,11-11V11c0-6.065-4.935-11-11-11S18,4.935,18,11v24C18,41.065,22.935,46,29,46z"
                          fill="#54a0e4"></path>
                </g>
            </svg>

        </div>
        <br>
        <div class="actions">
            <div>
                <v-btn v-show="status==='waiting'" @click="status = 'recording'" depressed><i
                        class="btn-icon" style="color: red; margin-left: -4px;">&#x25CF;</i>
                    Record
                </v-btn>
                <v-btn v-show="status==='recording'" @click="status = 'stopped'" depressed><i
                        class="btn-icon" style="margin-left: -5px;">&#x25A0;</i>
                    Stop
                </v-btn>
                <div v-show="status === 'stopped'">
                    <v-btn @click="status = 'waiting'" depressed><i
                            class="btn-icon">&#x274C;</i>
                        Discard
                    </v-btn>
                    <v-btn @click="status = 'waiting'" depressed><i
                            class="btn-icon">&#x2705;</i>
                        Save
                    </v-btn>

                </div>

            </div>


        </div>
    </div>
</template>

<script>
    export default {
        name: "AudioRecorder",
        data() {
            return {
                status: 'waiting'
            }
        },
        methods: {
            goBack(){
                this.$emit('back-click');
            }
        },
        computed: {
            svgClass() {

                return this.status === 'waiting' || this.status === 'stopped' ? {'animated': false} : {'animated': true};
            }
        }
    }
</script>

<style scoped>

    .animated {
        animation: pulse 2s infinite;
    }

    .back-button {
        position: absolute;
        top: 0;
        left: 0;
        font-size: 2.5rem;
        font-weight: 700;
        cursor: pointer;
    }
    .btn-icon {
        padding: 0;
        font-size: 2rem;
        margin-top: -2px;
        margin-right: 8px;
        margin-left: -13px;
    }

    .microphone svg {
        width: 6em;
        height: 6em;
        vertical-align: middle;
        /*text-align: center;*/
        fill: currentColor;
        border-radius: 50%;
        padding: 10px;
        text-align: center;

        /*box-shadow: 0 0 0 rgba(204, 169, 44, 0.4);*/

        /* 4px */
    }

    .recorder {
        font-weight: 700;
        font-size: 1.3rem;
    }

    @-webkit-keyframes pulse {
        0% {
            -webkit-box-shadow: 0 0 0 0 rgba(84, 160, 228, 0.4);
        }
        70% {
            -webkit-box-shadow: 0 0 0 30px rgba(84, 160, 228, 0);
        }
        100% {
            -webkit-box-shadow: 0 0 0 0 rgba(84, 160, 228, 0);
        }
    }

    @keyframes pulse {
        0% {
            -moz-box-shadow: 0 0 0 0 rgba(84, 160, 228, 0.4);
            box-shadow: 0 0 0 0 rgba(84, 160, 228, 0.4);
        }
        70% {
            -moz-box-shadow: 0 0 0 30px rgba(84, 160, 228, 0);
            box-shadow: 0 0 0 30px rgba(84, 160, 228, 0);
        }
        100% {
            -moz-box-shadow: 0 0 0 0 rgba(84, 160, 228, 0);
            box-shadow: 0 0 0 0 rgba(84, 160, 228, 0);
        }
    }

</style>