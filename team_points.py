def points_by_team(scores, teams):
    result = {}
    for team in teams:
        total = 0
        for player in teams[team]:
            total += scores[player]
        result[team] = total
    return result


def main():
    scores = {}
    teams = {}

    with open("players.txt") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 0:
                continue
            name = parts[0]
            points = int(parts[1])
            team = parts[2]
            scores[name] = points
            if team not in teams:
                teams[team] = []
            teams[team].append(name)

    print("Scores:", scores)
    print("Teams:", teams)
    print("Points by team:", points_by_team(scores, teams))


main()
