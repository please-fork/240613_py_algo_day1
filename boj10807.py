N = int(input())  # 입력으로 주어지는 정수의 개수를 N에 저장
A = map(int, input().split())  # 입력으로 주어진 정수들을 공백을 기준으로 분리하여 A에 저장
v = int(input())  # 찾고자 하는 정수를 v에 저장
answer = 0  # v와 같은 정수의 개수를 셀 변수 초기화

for a in A:  # A 리스트의 모든 정수들을 하나씩 a에 저장하며 반복
    if a == v:  # 현재 정수 a가 v와 같은 경우
        answer += 1  # v와 같은 정수의 개수를 1 증가

print(answer)  # 최종적으로 v와 같은 정수의 개수를 출력