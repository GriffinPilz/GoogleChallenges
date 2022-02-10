data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
n = 1

def solution(data, n): 
    if len(data) < 100:
        if n < 1:
            return None
        else:
            def checkInteger(x):
                return int(x)
            result = list(map(checkInteger, data))
            newResult = []
            finalList = []
            for i in result:
                if result.count(i) > n:
                    pass
                else:
                    newResult.append(i)
            for i in newResult:
                if i not in finalList:
                    finalList.append(i)
            print(finalList)

solution(data, n)