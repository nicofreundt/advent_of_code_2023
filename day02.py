import re

FILE = "input.txt"
POSSIBLE = {
    'red': 12,
    'green': 13,
    'blue': 14
}

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        games = [[[color[1:] for color in re.findall('((\d+) (blue|red|green))', round)] for round in game.split(';')] for game in file.readlines()]
        possible_games = []
        for i, game in enumerate(games):
            cur_game_possible = True
            for round in game:
                cur_round = {
                    'red': 0,
                    'green': 0,
                    'blue': 0
                }
                for color in round:
                    cur_round[color[1]] += int(color[0])
                if not all(POSSIBLE[k] >= v for k,v in cur_round.items()):
                    cur_game_possible = False
            if cur_game_possible:
                possible_games.append(i + 1)
        print(sum(possible_games))

    # part two 
    with open(FILE) as file:
        games = [[[color[1:] for color in re.findall('((\d+) (blue|red|green))', round)] for round in game.split(';')] for game in file.readlines()]
        games_power = []
        for i, game in enumerate(games):
            cur_game = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            for round in game:
                cur_round = {
                    'red': 0,
                    'green': 0,
                    'blue': 0
                }
                for color in round:
                    cur_round[color[1]] += int(color[0])
                for k,v in cur_round.items():
                    if cur_game[k] < v:
                        cur_game[k] = v
            games_power.append(cur_game['red'] * cur_game['green'] * cur_game['blue'])
        print(sum(games_power))
