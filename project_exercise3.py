import random
generator=[]
for number in range(5):
  generator.append(random.randrange(1,25))
print(generator)

def getBiggerNumber(x):
    max = 0
    for y in generator:
        if y > max:
            max = y
    print(max)

getBiggerNumber(generator)
