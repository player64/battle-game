<template>
  <div>
    <ul>
      <li v-for="(player, key) in players" :key="player.id">
        <button :class="{'active': key === chosen}" @click="chosenPlayer(key)"
                :disabled="(selected && selected.id === player.id)">
          {{player.name}} - Health: {{player.health}}; Gold: {{player.gold}}
        </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import {defineEmits, defineProps, ref, watch} from "vue";

const emit = defineEmits(['chosenPlayer'])

const chosen = ref(null)

const props = defineProps({
  players: Array,
  selected: {
    type: Object,
    required: false
  }
})

const chosenPlayer = (index) => {
  if(index === chosen.value) return

  chosen.value = index
  emit('chosenPlayer', props.players[index])
}
watch(() => props.selected, () => {

    chosen.value = null

})



</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 0.5rem;
}

button {
  cursor: pointer;
  display: block;
  width: 100%;
  border: none;
  background: none;
  text-align: left;
  padding: 0.2rem 0.3rem;
}

button[disabled] {
  cursor: default;
  padding: 0;
}

button.active {
  background: blue;
  color: #fff;
}
</style>