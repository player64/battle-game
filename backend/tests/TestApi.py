import json
import unittest
from threading import Thread

import time


from app import create_app, global_leaderboard, battle_processor
from app.models import Player
from app import global_storage


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

        # Start the battle_processor thread
        self.battle_processor_thread = Thread(target=battle_processor, daemon=True)
        self.battle_processor_thread.start()

        self.client = self.app.test_client()

        # Clean up global storage and leaderboard before each test
        global_storage._players = {}
        global_storage._reports = []
        global_leaderboard.leaderboard = []

        # Add some sample players to global_storage for testing purposes
        self.sample_player1 = Player.create("Player 1")
        self.sample_player2 = Player.create("Player 2")
        global_storage.add_player(self.sample_player1)
        global_storage.add_player(self.sample_player2)

    def test_create_player(self):
        response = self.client.post(
            '/create-player',
            json={"name": "Player 1"}
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("player_id", data)
        self.assertIn("player_name", data)
        self.assertEqual(data["player_name"], "Player 1")

    def test_get_active_players(self):
        player = Player.create("Player 2")
        global_storage.add_player(player)

        response = self.client.get('/get-players')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_get_reports(self):
        response = self.client.get('/get-reports')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_submit_battle(self):
        player1 = Player.create("Player 3")
        player2 = Player.create("Player 4")
        global_storage.add_player(player1)
        global_storage.add_player(player2)

        response = self.client.post(
            '/submit-battle',
            json={"attacker_id": player1.id, "defender_id": player2.id}
        )
        self.assertEqual(response.status_code, 202)
        data = response.get_json()
        self.assertIn("message", data)

        # Add a delay to give the battle_processor time to process the battle
        time.sleep(1)

        response = self.client.get('/leaderboard')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertGreater(len(data), 0)


if __name__ == '__main__':
    unittest.main()
