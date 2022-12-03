import sys


def problem1(filename: str) -> None:
    f = open(filename)
    lines = f.readlines()
    total_score = 0
    score_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'y': 24,
        'x': 25,
        'z': 26
    }
    for line in lines:
        middle = int(len(line)/2)
        first_half = line[:middle]
        second_half = line[middle:]
        already_matched = []
        for letter in first_half:
            for second_letter in second_half:
                if letter == second_letter and letter not in already_matched:
                    already_matched.append(letter)
                    if letter not in score_dict.keys():
                        total_score += score_dict[letter.lower()] + 26
                    else:
                        total_score += score_dict[letter]

    print(f'Total score: {total_score}.')


def problem2(filename: str) -> None:
    f = open(filename)
    lines = f.readlines()
    total_score = 0
    score_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'y': 24,
        'x': 25,
        'z': 26
    }
    current_group = 0
    while current_group < len(lines):
        first = lines[current_group]
        second = lines[current_group+1]
        fs = []
        for f in first:
            for s in second:
                if f == s:
                    fs.append(f)
        third = lines[current_group+2]
        for f in fs:
            if f in third:
                if f not in score_dict.keys():
                    total_score += score_dict[f.lower()] + 26
                else:
                    total_score += score_dict[f]
                break
        current_group += 3
    print(f'Total score: {total_score}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please use the script as: day3.py <filename>")
        exit(0)
    filename = sys.argv[1]
    problem2(filename)