# print all the perfect square roots between 1 to 25.

def is_perfect_square(number):
    # return True if the number is a perfect square else False
    sqrt=number**(0.5)
    if sqrt*sqrt == number:
        return True
    else:
        return False




is_perfect_square(25)

assert is_perfect_square(25)==True
assert is_perfect_square(26)==False
print("all cases passed")
