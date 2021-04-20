age = 19
x = 0
user_prompt = True
list_data = [1, 2, 3, 4, 6, 8, 5]
em_list = [[1, 2, 3], [2, 3, 4]]

# if age > 18:
#     print("You're older than 18!")
# elif age == 18:
#     print("You're exactly 18")
# else:
#     print('You\'re younger than 18!')

# for i in list_data:
#     print(i)

# for i in em_list:
#     print(i)

# for i in em_list:
#     for j in i:
#         print(j)

while x < 10:
    print(x)
    if x == 4:
        print("You've hit a breakpoint! Aborting while loop...")
        break
    x += 1

while user_prompt:
    your_age = input("What is your name")
    if age.isdigit():
        user_prompt = False
    else:
        print("")

