my_foods:list[str] = ['pizza', 'falafel', 'carrot cake']
friend_foods:list[str] = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)