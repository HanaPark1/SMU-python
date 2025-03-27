# 날짜 시간

# 시간을 가져올 수 있는 날짜 클래스
import datetime

now = datetime.datetime.now()

print("현재 시간:",now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 시간이 12 이상이면 오후, 12 미만이면 오전이라고 하고 시간을 출력하시오
# 13시 -> 오후 1시
# 9시 -> 오전 9시

if now.hour >= 12:
    if now.hour == 12:
        print("현재는 오후 12시입니다")
    else:
        print("현재는 오후 {:02d}시 {:02d}분입니다".format((now.hour)-12, now.minute))
else:
    print("현재는 오전 {:02d}시 {:02d}분입니다".format(now.hour, now.minute))
    
print("{}년 {:02d}월 {:02d}일입니다.".format(now.year, now.month, now.day))