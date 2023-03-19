import random
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

from app.models import Battle, Leaderboard, Player, GameStorage

battle_queue = Queue()
global_leaderboard = Leaderboard()
global_storage = GameStorage()


def battle_processor():
    print("Battle processor has been executed")
    """
    function runs continuously and processes battles in the order they are added to the battle_queue.
    It uses a ThreadPoolExecutor to execute battles concurrently.
    """
    with ThreadPoolExecutor():
        while True:
            battle_data = battle_queue.get()
            attacker = battle_data["attacker"]
            defender = battle_data["defender"]

            battle = Battle(attacker, defender)
            battle.process_battle()
            battle_report = battle.generate_battle_report()

            winner: Player = battle.winner
            loser: Player = battle.loser
            # gold stolen should be between 10% and 20% of their total amount of gold
            stolen_gold = int(loser.gold * random.uniform(0.1, 0.2))

            winner.gold += stolen_gold
            loser.gold -= stolen_gold

            global_leaderboard.update_player_score(winner, winner.score + stolen_gold)
            global_leaderboard.update_player_score(loser, loser.score - stolen_gold)

            # update storage
            global_storage.add_player(winner)
            global_storage.add_player(loser)
            global_storage.add_report(battle_report)

            print("Updated leaderboard:", global_leaderboard.get_leaderboard())
