import random
import uuid


class Player:
    def __init__(self, name: str):
        self.name = name
        self.id = str(uuid.uuid4())

        # initialise the player resources
        self.gold = 100
        self.attack = 100
        self.max_hit = random.randint(100, 200)
        self.health = 100
        self.luck = random.randint(10, 100)
        self.score = 0

    @classmethod
    def create(cls, name: str):
        if len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")
        elif len(name) > 20:
            raise ValueError("Name cannot be longer than 20 characters")

        # save to the database

        return cls(name)
