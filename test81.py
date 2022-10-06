def start():
    return print("""Please choose your option from the list below:
\t1. Learn Python
\t2. Learn Java
\t3. Go swimming
\t4. Have dinner
\t5. Go to bed
\t0. Exit""")

number = "Teste"

while True:
    if number == '0':
        break
    elif number in "12345":
        print(number)
    else:
        start()
    number = input()
    
#####################
##
## test97
##
#####################