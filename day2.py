# Day 2:** Find the largest of three numbers using only nested `if` statements.

num1 = 5
num2 = 25
num3 = 15

if num1 >= num2:
    if num1 >= num3:
        print(f"THE NUMBER 1 IS GREATER :- {num1} ")
    else:
        print(f"NUMBER 3 IS GREEATER :- {num3}")

else:
    if num2 >= num3:
        print(f"THE NUMBER 2 IS GREATER :- {num2} ")
    else:
        print(f"NUMBER 3 IS GREEATER :- {num3}")
