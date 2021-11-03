# Time : O(n) where n is the number of matches
# Space : O(k) where k are all the winning team
def tournamentWinner(competitions, results):
    winner = {}
    idx = 0
    while idx < len(results):
        homeTeam = competitions[idx][0]
        awayTeam = competitions[idx][1]
        if results[idx] == 0:
            winningTeam = awayTeam
        else:
            winningTeam = homeTeam

        if winningTeam not in winner:
            winner[winningTeam] = 1
        else:
            winner[winningTeam] += 1

        idx += 1

    maxPoint = 0
    for k, v in winner.items():
        if v > maxPoint:
            tournamentWinner = k
            maxPoint = v
    return tournamentWinner

competitions = [
  ["HTML", "Java"],
  ["Java", "Python"],
  ["Python", "HTML"]
]

results = [0, 1, 1]

print(tournamentWinner(competitions, results))