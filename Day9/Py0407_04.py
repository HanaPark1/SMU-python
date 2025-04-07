# finally 예외시, 예외가 발생되지 않았을 때 모두 실행

try:
    f = open("info.txt", 'w', encoding='utf8')
    raise NotImplementedError
except Exception as e:
    print(e)
finally:
    f.close()
    
a_list = [1,2,3,4,5]
print(a_list)
try:
    print(a_list[5])
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except:
    print("모든 예외처리 가능")
    
raise NotImplementedError("프로그램 미구현-수정부분이 프로그램 진행해야 함")