import heapq

from app.models import Player

"""
The heapq module allows you to create and manipulate heap data structures. 
It provides functions for inserting, deleting, and accessing elements in the heap, as well as for merging and sorting heaps.
"""


class Leaderboard:
    def __init__(self):
        self.leaderboard = []

    def add_player(self, player):
        heapq.heappush(self.leaderboard, (-player.score, player.name))

    """
    By storing the scores as negative values, we effectively invert the priorities: a higher score 
    """

    def update_player_score(self, player: Player, new_score):
        if (-player.score, player.name) in self.leaderboard:
            self.leaderboard.remove((-player.score, player.name))
            heapq.heapify(self.leaderboard)

        player.score = new_score
        heapq.heappush(self.leaderboard, (-player.score, player.name))
        print("Updated player score:", player.id, player.score)

    """
    When returning the leaderboard data in the get_leaderboard method, we negate the scores again (with -score) 
    to convert them back to their original positive values. 
    """

    def get_leaderboard(self, num_entries=None):
        sorted_leaderboard = heapq.nsmallest(num_entries or len(self.leaderboard), self.leaderboard)
        return [
            {
                'rank': index + 1,
                'player_name': player_name,
                'score': -score
            } for index, (score, player_name) in enumerate(sorted_leaderboard)
        ]
