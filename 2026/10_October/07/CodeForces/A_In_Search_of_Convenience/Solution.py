# 3
# 0 0 1
# 5 5 5
# 10 10 13

def solution(x1,y1,R):
    # return (x1,y1,R)
    for x in range(x1 - R, x1 + R + 1):
        for y in range(y1 - R, y1 + R + 1):
            if (x - x1)**2 + (y - y1)**2 == R**2:
                print(x, y)
                break
        else:
            continue
        break
    

no_of_testcases = int(input())
for testcase in range(no_of_testcases):
    x=list(map(int,input().split()))
    print(solution(*x))

