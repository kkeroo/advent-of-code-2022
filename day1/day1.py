import sys


def main(filename: str, n: int = 1) -> None:
    f = open(filename)
    lines = f.readlines()
    f.close()

    numbers = ['1','2','3','4','5','6','7','8','9']
    elfs = []
    starting_ix = 0
    for i, line in enumerate(lines):
        if line[0] not in numbers:
            elfs.append(lines[starting_ix:i])
            starting_ix = i+1

    total_calories = []
    for elf in elfs:
        elf = [int(x[:-1]) for x in elf]
        total_calories.append(sum(elf))

    total_calories.sort(reverse=True)
    total = sum(total_calories[:n])
    print(f'Total calories: {total}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use only one argument.")
        exit(0)
    filename = sys.argv[1]
    main(filename, 3)