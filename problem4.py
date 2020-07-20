strs = list("25 30 35 20 90 110 45 70 80 12 30 35 85".split(' '))

num= list(map(int,strs))

num.sort(reverse=True)

list1 =[]
list2= []

print(num)

for i in range(len(num)):
  if len(list1) == 0 and len(list2) == 0:
    list1.append(num[i])
    continue
  if sum(list1) > sum(list2):
    list2.append(num[i])
    continue
  if sum(list2) > sum(list1):
    list1.append(num[i])
    continue
  if sum(list1) == sum(list2):
    list1.append(num[i])
    continue
  

print(sum(list1))

  
print(list1)
  
print(sum(list2))
print(list2)
