def turn(array, who, m, n):
    res = ""
    if who == "M":
        array[m-1][n-1] = "○"
    else:
        array[m-1][n-1] = "×"
    for i in range(len(array)):
        res += " ".join(array[i])
        res += "\n"
    return res

def TicTacToe(m,n):
    return "Win"