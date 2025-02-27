


def count_trailing_zeroes(n):
    count = 0
    power_of_5 = 5
    see = [];
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
        see.append(count)

    print(see)
    return count

# Calculate trailing zeroes in 100!
n = 200
print(f"Trailing zeroes in {n}!: {count_trailing_zeroes(n)}")
