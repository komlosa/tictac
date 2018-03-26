board = []
win_commbinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

for x in range(0, 9):
    board.append(str(x + 1))


def draw():
    print(board[0], "|", board[1], "|", board[2])
    print("--|---|--")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|--")
    print(board[6], "|", board[7], "|", board[8])


def win():
    for x in range(0, 8):
        a = board[win_commbinations[x][0]]
        b = board[win_commbinations[x][1]]
        c = board[win_commbinations[x][2]]
        if a == b and a == c:
            print("win:", a)
            return True
    return False


step = 0
test = False
while not test and step < 9:
    nextchar = "O"
    if step % 2 ! = 0:
        nextchar = "X"
    try:
        move = int(input("Where do you want to put the next " + nextchar + "? 1-9: "))
    except ValueError:
        print("Invalid input")
        continue
    if move < 1 or move > 9:
        print("ValueError")
        continue
    if board[move-1] == "X" or board[move-1] == "O":
        print("This place is taken.")
        continue

    board[move-1] = nextchar
    step = step + 1
    draw()
    test = win()
print("The game ended")
