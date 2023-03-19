<template>
  <div>
  <h3>Leaderboard</h3>
  <table v-if="leaderboard.length">
    <tr>
      <th>Rank</th>
      <th>Name</th>
      <th>Score</th>
    </tr>

    <tr v-for="(entry, key) in leaderboard" :key="key">
      <td v-html="entry.rank" />
      <td v-html="entry.player_name" />
      <td v-html="entry.score " />
    </tr>

  </table>

    <div class="no-result" v-else>
      It looks like any battle has been performed. Submit a battle to update the ranking.
    </div>

  </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
  import axiosInstance from "@/axiosInstance";

  const leaderboard = ref([])

  const getLeaderboard = async () => {
    try {
      const response = await axiosInstance.get("/leaderboard");
      leaderboard.value = response.data;
    } catch (error) {
      console.error(error);
    }
  }

onMounted(async () => {
  await getLeaderboard()
})


</script>

<style scoped>
  .no-result {
    margin-bottom: 1rem;
  }
</style>