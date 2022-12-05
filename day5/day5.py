import sys


def main(filename: str, problem:int = 1) -> None:
    f = open(filename)
    actions = f.readlines()
    f.close()

    stacks = [
        ['W','P','G','Z','V','S','B'],
        ['F','Z','C','B','V','J'],
        ['C','D','Z','N','H','M','L','V'],
        ['B','J','F','P','Z','M','D','L'],
        ['H','Q','B','J','G','C','F','V'],
        ['B','L','S','T','Q','F','G'],
        ['V','Z','C','G','L'],
        ['G','L','N'],
        ['C','H','F','J']
    ]
    stacks = [stack[::-1] for stack in stacks]

    for action in actions:
        quatity = int(action.split(' ')[1])
        from_ix = int(action.split(' ')[3]) - 1
        to_ix = int(action.split(' ')[5]) - 1
        
        if problem == 1:
            for i in range(quatity):
                el = stacks[from_ix].pop()
                stacks[to_ix].append(el)
        else:
            grabbed_els = []
            for i in range(quatity):
                el = stacks[from_ix].pop()
                grabbed_els.append(el)
            stacks[to_ix] += grabbed_els[::-1]

    last_items = [stack[-1] for stack in stacks]
    print(last_items)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Use correct format')
        exit(0)
    filename = sys.argv[1]
    problem = int(sys.argv[2])
    main(filename, problem)