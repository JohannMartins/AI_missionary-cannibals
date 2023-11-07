#M #missionaries in left
#C #cannibals in left
# B=1left
# B=0right
def is_valid(state):
    if state[0] > 3 or state[1] > 3 or state[2] > 1 or state[0] < 0 or state[1] < 0 or state[2] < 0 or (0 < state[0] < state[1]) or (0 < (3 - state[0]) < (3 - state[1])):
        return False
    else:
        return True

def generate_next_states(M, C, B):
    moves = [[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1], [1, 1, 1]]
    valid_states = []
    for each in moves:
        if B == 1:
            next_state = [x1 - x2 for (x1, x2) in zip([M, C, B], each)]
        else:
            next_state = [x1 + x2 for (x1, x2) in zip([M, C, B], each)]
        if is_valid(next_state):
            valid_states.append(next_state)
    return valid_states

solutions = []

def find_sol(M, C, B, visited):
    if [M, C, B] == [0, 0, 0]:  # everyone crossed successfully
        solutions.append(visited + [[0, 0, 0]])
        return True
    elif [M, C, B] in visited:  # prevent looping
        return False
    else:
        visited.append([M, C, B])
        if B == 1:  # boat is in left
            for each_s in generate_next_states(M, C, B):
                find_sol(each_s[0], each_s[1], each_s[2], visited[:])
        else:  # boat in in right
            for each_s in generate_next_states(M, C, B):
                find_sol(each_s[0], each_s[1], each_s[2], visited[:])

# user input
M = int(input("Enter the number of missionaries in the left: "))
C = int(input("Enter the number of cannibals in the left: "))
B = int(input("Enter the boat position (1 for left, 0 for right): "))

find_sol(M, C, B, [])

solutions.sort()
count_rows = len(solutions)
print("THE MISSIONARIES AND CANNIBALS PROBLEM SOLVED USING THE DFS ALGORITHM :")
for i in range(count_rows):
    print()
    print("SOLUTION: " + str(i + 1))
    print("                 " + "Left Side" + "                      " + "Right Side" + "                   " + "Boat ")
    print("          Cannibals" + "     Missionaries" + "       " + "Cannibals" + "       Missionaries" + "    Boat Position")
    count_columns = len(solutions[i])
    for j in range(count_columns):
        if solutions[i][j][2] == 0:
            direction = "right"
        else:
            direction = "left"
        if j <= 9:
            print("State " + str(j) + "    Left M: " + str(solutions[i][j][0]) + ".    Left C: " + str(
                solutions[i][j][1]) + ".     |   Right M: " + str(
                abs(solutions[i][j][0] - 3)) + ".     Right C: " + str(abs(solutions[i][j][1] - 3)) + ".     | Boat: " + str(
                direction))
        else:
            print("State " + str(j) + "   Left M: " + str(solutions[i][j][0]) + ".    Left C: " + str(
                solutions[i][j][1]) + ".     |   Right M: " + str(
                abs(solutions[i][j][0] - 3)) + ".     Right C: " + str(abs(solutions[i][j][1] - 3)) + ".     | Boat: " + str(
                direction))
