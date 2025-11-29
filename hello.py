# 1から100までの和を求める
total = sum(range(1, 101))
print(f"1から100までの和: {total}")

# 1から100までの和を、順次途中結果を表示しながら求める
total = 0
for i in range(1, 101):
    total += i
    print(f"1から{i}までの和: {total}") 
print(f"最終的な和: {total}")
