<template>
  <form @submit.prevent="createPlayer">
  <input v-model="playerName" placeholder="Enter player name" />
  <button type="submit">Create</button>
  </form>
  <div v-if="errors !== null && errors.length">
    <div v-for="(error, key) in errors" :key="key" class="error" v-html="error" />
  </div>

  <div v-if="message !== ''" v-html="message"></div>
</template>

<script setup>
import {defineEmits, ref} from "vue";
import axiosInstance from "@/axiosInstance";
const emit = defineEmits(['playerCreated'])
const playerName = ref('')
const errors = ref([])

const message = ref('')
const createPlayer = async () => {
  errors.value = []

  if(playerName.value.trim() === '') {
    errors.value.push('Name cannot be empty')
    return
  }

  if(playerName.value.length > 20) {
    errors.value.push('Name cannot extend 20 characters')
    return
  }

  try {
    const response = await axiosInstance.post("/create-player", { name: playerName.value });
    playerName.value = ''
    message.value = `Player ${response.data.player_name} has been created!`
    createPlayer.value = ''
    emit('playerCreated')
  } catch (error) {
    console.error(error);
  }
}
</script>

<style scoped>

</style>