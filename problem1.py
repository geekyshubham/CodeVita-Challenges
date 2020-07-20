
num =int(input())

brides = list(input())

grooms = list(input())

count= 0

while grooms[0] in brides and len(grooms) >= 0 and grooms[0]!= None:
  if grooms[0] == brides[0]:
    grooms.pop(0)
    brides.pop(0)
    count = count + 1
    if len(grooms) == 0:
      break
    

  else:
    temp = brides.pop(0)
    brides.append(temp)
    



print(num-count)
