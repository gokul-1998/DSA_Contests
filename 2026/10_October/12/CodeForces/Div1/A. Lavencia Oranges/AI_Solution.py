
def capacity(k): # 5
    total = 0

    for s in range(1, k + 1): # 1,2,3,4,5
        total += s * (k // s) # (1*5)+(2*2)+(3*1)+(4*1)+(5*1)

    return total


def solve(n):
    # Find the minimum possible cost using binary search
    low, high = 1, n

    while low < high:
        mid = (low + high) // 2

        if capacity(mid) >= n:
            high = mid
        else:
            low = mid + 1

    cost = low

    # Construct the bag sizes
    sizes = []
    remaining = n

    for s in range(cost, 0, -1):
        count = min(cost // s, remaining // s)

        sizes.extend([s] * count)
        remaining -= s * count

    # Convert bag sizes into the required array a
    a = []

    for bag_id, size in enumerate(sizes, start=1):
        a.extend([bag_id] * size)

    print(cost)
    print(*a)


t = int(input())

for _ in range(t):
    n = int(input())
    solve(n)
