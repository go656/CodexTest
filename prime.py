"""整数が素数かどうかを判定するプログラム。"""

from math import isqrt


def is_prime(number: int) -> bool:
    """2 以上で、1 と自分自身以外に約数がない場合に True を返す。"""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def main() -> int:
    try:
        number = int(input("整数を入力してください: "))
    except (ValueError, EOFError):
        print("エラー: 整数を入力してください。")
        return 1

    if is_prime(number):
        print(f"{number} は素数です。")
    else:
        print(f"{number} は素数ではありません。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
