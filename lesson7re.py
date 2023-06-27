# # ori list ertshi produqti meoreshi fasevi daprintet ertad

# my_menu = ["khinkali", "Khachapuri", "Mtsvadi", "Lobio", "Shkmeruli"]
# prices = [2, 15, 20, 10, 14]


# ite = 0

# # for ite in range(len(my_menu)):
# #     print(my_menu[ite] + " costs " + str(prices[ite]) + " Lari.")


# # while ite in range(len(my_menu)):
# #     print(my_menu[ite] + " costs " + str(prices[ite]) + " Lari.")
# #     ite = ite +1
# print("---------------------------- დაიმახსოვრე და გამოიყენე!!!!")
# # !!!!!!!!!!!!ნიკამ გააკეთა < ნიშნით while i < len()


# # list with different type of values 

# # my_arr = ["banana", 11, True, 10.5, [1,2,3]]

# # print(my_arr[-1])
# # print(my_arr[3])

# # # output range of elements, (1:4 range; 2 step).
# # print(my_arr[1:4:2])

# # # from start to 4th ("slicing") range
# # print(my_arr[:5])

# # search in list (if True output)
# # my_menu = ["khinkali", "Khachapuri", "Mtsvadi", "Lobio", "Shkmeruli"]

# # if "Lobiani" in my_menu:
# #     print("Lobiani aris")
# # else:
# #     print("Lobiani ar gaqvs siashi shechemaaaaaaaa")
    
# # # subtitution of list element
# # my_menu[0] = "Caesar Salad"
# # print(my_menu)

# # # list range and adding static string
# # my_menu[1:3] = ["15% Discount on "]
# # print(my_menu)


# # change string value 
# name = "kukusha"
# #minda iyos nikusha


# new_name = ""

# # print("nik" + name[3:])

# my_name = "nikusha"

# new_name = ""


# მთელი შემდეგი ზოლები სტრინგის მნიშვნელობის შეცვლის ალტერნატივები

# for i in range(len(my_name)):
#     if i == 2 or i == 3:
#         new_name += "x"
#     else:
#         new_name += my_name[i]
# print(new_name)


# print(my_name.replace("ku", "qq"))
# print(my_name)

import fractions


my_name = 'nikusha'
# # 
# i = 0
# ii = 0
# # while i < len(my_name):
# if my_name[0] == "n" and my_name[1] == "i":
#     print("ti" + my_name[2:])
# i += 1
# my_name = "ti" + my_name[2:]

# my_name = my_name[0:2] + "xx" + my_name[4:]
# print(my_name)



# თქვენი custom იმპლემენტაცია

# ელემენტი, ცვლადი, შით = არგუმენტი.


menu = ["xinkali", "wvadi", "lobiani", "qababi"]

# inserting arguments in list .insert(პოზიცია3, არგუმენტი"nayini?"")
# menu.insert(3, "nayini")
# print(menu)

# # inserting but without position (deafult last pos. in list)
# menu.append("cecxli")
# menu.append("cecxli")
# print(menu)

# # menu.append menu.append
# # empty list insertation menu.append
# menu.append("pizza")
# print(menu)



# მომხმარებელს შემოატანინეთ 3 საჭმელი,
# სიაში შეიტანეთ ისინი, რომლებიც შეიცავენ მინიმუმ 2 "ა"-ს.


# f1 = input("food 1: ")
# f2 = input("food 2: ")
# f3 = input("food 3: ")
x = []
# # X A S H L A M A

# if True and True:
#     x += f1
#     x.append[""]
# f = "fdafs"
# x += f
# print(x)


# food = input("enter food name: ")
# a_symbols = 0           
# menu = []                     
# for i in range(len(food)):   #8
#     if food[i] == "a":   # if True
#         a_symbols += 1    # 0 + 1
# if a_symbols >= 2:                          #აი აქ მეშლებოდა ==, >= სწორი რადგან ხაშლამაზე ვამოწმებდი სადაც 3 ა იყო... ან მეორე სხვა შეცდომა პრინტი მქონდა უაზროდ ჩასმული ნაცვლად აფენდისა...
#     menu.append(food)
# print(menu)

# 1) false  2) True 3)false  4)  false  5)false6) True7) false  8) True




# a_symbols = 0           
# menu = []
# x = 0
# while x < 5:
#     food = input("enter food name: ")
#     x += 1
#     for i in range(len(food)):
#         if food[i] == "a":
#             a_symbols += 1
#     if a_symbols >= 2:
#         menu.append(food)

# print(menu)



# menu = ["xinkali", "wvadi", "lobiani", "qababi"]
# prices = [2, 20, 12, 18]

# for i in range(len(menu)):
#     print(menu[i]+ " ghirs " + str(prices[i]))

# my_arr = ["banana", 11, True, 10.5, [1,2,3]]

#მომხმარებელს შემოატანინეთ 5 საჭმელი,
# სიაში შეიტანეთ ისინი, რომლებიც შეიცავენ მინ. 2 ა-ს.
# menu = []
# a_counter = 0
# a_total = 0
# amount_of_input = int(input("Specify input number: "))
# if amount_of_input == 1:
#     food = input("enter food(1): ")
#     for i in range(len(food)):
#         if food[i] == "a":
#             a_counter += 1
#     if a_total + a_counter >=2:
#         menu.append(food)

# print(menu)

    
# x = int(input("enter x value"))
# if x  == 1:
#     print("True")



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


