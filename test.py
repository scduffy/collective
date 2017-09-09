def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False

    return True

total = 0

for g in range(0, 2_000_000):
    if is_prime(g):
        total = total + g
        #print(g)

print("\n")
print(total)
