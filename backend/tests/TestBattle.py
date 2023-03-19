import unittest
from unittest.mock import patch
from app.models import Battle
from app.models import Player


class TestBattle(unittest.TestCase):
    def setUp(self):

        self.attacker = Player.create("Attacker")
        self.defender = Player.create("Defender")
        self.battle = Battle(self.attacker, self.defender)

    def test_turn(self):
        with patch('random.randint', return_value=1):
            self.battle.turn()
            self.assertEqual(len(self.battle.turns), 1)
            self.assertEqual(self.battle.turns[0]['attacker'], self.attacker.id)
            self.assertEqual(self.battle.turns[0]['defender'], self.defender.id)

    def test_attack_missed(self):
        with patch('random.randint', return_value=50):
            player = Player.create("Attacker")
            player.luck = 10
            self.assertFalse(self.battle.attack_missed(player))

        with patch('random.randint', return_value=100):
            player = Player.create("Attacker")
            player.luck = 50
            self.assertFalse(self.battle.attack_missed(player))

    def test_calculate_attack_damage(self):
        # create new attacker
        attacker = Player.create("Attacker")

        attacker.max_hit = 100
        attacker.attack = 50

        battle = Battle(attacker, self.defender)
        # Test case: Attacker has full health
        self.assertEqual(battle.calculate_attack_damage(attacker), 50)

        # Test case: Attacker has 50% health
        attacker.health = 50
        self.assertEqual(battle.calculate_attack_damage(attacker), 25)

        # Test case: Attacker has 0% health (should not happen in practice)
        attacker.hit_points = 0
        self.assertEqual(battle.calculate_attack_damage(attacker), 25)

        # Test case: Attacker has 75% health
        attacker.hit_points = 75
        self.assertEqual(battle.calculate_attack_damage(attacker), 25)

    def test_turn(self):
        initial_attacker_health = self.attacker.health
        initial_defender_health = self.defender.health

        self.battle.turn()

        # Test that the attacker and defender have switched places
        self.assertEqual(self.battle.attacker, self.defender)
        self.assertEqual(self.battle.defender, self.attacker)

        # Test that the attacker's health has not changed after one turn
        self.assertEqual(self.attacker.health, initial_attacker_health)

        # Test that the defender's health has changed after one turn (unless the attack was missed)
        turn_data = self.battle.turns[-1]
        if not turn_data['attack_missed']:
            self.assertEqual(self.defender.health, initial_defender_health - turn_data['damages'])
        else:
            self.assertEqual(self.defender.health, initial_defender_health)

    def test_run(self):
        self.battle.process_battle()

        # Test that either the attacker or defender has 0 health after the battle
        self.assertTrue(self.attacker.health == 0 or self.defender.health == 0)

        # Test that the winner and loser attributes are correctly set
        self.assertIsNotNone(self.battle.winner)
        self.assertIsNotNone(self.battle.loser)
        self.assertNotEqual(self.battle.winner, self.battle.loser)

        print(self.battle.generate_battle_report())


if __name__ == '__main__':
    unittest.main()
