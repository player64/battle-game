<template>
  <AppNav @currentPage="setPage"/>
  <component v-if="currentComponent" :is="currentComponent"/>
  <div v-else>
    <h1>The battle game</h1>
    Use the navigation above to Create, get players to submit battles or display the leaderboard
  </div>
</template>

<script setup>
import {defineAsyncComponent, defineComponent, markRaw, ref} from "vue";
import AppNav from "./components/AppNav.vue"

defineComponent({
  AppNav
})

const currentPage = ref(null)

const setPage = (page) => {
  currentPage.value = page
  resolveComponent()
}

const currentComponent = ref(null);

const resolveComponent = async () => {
  if (!currentPage.value) return
  let componentName;
  switch (currentPage.value) {
    case 'create':
      componentName = 'CreatePlayer'
      break
    case 'players':
      componentName = 'GetPlayers'
      break
    case 'leaderboards':
      componentName = 'LeaderBoard'
      break
    case 'battle':
      componentName = 'SubmitBattle'
      break
    default:
      return
  }


  const component = defineAsyncComponent(() =>
      import(`./components/${componentName}.vue`)
  );

  currentComponent.value = markRaw(component);


}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
