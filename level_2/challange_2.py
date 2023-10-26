def solution(n, b):
    k = len(n)

    x = sorted(list(n))
    y = sorted(list(n), reverse=True)

    x, y = int(''.join(map(str, x))), int(''.join(map(str, y)))
    z = str(to_base(int(to_decimal(y, b)) - int(to_decimal(x, b)), b))

    last_zs = [] 

    if len(z) < k:
        for i in range(k-len(z)):
            z = "0"+z

    while True:
        x = sorted(list(z))
        y = sorted(list(z), reverse=True)

        x, y = int(''.join(map(str, x))), int(''.join(map(str, y)))
        z = str(to_base(int(to_decimal(y, b)) - int(to_decimal(x, b)), b))

        if len(z) < k:
            for i in range(k-len(z)):
                z = "0"+z

        last_zs.append(z)
        counter = 0 
        for i in range(len(last_zs)):
            if z == last_zs[i] and len(last_zs) != 1:
                for j in range(last_zs.index(z)+1, len(last_zs)):
                    counter += 1
                    if z == last_zs[j]:
                        return counter


def to_base(n, b):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return ''.join(reversed(nums))

def to_decimal(n, b):
    if (n != 0):
        decimal_number = 0
        i = 0
        remainder = 0

        while (n != 0):
            remainder = n % 10
            n = n // 10
 
            decimal_number += remainder * (b**i)
            i += 1
    
        return decimal_number

    else:
        return 0