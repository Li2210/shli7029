from time import time
import random

from Crypto.Hash import SHA256

# 以 SHA256 为例子 证明 hash function 很难找到碰撞

# Set up the initial key, message and modified message (m_dash)
# k = "evilgenius"
m = "Melbourne Cup: $8,000 on Horse 'Twilight Payment' [transaction id: {%d}]" % random.randint(100, 1000)
m = m.encode("ascii")
m_dash = "Melbourne Cup: $8,000 on Horse 'Steel Prince' [transaction id: {%d}]"

print("Finding collisions against %s" % m)

# Try to find hash collisions for increasingly lengthier hashes
for shortened_to in range(3, 10):
    # Calculate the hash up to N hex characters which we want to match against
    original_hash = SHA256.new(m).hexdigest()[:shortened_to]
    # Each hex character represents 4 bits as 0-9A-F = 16 = 2 ** 4 / one byte equal to 4 bits
    print("Attempting to match simplified %d-hex char hash (%d bits): %s" % (
        shortened_to, shortened_to * 4, original_hash))

    start_time = time()
    nonce = 0
    while True:
        # This nonce is the value we use to modify the message such that it will have a different hash each time
        nonce += 1
        updated_text = m_dash % nonce
        updated_text = updated_text.encode("ascii")
        h = SHA256.new(updated_text)
        impersonator_hash = h.hexdigest()[:shortened_to]
        # If the 'impersonator hash' collides with the original hash, we found our collision
        if original_hash == impersonator_hash:
            break
        # Else, loop around and try another variation

    end_time = time()
    print('End message: "%s"' % (m_dash % nonce))
    print("total over %0.2f seconds" % (end_time - start_time))
    print("%d attempts to find a collision were expected (2**(n-1)) [assuming no hash duplicates]" % 2 ** (
            (shortened_to * 4) - 1))
    print()
