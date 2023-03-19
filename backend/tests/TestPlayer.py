import unittest
from app.models import Player


class TestPlayer(unittest.TestCase):
    def test_create_player_with_valid_name(self):
        player = Player.create("Test")
        self.assertIsInstance(player, Player)
        self.assertEqual(player.name, "Test")

    def test_create_player_with_empty_name(self):
        with self.assertRaises(ValueError):
            Player.create("")

    def test_create_player_with_long_name(self):
        with self.assertRaises(ValueError):
            Player.create("This name is too long")

    def test_player_attributes(self):
        player = Player.create("Test")
        self.assertGreater(player.max_hit, 99)
        self.assertLess(player.max_hit, 200)

        self.assertGreater(player.luck, 9)
        self.assertLess(player.luck, 101)


if __name__ == '__main__':
    unittest.main()
