import unittest

from app.models import GameStorage, Player


class TestGameStorage(unittest.TestCase):
    def setUp(self):
        self.storage = GameStorage()
        self.players = [
            Player('John'),
            Player('Jane'),
            Player('Jack')
        ]

    def test_add_player(self):
        player = self.players[0]
        self.storage.add_player(player)
        self.assertIn(player.id, self.storage._players)

    def test_active_players(self):
        for player in self.players:
            self.storage.add_player(player)
        active_players = self.storage.active_players
        self.assertEqual(len(active_players), len(self.players))
        for player in active_players:
            self.assertGreater(player.health, 0)

    def test_dead_players(self):
        for player in self.players:
            player.health = 0
            self.storage.add_player(player)
        dead_players = self.storage.dead_players
        self.assertEqual(len(dead_players), len(self.players))
        for player in dead_players:
            self.assertEqual(player.health, 0)

    def test_add_report(self):
        report = {'winner': 'John', 'loser': 'Jane'}
        self.storage.add_report(report)
        self.assertEqual(len(self.storage.battle_reports), 1)
        self.assertEqual(self.storage.battle_reports[0], report)

    def test_get_reports(self):
        report1 = {'winner': 'John', 'loser': 'Jane'}
        report2 = {'winner': 'Jane', 'loser': 'Jack'}
        self.storage = GameStorage()
        self.storage.add_report(report1)
        self.storage.add_report(report2)
        reports = self.storage.get_reports()

        self.assertGreater(len(reports), 1)
        self.assertIn(report1, reports)
        self.assertIn(report2, reports)

    def test_get_last_report(self):
        report1 = {'winner': 'John', 'loser': 'Jane'}
        report2 = {'winner': 'Jane', 'loser': 'Jack'}
        self.storage.add_report(report1)
        self.storage.add_report(report2)
        last_report = self.storage.get_last_report()
        self.assertEqual(last_report, report2)

    def test_get_player_by_id(self):
        player = self.players[0]
        self.storage.add_player(player)
        found_player = self.storage.get_player_by_id(player.id)
        self.assertEqual(found_player, player)

    def test_get_player_by_nonexistent_id(self):
        player = self.players[0]
        self.storage.add_player(player)
        found_player = self.storage.get_player_by_id('nonexistent_id')
        self.assertIsNone(found_player)


if __name__ == '__main__':
    unittest.main()
