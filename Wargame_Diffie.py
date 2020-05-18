from math import ceil, sqrt, floor
import math


# n,m 互质
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


"""
def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for x in range(3, int(sqrt(n) + 1), 2):
            if n % x == 0:
                print(x)
                return False
        return True
    return False


print(isPrime(672804213107))
a = m / 13
print(a)
"""


# 计算pow(x,y,z) 相似快速幂
def pow_mod(x, y, z):
    p = 1
    while y:  # y > 0
        if y & 1:  # 位与 化成2进制后该位为1
            p = (p * x) % z
            # print(p)
        y = y >> 1  # 右移一位
        x = x * x % z
    return p


def bsgs(g, h, p):
    m = floor(sqrt(p - 1))

    hashtable = {(pow_mod(g, j, p) * h) % p: j for j in range(m + 1)} # h*g^j mod p
    print(hashtable.keys())

    gm = pow_mod(g, m, p)  # g^m mod p

    q = floor((p - 1) / m)
    for i in range(q + 1):
        k = pow_mod(gm, i, p)
        if k in hashtable:
            # print(j * t - hashtable[k])
            return i * m - hashtable[k]


m = pow_mod(5, 1, 14)
print(m)
a = bsgs(13, 5, 37)
print(a)
"""

b = bsgs(5, 354986528168, 672804213107)
print(b)
h = pow(5, b, 672804213107)
print(h)

shared = pow(320420178733, 29371762602, 672804213107)
print(shared)
"""
"""
shared_key = pow(A, b, p)
print(shared_key)
shared_keyTwo = pow(B, a, p)
print(shared_keyTwo)
"""
"""
g = 5
p = 672804213107
num = []
A = 354986528168
B = 320420178733
"""
