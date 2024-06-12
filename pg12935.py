def solution(arr):
    if len(arr) == 1:  # 배열의 길이가 1인 경우
        return [-1]  # -1을 요소로 갖는 배열을 반환
    
    # 1번: 최소값을 찾아 배열에서 제거하는 방법
    # arr.remove(min(arr))
    
    # 2번: 배열을 정렬하여 최소값을 찾아 제거하는 방법
    # arr.remove(sorted(arr)[0])
    
    # 3번: 최소값을 찾아 새로운 배열에 최소값을 제외한 요소들만 추가하는 방법
    min_val = min(arr)  # 배열에서 최소값을 찾음
    new_arr = []  # 새로운 배열을 초기화
    for v in arr:  # 기존 배열의 모든 요소를 하나씩 순회
        if v != min_val:  # 현재 요소가 최소값이 아닌 경우
            new_arr.append(v)  # 새로운 배열에 추가
    return new_arr  # 최소값을 제외한 새로운 배열을 반환
