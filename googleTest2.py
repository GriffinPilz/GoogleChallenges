def solution(l, t):
    foundValue = False

    for i in range(len(l)):
        if l[i] == t:
            print([i])
            return [i, i]
        else:
            for x in range(len(l[i:])):
                x = x+1
                if sum(l[i:i+x]) == t:
                    foundValue = True
                    print([i, i+x-1], sum([l[i], l[i+x-1]]))
                    return [i, i+x-1]
    if foundValue == False:
        return [-1, -1]


print(solution([9,7,10,2,4], 9))