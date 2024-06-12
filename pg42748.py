def solution(array, commands):
    answer = []  # 결과를 저장할 리스트 초기화
    for command in commands:  # 각 명령어를 하나씩 순회
        i, j, k = command  # 명령어에서 i, j, k 값을 추출
        # array의 i-1번째 인덱스부터 j번째 인덱스까지 잘라서 정렬
        num = sorted(array[i-1:j])[k-1]  
        # 정렬된 배열에서 k-1번째 인덱스의 값을 찾아 num에 저장
        answer.append(num)  # 찾은 값을 결과 리스트에 추가
    return answer  # 최종 결과 리스트 반환