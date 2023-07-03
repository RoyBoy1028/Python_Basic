# Tuple tuple=()
samsung_smart_phone = ('galaxy23', ('galaxy watch 4', 'galaxy watch 5'), 'galaxy flip 5')
print(samsung_smart_phone)
print(samsung_smart_phone[1])
print(len(samsung_smart_phone))
# samsung_smart_phone[1] = 'galaxy watch 5' error

###### List ######
fruits = ['apple',  ['mandarin', 'orange'], 'banana', 132, 'lychee']
print(fruits[2])
print(fruits[1][0], fruits[2])

fruits.append('melon') # add to list of fruits list=[]
print(fruits)

fruits.remove('banana')
print(fruits)

last = (fruits.pop())
print(last)
print(fruits)

fruits[1] = 'watermelon'
print(fruits)

# Dictionary = {}
weather = {'vancouver' : 'sunny', 'seoul':'rain', 'washington':'cloudy'}
print(weather['washington'])

students = {'name' : ['minsoo', 'Roy', 'Dain', 'David'], 'address' : ['vancouver', 'vancouver', '', 'Newyork']}
print(students ['name'])
print(students)

total = {'adult' : 1}
total['adult'] += 1
print(total['adult'])