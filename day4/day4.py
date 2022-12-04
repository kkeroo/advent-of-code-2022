import sys


def problem1(filename: str) -> None:
    f = open(filename)
    lines = f.readlines()
    f.close()
    pairs = []
    for line in lines:
        pair = line.split(',')
        first = pair[0].split('-')[0]
        second = pair[0].split('-')[1]
        p = [{'start': int(first), 'stop': int(second)}]
        first = pair[1].split('-')[0]
        second = pair[1].split('-')[1]
        p.append({'start': int(first), 'stop': int(second)})
        pairs.append(p)
    
    content = 0
    for pair in pairs:
        s1 = pair[0]['start']
        e1 = pair[0]['stop']
        s2 = pair[1]['start']
        e2 = pair[1]['stop']
        if (s1 <= s2 and e1 >= e2) or (s1 >= s2 and e1 <= e2):
            content += 1
    print(f'Fully contains:{content}') 


def problem2(filename: str) -> None:
    f = open(filename)
    lines = f.readlines()
    f.close()
    pairs = []
    for line in lines:
        pair = line.split(',')
        first = pair[0].split('-')[0]
        second = pair[0].split('-')[1]
        p = [{'start': int(first), 'stop': int(second)}]
        first = pair[1].split('-')[0]
        second = pair[1].split('-')[1]
        p.append({'start': int(first), 'stop': int(second)})
        pairs.append(p)

    overlaps = 0
    for pair in pairs:
        s1 = pair[0]['start']
        e1 = pair[0]['stop']
        s2 = pair[1]['start']
        e2 = pair[1]['stop']
        if (s1 >= s2 and s1 <= e2) or (e1 >= s2 and e1 <= e2) or (s1 <= s2 and e1 >= s2) or (e2 >= s1 and e2 <= e1):
            overlaps += 1
    print(f'Overlaps: {overlaps}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Use correct call.')
        exit(0)
    filename = sys.argv[1]
    problem2(filename=filename)
