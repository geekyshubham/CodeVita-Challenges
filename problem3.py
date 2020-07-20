
num =8

numberList = "234 567 321 345 123 110 767 111"

numbers = numberList.split(' ')
bitScore = []

for i in range(num):
  maximum = int(max(list(numbers[i]))) * 11
  minimum = int(min(list(numbers[i]))) * 7
  Score = int(maximum + minimum)
  ScoreLst = str(Score)
  bitScore.append(ScoreLst[len(ScoreLst)-2:])
allOdds = []
#all the bitscore are traversed
for ele in bitScore[::2]:
  allOdds.append(ele[0])

countOdds = {}

for i in allOdds:
  countOdds[i] = allOdds.count(i)
#FIGURING OUT PAIRS THAT ARE twice or more
OddPairs = 0
print(countOdds)

for odd in countOdds:
  if int(countOdds[odd]) > 1:
    OddPairs = OddPairs + 1
    if int(countOdds[odd]) > 2:
      OddPairs = OddPairs + 1



allEvens = []
#splittting out most significant digit from 2 bitdigits
for ele in bitScore[1::2]:
  allEvens.append(ele[0])

countEvens = {}
#traversing throught the significants digits counting its multiples
for i in allEvens:
  countEvens[i] = allEvens.count(i)

evenPairs = 0
print(countEvens)
for even in countEvens:
  if int(countEvens[even]) > 1:
    evenPairs = evenPairs + 1
    if int(countEvens[even]) > 2:
      evenPairs = evenPairs + 1


print(evenPairs+OddPairs)


