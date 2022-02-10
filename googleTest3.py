def solution(xs):
    positiveArray = []
    negativeArray = []
    for x in xs:
        if x > 0:
            positiveArray.append(x)
        elif x < 0:
            negativeArray.append(x)
    if (len(negativeArray) % 2) != 0:
        negativeArray.sort()
        negativeArray.pop()
    listFinal = negativeArray + positiveArray
    if len(listFinal) > 0:
        maxOutput = 1
        for x in listFinal:
            maxOutput = maxOutput * x
        print(str(maxOutput))
        return
    print(str(0))

solution([2,0,2,2,0])
#output = 8