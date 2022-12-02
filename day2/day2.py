import sys


def main(filename: str) -> None:
    f = open(filename)
    lines = f.readlines()

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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Run the script as: day2.py <filename>')
        exit(0)
    filename = sys.argv[1]
    main(filename)