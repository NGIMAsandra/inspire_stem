friends = ["Sandra", "samuel", "Suzie", "rose","max"]
for friend in friends:
    print(friend)

enemies = friends[:]
for enemy in enemies :
    print(enemy)

#fruits
fruits = ["Apple","orange","pear", "Banana","strawberry"]
print(fruits[0:3])

del fruits[0]
print(fruits)

squares =[] # initializes an empty list
for x in range(0,11) :
    squares . append(x**2)
print (squares)