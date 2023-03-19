<template>
  <div v-if="report">
    <BattleReport :report="report" />
  </div>
  <div v-else>
    <h3>Submit Battle</h3>
    <div v-if="players.length < 2">
      <p>
        You have {{ players.length }} registered player. You need at least two players to submit a battle. <br>
        Create new player
      </p>
      <CreatePlayerForm @player-created="getActivePlayers()"/>
    </div>

    <div class="player-list" v-else>
      <div>
        <h4>Choose attacker</h4>
        <BattleListPlayers :players="players" @chosen-player="assignAttacker"/>
      </div>
      <div v-if="attacker">
        <h4>Choose defender</h4>
        <BattleListPlayers :players="players" @chosen-player="assignDefender" :selected="attacker"/>
      </div>
    </div>

    <div class="chosen-players">
      <div class="chosen-players__attacker" v-if="attacker">
        <h2>Attacker</h2>
        <PlayerDetails :player="attacker"/>
      </div>

      <div class="chosen-players__defender" v-if="defender">
        <h2>Defender</h2>
        <PlayerDetails :player="defender"/>
      </div>
    </div>


    <div v-if="confirmation" class="confirmation" v-html="confirmation" />

    <div class="cta" v-if="attacker && defender && !submitting">
      <button @click="submitBattle">Submit battle</button>
    </div>
  </div>
</template>

<script setup>
import {defineComponent, onMounted, ref} from "vue";
import {getPlayers} from "@/util";
import CreatePlayerForm from "@/components/CreatePlayerForm.vue";
import BattleListPlayers from './BattleListPlayers.vue'
import PlayerDetails from "@/components/PlayerDetails.vue"
import BattleReport from "@/components/BattleReport.vue";
import axiosInstance from "@/axiosInstance";

const players = ref([])


defineComponent({
  CreatePlayerForm,
  BattleListPlayers,
  PlayerDetails,
  BattleReport
})


const getActivePlayers = async () => {
  players.value = await getPlayers('active')
}

onMounted(async () => {
  await getActivePlayers()
})

const assignDefender = (player) => {
  defender.value = player
}

const assignAttacker = (player) => {
  attacker.value = player
  defender.value = null
}

const attacker = ref(null)
const defender = ref(null)


const report = ref(null)


const getResultReport = async() => {
  try {
    const response = await axiosInstance.get("/get-last-report")


    report.value = response.data

  } catch (error) {
    console.error(error);
  }

}

const confirmation = ref(null)
const submitting = ref(false)
const submitBattle = async () => {
  submitting.value = true
  try {
    const response = await axiosInstance.post("/submit-battle", {
      attacker_id: attacker.value.id,
      defender_id: defender.value.id,
    });

    confirmation.value = response.data.message + '. You should see the battle report soon.'

    setTimeout(getResultReport, 1000)

  } catch (error) {
    console.error(error);
  }
}


</script>

<style scoped>
.player-list {
  display: flex;
}

.chosen-players {
  display: flex;
  margin: 0 -2rem;
}

.chosen-players__attacker,
.chosen-players__defender {
  padding: 0 2rem;
  flex: 0 0 40%;
  max-width: 40%;
}

.cta {
  margin: 2rem 0;
  text-align: center;
  width: calc(80% + 4rem);
}

.cta button {
  background: green;
  cursor: pointer;
  border: none;
  color: #fff;
  padding: 0.5rem 1rem;
  font-size: 1.5rem;
}

.confirmation {
  background: green;
  width: 50%;
  margin: 1rem auto;
  text-align: center;
  padding: 0.3rem;
  color: #fff;
}

</style>