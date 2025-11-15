#!/usr/bin/env python3


def generate_num_table(
    num: int,
    stop: int = 10,
) -> list[int]:
    table = []
    for i in range(1, stop + 1):
        table.append(f"{num} * {i} = {num * i}")
    return table


def multiplication_table(
    n: int = 10,
) -> dict[list[int]]:
    table = {}
    for i in range(1, n + 1):
        num_table = generate_num_table(i)
        table[i] = num_table
    return table


def print_table(
    table: dict[list[int]],
) -> None:
    for num, num_table in table.items():
        print(f"\n-----{num}-----\n")
        for row in num_table:
            print(row)


if __name__ == "__main__":
    table = multiplication_table()
    print_table(table)
