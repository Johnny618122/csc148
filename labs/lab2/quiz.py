from typing import List, Dict

class Tournament:

    teams: List[str]
    team_stats: Dict[str, List[int]]

    def __init__(self, teams: List[str])->None:

        self.team_stats = {}
        self.teams = []
        for team_name in teams:
            self.teams.append(team_name)
            self.team_stats[team_name] = [0,0]

    def record_game(self, team1: str, team2: str, score1: int, score2: int):
        self.team_stats[team1][0] += 1
        self.team_stats[team2][0] += 1

        if score1 > score2:
            self.team_stats[team1][1] += 1
        else:
            self.team_stats[team2][1] += 1


