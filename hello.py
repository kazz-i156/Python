def sum_1_to_100():
    """1から100までの和を返す。"""
    return sum(range(1, 101))


if __name__ == "__main__":
    total = sum_1_to_100()
    print(f"1から100までの和: {total}")
