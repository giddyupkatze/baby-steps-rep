#მომხმარებელს შემოატანინეთ 5 საჭმელი,
# სიაში შეიტანეთ ისინი, რომლებიც შეიცავენ მინ. 2 ა-ს.
menu = []
a_counter = 0
a_total = 0

amount_of_input = int(input("Specify input number: "))
for z in range(amount_of_input):
    food = input("enter food: ")

    for i in range(len(food)):
        if food[i] == "a":
            a_counter += 1
    if a_total + a_counter >=2:
        menu.append(food)

print(menu)



# :d