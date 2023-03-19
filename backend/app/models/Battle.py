import random

from app.models import Player, GameStorage


class Battle:
    def __init__(self, attacker: Player, defender: Player):
        self.attacker = attacker
        self.defender = defender
        self.turns = []
        self.loser = None
        self.winner = None

    def process_battle(self):
        while self.attacker.health > 0 and self.defender.health > 0:
            self.turn()
        self.winner = self.attacker if self.attacker.health > 0 else self.defender
        self.loser = self.defender if self.winner == self.attacker else self.attacker

    def turn(self):
        attack_damage = self.calculate_attack_damage(self.attacker)
        attack_missed = self.attack_missed(self.defender)

        if not attack_missed:
            self.defender.health -= attack_damage
            if self.defender.health < 0:
                self.defender.health = 0

        self.turns.append({
            'attacker': self.attacker.name,
            'defender': self.defender.name,
            'damages': attack_damage,
            'attack_missed': attack_missed,
            'attacker_health': self.attacker.health,
            'defender_health': self.defender.health
        })

        # swap players
        self.attacker, self.defender = self.defender, self.attacker

    def attack_missed(self, player: Player) -> bool:
        return random.randint(0, 200) < player.luck

    def calculate_attack_damage(self, player: Player):
        # damage_reduction calculates the damage based on the attacker's health and max hit.
        # This value is between 0 and 1. When the attacker's health is at its maximum, the damage reduction is 0.
        # When the attacker's health is 0, the damage reduction is 1.

        damage_reduction = 1 - (player.health / player.max_hit)

        # reduced_attack Calculates the actual attack value by multiplying the attacker's base attack value
        # by the inverse of the damage reduction. However, it caps the reduction at 50% of the base attack
        reduced_attack = player.attack * max(0.5, 1 - damage_reduction)
        return round(reduced_attack)

    def generate_battle_report(self):
        return {
            'winner': self.winner.name,
            'loser': self.loser.name,
            'turns': self.turns
        }
