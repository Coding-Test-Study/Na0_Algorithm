def solution(dartResult):
    answer = 0
    score = [i for i in range(0,11)]
    bonus = ['*','#']
    option = ['S','D','T']

    for i in dartResult:
        if i in score:
            answer.append(i)
        elif i in bonus:
            if i==bonus[0]:
     
        elif i in option:

            
    return answer
    
li = list(input())
print(li)
