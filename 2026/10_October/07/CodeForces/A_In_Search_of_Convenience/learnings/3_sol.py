def solution(x1,y1,R):
    # return (x1,y1,R)
    for x in range(x1 - R, x1 + R + 1): # 0....10
        for y in range(y1 - R, y1 + R + 1): # 0...10
            if (x - x1)**2 + (y - y1)**2 == R**2: #  25 + 0 == 25
                print(x, y)
                break
        else:
            continue
        break

solution(5,5,5)
# solution(2,1,5)
# solution(0,0,1)
# solution(10,10,13)