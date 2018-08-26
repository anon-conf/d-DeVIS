<template>
  <i @click="updateValue"
     class="fas fa-check-circle fa-10x toggle"
     :class="switchStyleObject">
    <svg aria-hidden="true" data-prefix="fas" data-icon="check-circle" class="svg-inline--fa fa-check-circle fa-w-16"
         role="img" xmlns="http://www.w3.org/2000/svg" width="150px" height="150px"  viewBox="0 0 512 512" >

<g>
  <path fill="currentColor"
  d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zM227.314 387.314l184-184c6.248-6.248 6.248-16.379 0-22.627l-22.627-22.627c-6.248-6.249-16.379-6.249-22.628 0L216 308.118l-70.059-70.059c-6.248-6.248-16.379-6.248-22.628 0l-22.627 22.627c-6.248 6.248-6.248 16.379 0 22.627l104 104c6.249 6.249 16.379 6.249 22.628.001z"></path>
  <text x="27%" y="30%" font-size="75" :fill="textColor">Invert</text>
</g>

    </svg>
  </i>

</template>

<script>
export default {
  name: 'CircleCheck',
  props: {
    value: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    updateValue () {
      this.$emit('input', !this.value)
    }
  },
  computed: {
    switchStyleObject () {
      return {
        'pulsate-fwd': this.value
      }
    },
    textColor () {
      return this.value ? 'white' : 'black'
    }
  }
}
</script>

<style scoped>

  .toggle {

    background-color: #fff;
    border-radius: 50%;
    width: 100px;
    color: #eee;
    cursor: pointer;
  }

  text {
    font: 80px sans-serif;
  }

  .pulsate-fwd {
    -webkit-animation: pulsate-fwd 0.5s ease-in-out both;
    animation: pulsate-fwd 0.5s ease-in-out forwards;
  }

  .pulsate-bkd {
    -webkit-animation: pulsate-fwd 0.5s ease-in-out reverse;
    animation: pulsate-fwd 0.5s ease-in-out reverse;
  }

  @-webkit-keyframes pulsate-fwd {
    0% {
      -webkit-transform: scale(1);
      transform: scale(1);
      color: #eee;
    }
    50% {
      -webkit-transform: scale(1.1);
      transform: scale(1.1);
    }
    100% {
      -webkit-transform: scale(1);
      transform: scale(1);
      color: #00be7e;
    }
  }

  @keyframes pulsate-fwd {
    0% {
      -webkit-transform: scale(1);
      transform: scale(1);
      color: #eee;
    }
    50% {
      -webkit-transform: scale(1.1);
      transform: scale(1.1);
    }
    100% {
      -webkit-transform: scale(1);
      transform: scale(1);
      color: #00be7e;
    }
  }

</style>
