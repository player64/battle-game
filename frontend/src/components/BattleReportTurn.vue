<template>
  <div class="step">
    <h6>Step {{stepNo + 1}}</h6>
    <p>Attacker: {{step.attacker}}</p>
    <p>Defender: {{step.defender}}</p>
    <p>Attack missed: {{step.attack_missed}}</p>
    <p>Damages: {{step.damages}}</p>
    <p>Attacker health: {{step.attacker_health}}</p>
    <p>Defender health: {{step.defender_health}}</p>
  </div>
</template>

<script setup>
 import {defineProps} from "vue";

 defineProps({
   step: Object,
   // eslint-disable-next-line vue/no-reserved-props
   stepNo: Number
 })
</script>

<style scoped>
  h6 {
    margin: 0;
    font-size: 1.3rem;
  }

  p {
    margin: 0 0 0.3rem 0;
  }
</style>