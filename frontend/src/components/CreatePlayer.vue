<template>
  <div>
    <h3>Create Player</h3>
    <CreatePlayerForm />
  </div>
</template>

<script setup>
import {defineComponent} from "vue";
import CreatePlayerForm from "@/components/CreatePlayerForm.vue";

defineComponent({
  CreatePlayerForm
})
</script>

<style scoped>

</style>