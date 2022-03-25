# 풀이 방법
# 문제의 특징
# 정답예제는 마라톤 미완주자는 무조건 1명만 나옴
# 해시 값은 값에 따라 중복되지 않은 숫자 값이 1,000이라면,
# 완주자는 1명만 부족하기에 1,000
def solution(participant, completion):

    #해시값의 총 합을 저장할 변수
    tmp = 0

    #해시값과 이름이 저장되는 키값 구조
    dic = {}

    #참여자 전체 해시값 더하기 및 이름(해시값) 저장하기
    for p in participant:

        dic[hash(p)] = p

        tmp += int(hash(p))

    for com in completion:

        tmp -= hash(com)

    return dic[tmp]