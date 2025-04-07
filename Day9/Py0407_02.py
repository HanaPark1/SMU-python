a_list = [1,2,3,4,5]
for a in a_list:
    print(a)
    
# for i in range(6):
#     print(a_list[i]) # 구문에 에러는 없지만 실행시 에러 - 런타임 에러
# - 프로그램이 종료

# 예외 처리
print("1. 학생 성적 출력")
choice = int(input("원하는 번호를 입력하세여: "))
# if choice.isdigit():
# # 숫자로 변환 가능한지 확인
#     choice = int(choice)
# else:
#     print("숫자만 입력이 가능합니다. ")
try: # 예외처리 강제로 프로그램이 종료되는 문제를 해결, 에러에 대한 문제점 확인
    choice = int(choice)
except Exception as e:
    print("숫자만 입력")
    print(e) # 에러의 구문 출력 가능
print("입력한 번호:",choice)

    
    