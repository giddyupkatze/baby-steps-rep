
# homework correction and discussion
# shopping_list = ["Soup", "Matsoni", "Granola", "Cookies", "Bread"]
# shopping_paycheck = [2.5, 3, 5, 2, 1.5]

# print(len(shopping_list))
# print(len(shopping_paycheck))

# i = 0 #saiteracio cvladi
# while i < len(shopping_list):
#     print(shopping_list[i]+ " costs " + str(shopping_paycheck[i]) + " Lari.")
#     i += 1

# prices = [0, 0, 0, 0, 0, 0]
# prices[0] = 12.7
# print(prices)


# my_arr = ["banana", 11, True, 10.5, [1,2,3]]

# prices = [2, 20, 15, 10, 15, 2, "nika"] #python
# # int prices = [2, 20, 15, 10, 15, 2] java  #აქ სტრინგის დამატება პრობლემატურია...

# #კვადრატული ფრჩხილით შექმნილი კოლექცია არის ლისთი. კოლექცია - ელემენტების მიმდევრობა
# my_arr = ["banana", 11, True, 10.5, [1,2,3]]
# # print(my_arr[-1])
# # print(my_arr[3])
# # print(my_arr[1:3])
# # print(my_arr[0:6:2]) #ყოველი მეორე გამოიტანა...
# # print(my_arr[:4])   #დასაწყისიდან მეოთხემდე, როგორც სტრინგში ისე სიებში სლაისი და რეინჯი

# # შევამოწმოთ ჩვენს სიაში...
# menu = ["Soup", "Matsoni", "Granola", "Cookies", "Bread"]

# # if "Matsoni" in menu:
# #     print("Matsoni gvaqvs")

# # მენიუში ინდექსის დადხმარებით სიის ელემენტის განახლება / შეცვლა
# menu[1] = "Lobiani"
# print(menu)
# print(menu[1])

# # მენიუში ახალი მნიშვნელობები რეინჯში სლაისინგით
# menu[2:4] = ["Butter", "Watermelon"]
# print(menu)

# string object does not support item assignment
# my_name = "nikusha"
# my_name[3] = "a" 
# print(my_name)  #

# alternative of changinge string symbols
# my_name = "nikusha"
# new_name = ""
# for i in range(len(my_name)):
#     if i == 2 or i ==3:
#         new_name += "xx"
#     else:
#         new_name += my_name[i]
    
# print(new_name)
# my_name = "nikusha"
# my_name.replace("ku", "qq") #ar mushaobs
# print(my_name)
# print(my_name.replace("ku", "qq"))



# test1 = "xinkali girs ?? lari"
# print(test1.replace("??", str(2)))

# .insert - ჩამატება პოზიციის მითითებით
# menu = []
# menu.insert(3, "Ice-Cream")
# # print(menu)

# # .append  - ჩამატება
# menu.append("Fire")
# # print(menu)
# menu.append("Gasolin")
# print(menu)

# # ცარიელის სიის შექმნა
# menu = []
# menu.append("pizza")
# print(menu)



# მომხმარებელს შემოატანინეთ 5 საჭმელი,
# სიაში შეიტანეთ ისინი რომლებიც შეიცავენ
# მინიმუმ 2 'ა'- ს.
# new_food = []
# i = 0
# while i in range(5):
#     food = [input("enter food names:")]
#     i += 1
# if "aa" in food[i]:
#     food[i] += new_food[i]
    
# print(new_food)

# menu = []
# for i in range(5):
#     food = input("enter food: " )
#     if food.count("a") >=2:
#         menu.append(food)

# print(menu)
# amount_of_a = 0
# menu = []
# for i in range(2):
#     food = input("enter food: " )
#     for char in food:
#         if char == "aa":
#             amount_of_a += 1
#     if amount_of_a >=2:
#         menu.append(food)

# print(menu)



