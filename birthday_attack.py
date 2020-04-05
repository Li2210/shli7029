from time import time
import random

from Crypto.Hash import SHA256

# Try to find hash collisions for increasingly lengthier hashes
# prove birthday attack(2**(n/2)) is much faster than brute force(2**(n-1)).

M1, M2 = {}, {}
while True:
    m1 = "Melbourne Cup: $8,000 on Horse 'Twilight Payment' [transaction id: {%d}]" % random.randint(0, 10000000000)
    m1 = m1.encode("ascii")
    hash_m1 = SHA256.new(m1).hexdigest()[:8]
    m2 = "Melbourne Cup: $8,000 on Horse 'Steel Prince' [transaction id: {%d}]" % random.randint(0, 10000000000)
    m2 = m2.encode("ascii")
    hash_m2 = SHA256.new(m2).hexdigest()[:8]
    if hash_m1 in M2:
        print("find a collision in %d-hex" % 8)
        print('m1 is: "%s"' % m1)
        print('h1 is: "%s"' % hash_m1)
        print(M2[hash_m1])
        break
    elif hash_m2 in M1:
        print('m2 is: "%s"' % m2)
        print('h2 is: "%s"' % hash_m2)
        print(M1[hash_m2])
        break
    else:
        M1[hash_m1] = m1
        M2[hash_m2] = m2
