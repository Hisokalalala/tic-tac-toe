# tic-tac-toe
三目並べのPythonパッケージ

# tictactoe

A [tictactoe](https://ja.wikipedia.org/wiki/%E4%B8%89%E7%9B%AE%E4%B8%A6%E3%81%B9) program available as Python package.

## How to install

```sh
$ make install
```

## Usage as Python package

`tictactoe` function can play a game with two players.

```py
>>> from tictactoe.tictactoe import tictactoe
>>> tictactoe()
1 2のように座標を入力してください.
座標の分布としては以下のようになっております.
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)

先攻は○の人です
今は○の人のターンです
1 2(input by first player)
? ○ ?
? ? ?
? ? ?

今は×の人のターンです
1 1(input by second player)
× ○ ?
? ? ?
? ? ?

今は○の人のターンです

...

× ○ ×
? ○ ?
? ? ?

今は○の人のターンです
3 2
× ○ ×
? ○ ?
? ○ ?

'result: ○ WIN!!'
```

## LICENSE
MIT License
