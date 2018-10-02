<template>
    <div class="full-screen">
        <div class="header">
            <div @click="activateLayer(1)" :class="layerOneClass"><span class="layer__step">1</span>
                <div class="layer__label">Name of step 1</div>
            </div>
            <hr class="layer-divider theme--light">
            <div @click="activateLayer(2)" :class=layerTwoClass><span class="layer__step">2</span>
                <div class="layer__label">Name of step 2</div>
            </div>
            <hr class="layer-divider theme--light">
            <div @click="activateLayer(3)" :class="layerThreeClass"><span class="layer__step">3</span>
                <div class="layer__label">Name of step 3</div>
            </div>
        </div>

        <div class="image-grid">
            <div class="item">1</div>
            <div class="item">2</div>
            <div class="item">3</div>
            <div class="item">4</div>
            <div class="item">5</div>
            <div class="item">6</div>
            <div class="item">7</div>
            <div class="item">8</div>
            <div class="item">9</div>
            <div class="item">10</div>
            <div class="item">11</div>
            <div class="item">12</div>
            <div class="item">13</div>
            <div class="item">14</div>
            <div class="item">15</div>
            <div class="item">16</div>
        </div>
    </div>
</template>

<script>
    const print = console.log;
    export default {
        name: "VisualizeLayer",
        data(){
            return {
                activeLayer: 1
            }
        },
        methods: {
            activateLayer(layer){
                this.activeLayer = parseInt(layer);
            }
        },
        computed: {
            layerOneClass(){
                return {
                    'layer': true,
                    'layer__step--active': this.activeLayer === 1,
                    'layer__step--inactive': this.activeLayer !== 1,
                }
            },
            layerTwoClass(){
                return {
                    'layer': true,
                    'layer__step--active': this.activeLayer === 2,
                    'layer__step--inactive': this.activeLayer !== 2,
                }
            },
            layerThreeClass(){
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

    .layer {
        align-items: center;
        display: flex;
        flex-direction: row;
        padding: 24px;
        position: relative;
        cursor: pointer;
    }

    .layer__step {
        align-items: center;
        color: #fff;
        border-radius: 50%;
        display: inline-flex;
        font-size: 12px;
        justify-content: center;
        height: 24px;
        margin-right: 8px;
        min-width: 24px;
        width: 24px;
        transition: 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);

    }

    .layer__label {
        align-items: flex-start;
        display: flex;
        flex-direction: column;
        text-align: left;
    }

    .layer__step .layer__label {
        color: rgba(0,0,0,0.38)
    }

    .layer__step--active .layer__label {
        transition: 0.3s cubic-bezier(0.4, 0, 0.6, 1);
        text-shadow: 0px 0px 0px #000;
    }

    .layer__step--active .layer__step {
        background-color: #1867c0 !important;
        border-color: #1867c0 !important;
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

    .layer__step--inactive .layer__step {
        background: rgba(0, 0, 0, 0.38);
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