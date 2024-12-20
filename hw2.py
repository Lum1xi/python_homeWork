def calculate_sum_safe(numbers):
    try:
        for number in numbers:
            if number < 0:
                raise ValueError("Список містить від'ємне число!")
        return sum(numbers)
    except ValueError as e:
        return f"Помилка: {e}"

user_numbers = list(map(float, input("Введіть числа через пробіл: ").split()))
result = calculate_sum_safe(user_numbers)
print(result)
