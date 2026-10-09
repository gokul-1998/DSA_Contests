def solution(x1,y1,R):
    # return (x1,y1,R)
    # 0,5
    for x in range(x1 - R, x1 + R + 1): # 0....10
        for y in range(y1 - R, y1 + R + 1): # 0...10
            # if (x - x1)**2 + (y - y1)**2 == R**2: # 25+25 ==25
            #     print(x, y)
                # break
            pass
        else:
            print(x,y)
            continue
        break

solution(5,5,5)