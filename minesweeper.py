import random
import sys

l = sys.argv

if len(l) != 4:
    print("USAGE: script.py Rows Columns Mines")
    sys.exit()
n = l[1]
m = l[2]
mines = l[3]
try:
    n = int(n)
    m = int(m)
    mines = int(mines)

except ValueError:
    print("Wrong input: Rows,Columns and Mines must be numbers")
    sys.exit()

if mines > n * m:
    print("Too many Mines")
    sys.exit()
board = []
for x in range(n * m):
    board.append(" ")

while board.count("*") < mines:
    i = random.choice(range(0, len(board)))
    if board[i] == " ":
        board[i] = "*"

for i in range(len(board)):
    count = 0
    if board[i] != "*":
        try:
            if i == 0:
                count += board[i + 1].count("*")
                count += board[i + n].count("*")
                count += board[i + n + 1].count("*")
            elif i == n * (m - 1):
                count += board[i - n].count("*")
                count += board[i - n + 1].count("*")
                count += board[i + 1].count("*")
            elif n * (m - 1) < i < n * m - 1:
                count += board[i - n - 1].count("*")
                count += board[i - n].count("*")
                count += board[i - n + 1].count("*")
                count += board[i - 1].count("*")
                count += board[i + 1].count("*")
            elif i == n - 1:
                count += board[i - 1].count("*")
                count += board[i + n].count("*")
                count += board[i + n - 1].count("*")
            elif 0 < i < n - 1:
                count += board[i + 1].count("*")
                count += board[i - 1].count("*")
                count += board[i + n - 1].count("*")
                count += board[i + n].count("*")
                count += board[i + n + 1].count("*")

            elif i == n * m - 1:
                count += board[i - n].count("*")
                count += board[i - n - 1].count("*")
                count += board[i - 1].count("*")

            elif i % n == 0:
                count += board[i + 1].count("*")
                count += board[i + n].count("*")
                count += board[i - n].count("*")
                count += board[i + n + 1].count("*")
                count += board[i - n + 1].count("*")
            elif i % n == (n - 1):
                count += board[i - 1].count("*")
                count += board[i + n].count("*")
                count += board[i - n].count("*")
                count += board[i + n - 1].count("*")
                count += board[i - n - 1].count("*")
            else:
                count += board[i + 1].count("*")
                count += board[i - 1].count("*")
                count += board[i + n].count("*")
                count += board[i - n].count("*")
                count += board[i + n - 1].count("*")
                count += board[i + n + 1].count("*")
                count += board[i - n + 1].count("*")
                count += board[i - n - 1].count("*")
        except IndexError:
            continue
        finally:
            board[i] = str(count)

for x in range(0, n * m, n):
    print(board[x:x + n])

filename = "minesweeper"
with open(filename + ".txt", "w") as file:
    for x in range(0, n * m, n):
        file.write('{}\n'.format(board[x:x + n]))
