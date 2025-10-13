#############################################################################
# 1) 함수 구현 :
#   ∙ factorial_iter(n) -> int
#   ∙ 반복문으로 n! 계산. n<0이면 ValueError 발생.
#   ∙ factorial_rec(n) -> int
#   ∙ 재귀로 n! 계산. n<0이면 ValueError 발생.
#   ∙ run_with_time( ) -> 실행 결과와 경과 시간(초) 을 반환. (예외는 전파)

# 2) 인터랙티브 메뉴 : 
#   ∙ 아래 메뉴를 출력하고 사용자 입력에 따라 동작:
#   ∙ 1/2/3 선택 시 n을 문자열 입력으로 받아 정수인지 확인 후 처리
#   ∙ 4 선택 시 사전 정의된 테스트 케이스들에 대해 일괄 수행
# 3) 테스트 데이터 : 
#   ∙ 다음 리스트를 전역 변수로 두고 메뉴 4번에서 순회하며 실행: 
#     [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]
#   ∙ 각 n에 대해 반복/재귀를 모두 실행하고
#   ∙ 결과 일치 여부
#   ∙ 각 방식의 실행 시간
#   ∙ n! 값(전체)을 출력
# 4) 입출력/예외 :
#   ∙n이 정수가 아니거나 음수면 오류 메시지 출력 후 메뉴로 복귀
#   ∙재귀는 큰 n에서 RecursionError가 발생할 수 있음 → 예외 처리 필수 아님(그대로 노출 허용)
#############################################################################


def factorial_iter(n):
    # 반복문 기반 n! 계산
    result = 1
    for k in range(2, n+1):
        result *= k
    return result
    
def factorial_rec(n):
    # 재귀함수 기반 n! 계산
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial_rec(n-1)

def run_with_time(func, n):
    import time
    start = time.time()
    result = func(n)
    end = time.time()
    return  end - start

def equal(res1, res2):
    if res1 == res2:
        return "일치"
    else:
        return "불일치"

test_data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def main():
    
    while True:
        print("팩토리얼 계산기 (반복/제귀) - 정수 n>=0를입력하시요. \n")
        print("=====Factorial Tester=====\n")
        print("1) 반복적으로 n! 계산 \n")
        print("2) 재귀로 n! 계산 \n")
        print("3) 두 방식 모두 계산 후 결과/시간 비교 \n")
        print("4) 준비된 테스트 데이터 일괄 실핼 \n")
        print("q) 종료.\n")
        print("---------------------------\n")
        
        choice = input("선택: ").strip()
        if choice == 'q' or choice == 'Q':
            print("종료합니다.")
            break
        
        elif choice not in ['1', '2', '3', '4']:
            print("1,2,3,4 중에서 선택하세요. \n")
            continue
        
        if choice == '4':
            print("테스트 데이터 실행\n")
            for n in test_data:
                iter_time = run_with_time(factorial_iter, n)
                rec_time = run_with_time(factorial_rec, n)
                print(f"n = {n} | same={equal(factorial_iter(n), factorial_rec(n))} | iter={iter_time:.6f}s , rec={rec_time:.6f}s")
            print()
            continue
        if choice in ['1', '2', '3']:
            user_input = input("\nn 값(정수, 0 이상)을 입력하세요: ").strip()
            if not user_input.isdigit():
                print("정수 (0 이상의 숫자)만 입력해 주세요.")
                continue
            n = int(user_input)
            if n < 0:
                print("0 이상의 숫자를 입력해 주세요.")
                continue

        if choice == '1':
            print(f"[반복] {n}!" , factorial_iter(n), "[반복] 시간: {run_with_time(factorial_iter, n)} s" )
            print(f"[반복] 시간: {run_with_time(factorial_iter, n)} s \n" )
            
        elif choice == '2':
            print(f"[재귀] {n}!" , factorial_rec(n))
            print(f"[반복] 시간: {run_with_time(factorial_rec, n)} s \n" )
        
        elif choice == '3':
            print(f"[반복] {n}!" , factorial_iter(n))
            print(f"[재귀] {n}!" , factorial_rec(n))
            print("결과 일치 여부: ", equal(factorial_iter(n), factorial_rec(n)))
            print(f"[반복] 시간: {run_with_time(factorial_iter, n)} s  |  [재귀] 시간: {run_with_time(factorial_rec, n)} s")

        
            

if __name__ == "__main__":
    main()