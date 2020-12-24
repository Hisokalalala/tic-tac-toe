import argparse
import sys

def turn(array: list, who: str, m: int, n: int) -> str:
    res = ""
    if who == "M" and array[m-1][n-1] == "?":
        array[m - 1][n - 1] = "○"
    elif who == "B" and array[m-1][n-1] == "?":
        array[m - 1][n - 1] = "×"
    else:
        raise ValueError("空いているマスにしか書き込みはできません、やり直してください")
    for i in range(len(array)):
        res += " ".join(array[i])
        res += "\n"
    return res


def tictactoe(now: str = "M") -> str:
    array = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]
    cnt = 0
    print("1 2のように座標を入力してください.")
    print("座標の分布としては以下のようになっております.")
    print("(1,1) (1,2) (1,3)\n(2,1) (2,2) (2,3)\n(3,1) (3,2) (3,3)\n")
    if now == "M":
        print("先攻は○の人です")
    else:
        print("先攻は×の人です")
    while cnt < 9:
        if (array[0] == ["○", "○", "○"] or array[1] == ["○", "○", "○"] or array[2] == ["○", "○", "○"] or
                (array[0][0] == "○" and array[1][0] == "○" and array[2][0] == "○") or (
                        array[0][1] == "○" and array[1][1] == "○" and array[2][1] == "○") or
                (array[0][2] == "○" and array[1][2] == "○" and array[2][2] == "○") or (
                        array[0][0] == "○" and array[1][1] == "○" and array[2][2] == "○") or
                (array[0][2] == "○" and array[1][1] == "○" and array[2][0] == "○")):
            return "result: ○ WIN!!"
        elif (array[0] == ["×", "×", "×"] or array[1] == ["×", "×", "×"] or array[2] == ["×", "×", "×"] or
              (array[0][0] == "×" and array[1][0] == "×" and array[2][0] == "×") or (
                      array[0][1] == "×" and array[1][1] == "×" and array[2][1] == "×") or
              (array[0][2] == "×" and array[1][2] == "×" and array[2][2] == "×") or (
                      array[0][0] == "×" and array[1][1] == "×" and array[2][2] == "×") or
              (array[0][2] == "×" and array[1][1] == "×" and array[2][0] == "×")):
            return "result: × WIN!!"
        else:
            if now == "M":
                print("今は○の人のターンです")
            else:
                print("今は×の人のターンです")
            try:
                x, y = (int(m) for m in input().split())
            except (ValueError, IndexError) as e:
                print("座標の入力形式が間違っています、入力し直してください")
                x, y = (int(m) for m in input().split())
            if now == "M":
                try:
                    situation = turn(array, "M", x, y)
                except ValueError as e:
                    print(e)
                    try:
                        x, y = (int(m) for m in input().split())
                    except (ValueError, IndexError) as e:
                        print("座標の入力形式が間違っています、入力し直してください")
                        x, y = (int(m) for m in input().split())
                    situation = turn(array, "M", x, y)
                print(situation)
                now = "B"
                cnt += 1
            else:
                try:
                    situation = turn(array, "B", x, y)
                except ValueError as e:
                    print(e)
                    try:
                        x, y = (int(m) for m in input().split())
                    except (ValueError, IndexError) as e:
                        print("座標の入力形式が間違っています、入力し直してください")
                        x, y = (int(m) for m in input().split())
                    situation = turn(array, "B", x, y)
                print(situation)
                now = "M"
                cnt += 1
    else:
        return "result: DRAW"

def main():
    parser = argparse.ArgumentParser(description='TicTacToe program.')
    parser.add_argument('--now', type=str, default="M",
                        help='先攻を決めます。○が先なら"M"を×が先なら"B"を引数として入れてください')
    args = parser.parse_args()

    print(tictactoe(now=args.now))
    print("GameEND")
