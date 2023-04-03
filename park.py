#  성공
def solution(park, routes):
    answer = []
    X = [-1, +1, 0, 0]
    Y = [0, 0, -1, +1]
    changX, changY = 0, 0
    num = 0
    all_clear = True

    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == "S":
                answer = [x, y]
                break

    for rout in routes:
        op, n = rout.split()
        n = int(n)

        if op == "N":
            num = 0
        elif op == "S":
            num = 1
        elif op == "W":
            num = 2
        else:
            num = 3

        changX = answer[0]
        changY = answer[1]
        all_clear = True
        for _ in range(n):
            changX += X[num]
            changY += Y[num]
            if 0 <= changX < len(park) and 0 <= changY < len(park[0]):
                if park[changX][changY] == "X":
                    all_clear = False
                    break
            else:
                all_clear = False
                break

        if all_clear == True:
            answer[0] = changX
            answer[1] = changY

    return answer


park = ["OSO", "OOO", "OXO", "OOO"]
routes = ["E 2", "S 3", "W 1"]
print(solution(park, routes))
