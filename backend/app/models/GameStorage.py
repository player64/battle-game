class GameStorage:
    _players = {}
    battle_reports = []

    def add_player(self, player):
        self._players[player.id] = player

    @property
    def active_players(self) -> list:
        return [player for player in self._players.values() if player.health > 0]

    @property
    def dead_players(self) -> list:
        return [player for player in self._players.values() if player.health == 0]

    def add_report(self, report: dict):
        self.battle_reports.append(report)

    def get_reports(self):
        return self.battle_reports

    def get_last_report(self) -> list:
        if not self.battle_reports:
            return []
        return self.battle_reports[-1]

    def get_player_by_id(self, player_id: str):
        return self._players.get(player_id, None)
