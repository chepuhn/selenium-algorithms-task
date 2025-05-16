user_input = input("Введите числа через запятую: ")
numbers = [int(x.strip()) for x in user_input.split(",")]
even_numbers = [num for num in numbers if num % 2 == 0]
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:

    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
sorted_numbers = numbers[:]
for i in range(len(sorted_numbers)):
    for j in range(i + 1, len(sorted_numbers)):
        if sorted_numbers[i] > sorted_numbers[j]:
            sorted_numbers[i], sorted_numbers[j] = sorted_numbers[j], sorted_numbers[i]

print("Четные числа:", even_numbers)
print("Максимальное число:", maximum)
print("Минимальное число:", minimum)
print("Отсортированный список:", sorted_numbers)
