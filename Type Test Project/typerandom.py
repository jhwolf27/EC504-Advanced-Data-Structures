import time
start = time.time()
L=0
while time.time() < start + 10:
    with open('typerandom.txt') as f:
        for line in f:
            print(line)
            s = input('--> ')
            print(s)
            if line == s:
                L = L + 1
                print(L)
            else:
                print('nope')
