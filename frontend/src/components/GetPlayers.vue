<template>
  <h3>{{(type === 'active') ? 'Active' : 'Dead'}} Players</h3>

  <ul>
    <li>Filter by</li>
    <li>
      <button @click="getPlayerType('active')" :disabled="(type === 'active')">Active</button>
    </li>
    <li>
      <button @click="getPlayerType('dead')" :disabled="(type === 'dead')">Dead</button>
    </li>
  </ul>

  <table v-if="players.length">
    <tr>
      <th>#</th>
      <th>Name</th>
      <th>Health</th>
      <th>Gold</th>
      <th>Score</th>
    </tr>
    <tr v-for="(player, key ) in players" :key="key">
      <td v-html="`${key + 1}.`" />
      <th class="text-left" v-html="player.name" />
      <td v-html="player.health " />
      <td v-html="player.gold" />
      <td v-html="player.score" />
    </tr>
  </table>

  <div class="no-result" v-else>
    <div v-if="type === 'active'">
      <p>There is no registered players.You can create here:</p>
      <CreatePlayerForm @player-created="getPlayerType('active')" />
    </div>
    <div v-else-if="type === 'dead'">
      There is no dead players yet. Submit the battle
    </div>
  </div>
</template>

<script setup>
import {defineComponent, onMounted, ref} from "vue";
const players = ref([])
import {getPlayers} from '@/util'
import CreatePlayerForm from "@/components/CreatePlayerForm.vue";


const type = ref('active')

defineComponent(CreatePlayerForm)

const getPlayerType = async (typeValue) => {
  type.value = typeValue
  players.value = await getPlayers(typeValue)
}


onMounted(async () => {
  await getPlayerType('active')
})
</script>

<style scoped>
  .no-result {
    margin-top: 1rem;
  }

  th {
    text-align: left;
  }

  th,
  td {
    padding: 0.3rem;
  }

  ul {
    list-style-type: none;
    display: flex;
    padding: 0;
    margin: 0 -0.3rem;
  }

  li {
    padding: 0 0.3rem;
  }
</style>