<template>
  <div class="player">
    <h2 v-html="player.name"/>
    <p>Health {{ player.health }}</p>
    <p>Gold: {{ player.gold }}</p>
    <p>Attack: {{ player.attack }}</p>
    <p>Max hit: {{ player.max_hit }}</p>
    <p>Luck: {{ player.luck }}</p>
    <p>Score: {{ player.score }}</p>
  </div>
</template>

<script setup>
import {defineProps} from "vue";

defineProps({
  player: Object
})
</script>

<style scoped>
.player {
  padding: 0.5rem;
  border: 1px solid #d3d3d3
}

h2 {
  margin: 0;
}

p {
  margin: 0;
}
</style>