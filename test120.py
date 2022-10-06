user_input = str(input("Please enter three numbers: "))
user_input_list = user_input.split(",")

for i in range(len(user_input_list)):
    user_input_list[i] = int(user_input_list[i])

print(user_input_list[0] + user_input_list[1] - user_input_list[2])