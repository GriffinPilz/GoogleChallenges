def checkXOR(start, length):
    start = start
    count = length
    upCount = 0
    data = [0]
    workingSet = []
    if length == 0:
        print("0")
    else:
        while count > 0:
            tempList = []
            for i in range(length):
                number = i + start
                tempList.append(number)
            data += tempList
            start = data[-1]+1
            count-=1
            print("data: ", data, "d: ", data[-1]-upCount)
            print("tempList: ", tempList)
            for x in range(length):
                if tempList[x] <= data[-1]-upCount:
                    workingSet.append(tempList[x])
            upCount += 1
            print("workingSet: ", workingSet)
        output = 0 ^ workingSet[0]
        for i in range(len(workingSet)-1):
            output = output ^ workingSet[i+1]
        print(output)
        
    
checkXOR(100, 10)
