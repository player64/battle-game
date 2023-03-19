import unittest
import heapq
from app.models import Player, Leaderboard


class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard()
        self.player1 = Player.create("Player1")
        self.player2 = Player.create("Player2")
        self.player3 = Player.create("Player3")

    def test_add_player(self):
        self.leaderboard.add_player(self.player1)
        self.leaderboard.add_player(self.player2)

        # Check that players are added to the leaderboard
        self.assertIn((-self.player1.score, self.player1.name), self.leaderboard.leaderboard)
        self.assertIn((-self.player2.score, self.player2.name), self.leaderboard.leaderboard)

    def test_update_player_score(self):
        self.leaderboard.add_player(self.player1)
        self.leaderboard.add_player(self.player2)

        new_score = self.player1.score + 10
        self.leaderboard.update_player_score(self.player1, new_score)

        # Check that the player's score is updated in the leaderboard
        self.assertIn((-new_score, self.player1.name), self.leaderboard.leaderboard)
        self.assertEqual(self.player1.score, new_score)

    def test_get_leaderboard(self):
        self.player1.score = 20
        self.player2.score = 10
        self.player3.score = 30

        self.leaderboard.add_player(self.player1)
        self.leaderboard.add_player(self.player2)
        self.leaderboard.add_player(self.player3)

        # Test getting the full leaderboard
        full_leaderboard = self.leaderboard.get_leaderboard()
        self.assertEqual(len(full_leaderboard), 3)

        # Test the order of the players in the leaderboard
        self.assertEqual(full_leaderboard[0]['player_name'], self.player3.name)
        self.assertEqual(full_leaderboard[1]['player_name'], self.player1.name)
        self.assertEqual(full_leaderboard[2]['player_name'], self.player2.name)

        # Test getting a limited number of entries from the leaderboard
        top_two = self.leaderboard.get_leaderboard(2)
        self.assertEqual(len(top_two), 2)
        self.assertEqual(top_two[0]['player_name'], self.player3.name)
        self.assertEqual(top_two[1]['player_name'], self.player1.name)


if __name__ == '__main__':
    unittest.main()
