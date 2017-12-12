def battle(left, right):
    left_counter = 0
    right_counter = 0
    for l in left:
        print(left, right)
        m = 10
        for r in right:
            if r < m and r >= l:
                m = l
        if m < 10:
            right.remove(m)
            right_counter = right_counter + 1
        else:
            left_counter = left_counter + 1

    return counter


input = open('input.txt', 'r')
output = open('output.txt', 'w')
length = int(input.readline().strip())
left = [*map(int, input.readline().strip())]
right = [*map(int, input.readline().strip())]

c = battle(left, right)

print(c)
