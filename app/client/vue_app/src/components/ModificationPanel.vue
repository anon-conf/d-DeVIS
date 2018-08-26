<template>
  <div>
    <b-row align-h="center" >
      <circle-slider :side="150" v-model="parameters.slicing" text="Slicing"
                     show-value></circle-slider>
      <circle-slider :side="150" v-model="parameters.crossfading" text="Crossfading" show-value></circle-slider>
      <circle-slider :side="150" v-model="parameters.loudness" text="Loudness" show-value></circle-slider>
      <circle-slider :side="150" v-model="parameters.fade" text="Fade" show-value></circle-slider>
      <circle-slider :side="150" v-model="parameters.repeat" text="Repeat" show-value></circle-slider>
      <circle-check v-model="parameters.invert"></circle-check>
    </b-row>

  </div>
</template>

<script>
// import axios from 'axios'
// import config from '../config'

import {CircleSlider} from 'vue-circle-slider'
import CircleCheck from './CircleCheck'

console.log(CircleSlider)
// const {rootUrl} = config

export default {
  name: 'ModificationPanel',
  components: {
    circleSlider: CircleSlider,
    circleCheck: CircleCheck
  },
  props: ['parameters']
}

</script>

<style scoped>

  *,
  *:after,
  *:before {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  body {
    font-family: Avenir, 'Helvetica Neue', 'Lato', 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #4b0f31;
    background-color: #f1e5e6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

</style>
