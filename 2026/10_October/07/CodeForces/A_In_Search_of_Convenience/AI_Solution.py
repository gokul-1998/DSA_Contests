# https://chatgpt.com/share/6ac8f943-0fb4-83ee-856f-4f3fbbd3d373

t = int(input())

for _ in range(t):
    x0, y0, R = map(int, input().split())

    for x in range(x0 - R, x0 + R + 1):
        for y in range(y0 - R, y0 + R + 1):
            if (x - x0)**2 + (y - y0)**2 == R**2:
                print(x, y)
                break
        else:
            continue
        break