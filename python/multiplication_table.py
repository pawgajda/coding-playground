#!/usr/bin/env python3


def print_multiplication_table(
    n: int = 10,
) -> None:
    for i in range(1, n + 1):
        print(f"\n-----{i}-----\n")
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")


if __name__ == "__main__":
    print_multiplication_table()
