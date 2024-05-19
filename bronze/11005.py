def cha(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base

    return result

n, b = map(int, input().split())


converted_number = cha(n, b)

# 결과 출력
print(converted_number)
