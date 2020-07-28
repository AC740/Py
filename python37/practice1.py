
array = [1,2,5,12,7,13]
numbers = {x:0 for x in array}

print(numbers)

left = right = 0

for number in array:
    if numbers[number] == 0:
        left_count = number - 1
        right_count = number + 1
        while left_count in numbers:
            numbers[left_count] = 1
            left_count -= 1
        left_count + 1