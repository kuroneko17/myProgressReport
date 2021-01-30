minNum = int(input('Please enter the minNumber:'))
maxNum = int(input('Please enter the maxNumber:'))
for i in range(minNum,maxNum):
    if i%7 == 0 or i%10 == 7 or i//10 == 7 :
        continue
    print(i)
