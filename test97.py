list_computer_parts = [
    "Monitor",
    "Keyboard",
    "Mouse",
    "HDMI Cable",
    "Celular",
    "Gatorade"
]

def print_parts(list_computer_parts):
    print("Please add options from the list below:")
    for number , part in enumerate(list_computer_parts):
        print("{0}: {1}".format(number+1 , part))
    print("0: Finish")

list_final = []
user_input = -1
list_possible_options = []
for k in range(1,len(list_computer_parts) + 1):
    list_possible_options.append(k)

while user_input != 0:
    if user_input in list_possible_options:
        list_final.append(list_computer_parts[user_input - 1])
    else:
        print_parts(list_computer_parts)
    user_input = int(input())
    
    
print(list_final)