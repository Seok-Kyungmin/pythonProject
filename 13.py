from collections import deque

def solution(priorities, location):
    answer = 0

    # deque 구조만들기
    # 키 : [2, 1, 3, 2] 값으로 설정 / 값 : location과 매칭할 인덱스
    # myDeque 변수 값 : deque([2, 0), (1, 10, (3, 2), (2, 3)])
    myDeque = deque([(v,i) for i,v in enumerate(priorities)])

    #print(myDeque)

    while myDeque:

        firstData = myDeque.popleft()

        if myDeque and max(myDeque)[0] > firstData[0]:
            myDeque.append(firstData)

        else:
            answer += 1

            if location == firstData[1]:
                break
    return answer
