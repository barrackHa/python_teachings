from math import pow

# for i in range(7):
i = 0
while  input():
    n = int(pow(2,i))
    mult = '*2' * i
    print(
        '{}) {} = {} -> {}'.format(
            i, '1' + mult ,n, bin(n)[2:]
        )
    )
    i += 1