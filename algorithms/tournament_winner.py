class TournamentWinner:

    def __init__(self, competitions, results):
        self.competitions = competitions
        self.results = results

    # Time : O(n) where 'n' is the number of competitions
    # Space : O(k) where 'k' is the number of teams
    def solution1(self):
        winner_map = {}
        for competition, result in zip(self.competitions, self.results):
            if result == 1:
                winner = competition[0]
            else:
                winner = competition[1]
            
            if winner not in winner_map:
                winner_map[winner] = 1
            else:
                winner_map[winner] += 1
        
        max_score = 0
        for team, score in winner_map.items():
            if score > max_score:
                max_score = score
                winner = team
        
        return winner

# Testing the code -

competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

results = [0, 0, 1]

obj = TournamentWinner(competitions, results)
print(obj.solution1())
