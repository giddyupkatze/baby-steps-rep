# .append() - the append() function is used to add an item to the end of the list. for ex.:
# nums = [1, 2, 3]
# nums.append(4)
# print(nums)
# Outcome [1, 2, 3, 4]

# String repeat by * sign
# x = 'abc'
# x *= 2
# print(len(x))

# .append - o add a new argument onto a list
# list = ['bla', 'blu', 'ble']
# list.append('z')
# print(list)
# 'z' is added to the list(in the end)

# .insert(1, "star") -insert a new argument with given position
# words = ['Python', 'Fun']
# words.insert(1, 'Star')
# print(words)

# .list('r') function - index() finds the first occurrence of a list item and returns its index
# # fruits = ["Apple", "Tomato", "Peach"]
# letters = ['a', 'b', 'c', 'd', 'e']
# numbers = [1, 2, 3, 4, 5, 10, 20]
# print(letters.index('d'))
# print(fruits.index("Peach"))
# print(numbers.index(4))

# print(letters[0]+letters[2]+letters[4]) #ace


# # fyunctions min() and max()
# shorts_prices = [1, 8, 42, 3]
# print(min(shorts_prices))
# print(max(shorts_prices))

# list.count(item) - Returns a count of how many times an item occurs in a list.
# list.remove(item) - Removes an item from a list.
# list.reverse(item) - Reverses items in a list.
x = [2, 4, 6, 2, 7, 2, 9]
water_types = ["Sp.Water", "Still Water", "Tap Water"]
letters = ["a", "e", "i", "o", "u"]
names = ["Michael", "Natasha", "Jim"]
# print(x.count(2)) # counts entered elements
# print(water_types.count("Tap Water"))
# print(letters.count("o"))
# print(names[1].count("a"))


# removes the arguments in list
# x.remove(2)
# print(x)
# water_types.remove("Tap Water")
# print(water_types)

# .reverse() - reverses list arguments
# x.reverse()
# print(x)
# water_types.reverse()
# print(water_types)
# SO ONLY LISTS CAN HAVE THIS HAPPEN..
# name = "nika"
# name.reverse()
# print(name)




# List Functions
# You are working on a queue management program.

# The queue is represented by a list. 

# Write a program to take an input, add it to the end of the queue, and output the resulting list.

# level
# The append() method can be used to add new items to the list.

queue = ['John', 'Amy', 'Bob', 'Adam']
name = input()
queue.append(name)
print(queue)