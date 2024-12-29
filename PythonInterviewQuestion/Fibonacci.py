def generate_fibonacci_sequence(num: int) -> list:
    fibonacci_list = []
    sum, start, mid = 0, 0, 1
    for _ in range(num):
        fibonacci_list.append(start)
        sum = start + mid
        start = mid
        mid = sum
    return fibonacci_list


num = 5
fibonacci_list = generate_fibonacci_sequence(num)
print(fibonacci_list)
