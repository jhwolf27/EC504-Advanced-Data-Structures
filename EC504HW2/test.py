import math



def R1(n):
    if (n == 0):
        return 1
    else:
        return R1(n-1) * R1(n-1) * R1(n-1)

def R2(n):
    if (n == 0):
        return 1
    if (R2(n//2) >= 5):
        return R2(n//2) + 5
    else:
        return 5

def R3(n):
    if (n <= 1):
        return 1
    sum=0
    for ii in range(int(math.sqrt(n))):
        sum += R3(int(math.sqrt(n)))
    return sum

def R4(n):
    if (n <= 1):
        return 1
    count = 1
    tmp = R4(n//2)
    for jj in range(n):
        ii=1;
        while (ii<n):
            if (tmp < math.exp(ii+jj)):
                count += 1
            ii*=2
    return R4(n//2) * (count % 2)

def R5(n):
    if (n == 0): return 1
    if (n == 1): return 3
    return R5(n-1) + R5(n-2)*R5(n-2)


