<template>
  <nav>
    <ul>
      <li v-for="item in nav" :key="item.slug">
        <button @click="emit('currentPage', item.slug)" v-html="item.name" />
      </li>
    </ul>
  </nav>
</template>

<script setup>
import {defineEmits, ref} from 'vue';
 const emit = defineEmits(['currentPage'])


const nav = ref([
  {
    'name': 'Create character',
    'slug': 'create'
  },
  {
    'name': 'Get players',
    'slug': 'players'
  },
  {
    'name': 'Submit battle',
    'slug': 'battle'
  },
  {
    'name': 'Leaderboards',
    'slug': 'leaderboards'
  },
])

</script>

<style scoped>
  ul {
    list-style-type: none;
    padding: 0;
    display: flex;
    margin: 0 -0.5rem;
  }

  li {
    padding: 0 0.5rem;
  }
</style>