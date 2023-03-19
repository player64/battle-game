<template>
  <div>
    <h2>Winner: {{ report.winner }}</h2>
    <h2>Loser: {{report.loser}}</h2>

    Steps:
    <div class="turns" v-if="report.turns.length">
      <BattleReportTurn class="turns__item" v-for="(step, key) in report.turns" :key="key" :stepNo="key" :step="step" />
    </div>

  </div>
</template>

<script setup>
import {defineProps, defineComponent} from 'vue'
import BattleReportTurn from "@/components/BattleReportTurn.vue";
defineProps({
  report: Object
})

defineComponent(
    BattleReportTurn
)
</script>

<style scoped>
  .turns {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin: 0 -0.5rem;
  }

  .turns__item {
    border: 1px solid #d3d3d3;
    padding: 0.5rem;
    margin: 0.5rem;
  }
</style>