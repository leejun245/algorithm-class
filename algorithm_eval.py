# 알고리즘 시간 복잡도  기말고사에서 이런 식으로 코드에서 얼마나 비교, 이동연산이 몇번 했는지
# 예제 리스트에서 최대값 찾기
# 비교연산 및 이동연산 기반 효율성 분석

def find_max(A):
    # A는 리스트
    n = len(A) # 입력크기
    move_count = 0 # 이동연산 횟수
    comp_count = 0 # 비교연산 횟수

    max_val = A[0] # 초기화 (이동연산 1회)
    move_count += 1

    for i in range(1, n): # 1부터 n-1까지 반복
        comp_count += 1 # A[i] > max_val 비교 연산
        if A[i] > max_val:
            max_val = A[i] # 이동연산 1회
            move_count += 1

    return max_val, comp_count, move_count

def selection_sort(arr): # 선택 정렬
    a = arr[:] # 원본을 복사
    n = len(arr) #배열 크기
    for i in range(n-1): # i번쨰 위치에서 최소값 삽입
        least_idx = i # 최소값 인덱스
        for j in range(i+1, n): # i+1 ~ n-1 미정렬된 구간 탐색
            if a[j] < a[least_idx]: # 더 작은 값을 발견
                least_idx = j # 최소값 인덱스 갱신
        a[i], a[least_idx] = a[least_idx], a[i] # 최소값과 i번째 위치 교환
    return a

def insertion_sort(arr): # 삽입 정렬
    a = arr[:] # 원본을 복사
    n = len(arr) #배열 크기
    for i in range(1, n): # 두번쨰 요소부터 시작
        key = a[i] # 삽입할 원소
        j = i-1 # 정렬된 구간의 마지막 인덱스
        while j >= 0 and a[j] > key: # 삽입 위치 확인 앞은 범위를 안 벗어나게 하기위해
            a[j+1] = a[j] # 요소를 한칸 뒤로 이동 
            j -= 1 # 인덱스 감소
        a[j+1] = key # 삽입
    return a


#=============================================
# 테스트 코드
#=============================================
if __name__ == "__main__":
    data = [3, 9, 2, 7, 5, 10, 4]
    # result, comp, move = find_max(data) # 이동연산+ 비교연산에 대한 카운트
    # print(f"비교연산 횟수: {comp}, 이동연산 횟수: {move}") # 이동 초기화 + 이동 + 이동으로 이동은 3번이다

    #sorted_data = selection_sort(data)  # 선택 정렬
    ins = insertion_sort(data) # 삽입 정렬
    print(ins)