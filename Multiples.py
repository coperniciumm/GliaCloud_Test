mul_3_or_5 = [mul_three for mul_three in range(1, 1000) if mul_three % 3 == 0 or mul_three % 5 == 0]
print(sum(mul_3_or_5))
