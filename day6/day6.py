import sys


def main(filename: str, problem:int = 1) -> None:
    f = open(filename)
    message = f.readlines()[0]
    f.close()

    c = 0
    offset = 4 if problem == 1 else 14
    while c < len(message)-offset:
        window = message[c:c+offset]
        uniq = True
        for i,el in enumerate(window):
            for j,ell in enumerate(window):
                if j==i:
                    continue
                if el == ell:
                    uniq = False
        if uniq:
            print(c+offset)
            return
        c = c+1
        
        

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Use correct format')
        exit(0)
    filename = sys.argv[1]
    problem = int(sys.argv[2])
    main(filename, problem)