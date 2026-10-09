numbers = [1, 2, 3, 4, 5]

# Capture the head and tail, and grab everything else in the middle
first, *middle, last = numbers

print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4] (always returns a list)
print(last)  