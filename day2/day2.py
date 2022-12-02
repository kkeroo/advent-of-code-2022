import sys


def problem1(filename: str) -> None:
    f = open(filename)
    lines = f.readlines()
    f.close()

    beating_table = {'X': 'C', 'Y': 'A', 'Z': 'B'}  # ex. Rock X beats scissors C
    scoring_table = {'X': 1, 'Y': 2, 'Z': 3}  # Rock is worth 1 point
    coding_table = {'A': 'X', 'B': 'Y', 'C': 'Z'}  # A is rock and X is rock

    total_score = 0
    for line in lines:
        game = line.split(' ')
        game[-1] = game[-1][:-1] if game[-1][-1] == '\n' else game[-1]
        opponent = game[0]
        you = game[1]
        game_score = scoring_table[you]
        if coding_table[opponent] == you:  # draw
            game_score += 3
        else:
            if beating_table[you] == opponent:  # win
                game_score += 6
        total_score += game_score
    print(f'Total score: {total_score}')


def problem2(filename: str) -> None:
    f = open(filename)
    lines = f.readlines()
    f.close()

    beating_table = {'A': 'C', 'B': 'A', 'C': 'B'}
    scoring_table = {'A': 1, 'B': 2, 'C': 3}  # Rock is worth 1 point

    total_score = 0
    for line in lines:
        game = line.split(' ')
        game[-1] = game[-1][:-1] if game[-1][-1] == '\n' else game[-1]
        opponent = game[0]
        result = game[1]
        if result == 'X':  # lose
            play = beating_table[opponent]
            total_score += scoring_table[play]
        elif result == 'Y':  # draw
            total_score += scoring_table[opponent] + 3
        else:  # win
            play = [k for (k,v) in beating_table.items() if v == opponent][0]
            total_score += scoring_table[play] + 6

    print(f'Total score: {total_score}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Run the script as: day2.py <problem> <filename>')
        exit(0)
    try:
        problem = int(sys.argv[1])
        filename = sys.argv[2]
        if problem == 1:
            problem1(filename)
        elif problem == 2:
            problem2(filename)
    except:
        print('Run the script as: day2.py <problem> <filename>')
        exit(0)