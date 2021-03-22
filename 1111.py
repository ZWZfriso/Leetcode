def goroad(road: list, curp: list, direc: int):
    left, right = curp[0], curp[1]
    if direc == 2:
        while right >= 0:
            if road[left][right] == '#':
                break
            right -= 1
        return [left, right + 1]
    elif direc == 3:
        while right < len(road[0]):
            if road[left][right] == '#':
                break
            right += 1
        return [left, right - 1]
    elif direc == 0:
        while left >= 0:
            if road[left][right] == '#':
                break
            left -= 1
        return [left + 1, right]
    elif direc == 1:
        while left < len(road):
            if road[left][right] == '#':
                break
            left += 1
        return [left - 1, right]
def finddirec( direction: list, direc: str):
    for i in range(len(direction)):
        if direc == direction[i]:
            return i
    return -1
inputlist = list(map(int, input().split(' ')))
n, m, k = inputlist[0], inputlist[1], inputlist[2]
road, mark = [], []
for _ in range(n):
    temp = input()
    road.append(temp)
for _ in range(k):
    temp = input()
    mark.append(temp)
direction = ["NORTH", "SOUTH", "WEST", "EAST"]
curposition = [0, 0]
for i in range(n):
    for j in range(m):
        if road[i][j] == '@':
            curposition = [i, j]
            break
while len(mark) != 0:
    if mark[0] in direction:
        direc = finddirec(direction, mark[0])
        curposition = goroad(road, curposition, direc)
        mark = mark[1:]
print(curposition[0] + 1, curposition[1] + 1)
