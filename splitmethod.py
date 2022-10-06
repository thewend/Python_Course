word = "Asas dae qwe qwe trg fdyt"
print(word.split())

numbers = "9,54,954,567456,768679786,23"
numbers_split = numbers.split(",")
print(numbers_split)

print("".join(numbers_split))

print("".join(numbers.split(",")))

numbers_119 = "9,223,372,036,854,775,807"
numbers_119 = numbers_119.split(",")
print(numbers_119)

for i in range(len(numbers_119)):
    numbers_119[i] = int(numbers_119[i])
print(numbers_119)