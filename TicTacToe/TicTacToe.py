def turn(array: list, who: str, m: int, n: int) -> str:
    res = ""
    if who == "M":
        array[m - 1][n - 1] = "○"
    else:
        array[m - 1][n - 1] = "×"
    for i in range(len(array)):
        res += " ".join(array[i])
        res += "\n"
    return res


def tictactoe() -> str:
    array = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]
    cnt = 0
    now = "M"
    print("1 2のように座標を入力してください左上の座標は1 1です。右下に行くにつれて数字が増えます")
    print("先攻は○の人です")
    while cnt < 9:
        if (array[0] == ["○", "○", "○"] or array[1] == ["○", "○", "○"] or array[2] == ["○", "○", "○"] or
                (array[0][0] == "○" and array[1][0] == "○" and array[2][0] == "○") or (
                        array[0][1] == "○" and array[1][1] == "○" and array[2][1] == "○") or
                (array[0][2] == "○" and array[1][2] == "○" and array[2][2] == "○") or (
                        array[0][0] == "○" and array[1][1] == "○" and array[2][2] == "○") or
                (array[0][2] == "○" and array[1][1] == "○" and array[2][0] == "○")):
            return "result: Maru WIN!!"
        elif (array[0] == ["×", "×", "×"] or array[1] == ["×", "×", "×"] or array[2] == ["×", "×", "×"] or
              (array[0][0] == "×" and array[1][0] == "×" and array[2][0] == "×") or (
                      array[0][1] == "×" and array[1][1] == "×" and array[2][1] == "×") or
              (array[0][2] == "×" and array[1][2] == "×" and array[2][2] == "×") or (
                      array[0][0] == "×" and array[1][1] == "×" and array[2][2] == "×") or
              (array[0][2] == "×" and array[1][1] == "×" and array[2][0] == "×")):
            return "result: Batsu WIN!!"
        else:
            x, y = (int(m) for m in input().split())
            if now == "M":
                situation = turn(array, "M", x, y)
                print(situation)
                now = "B"
                cnt += 1
                if cnt < 9:
                    print("次は×の人のターンです")

            else:
                situation = turn(array, "B", x, y)
                print(situation)
                now = "M"
                cnt += 1
                if cnt < 9:
                    print("次は○の人のターンです")

    else:
        return "result: DRAW"

a = tictactoe()
print(a)
print("GameEnd")
