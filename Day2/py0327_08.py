# bool, int, float, str
# list - 배열

a = 10
fruit = ['사과', '배', '딸기', '포도']

f_input = input("과일을 입력하세요")
fruit.append(f_input)

if '사과' in fruit:
    print("사과 있어요!!")
else:
    print("사과 없습니다")
    
print(fruit[0])

    
info_list = [{"galContentId":"2586952","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/52/2586952.jpg","galCreatedtime":"20190109152342","galModifiedtime":"20190109152354","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},{"galContentId":"2586949","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/49/2586949.jpg","galCreatedtime":"20190109152321","galModifiedtime":"20190109152332","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},{"galContentId":"2586948","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/48/2586948.jpg","galCreatedtime":"20190109152256","galModifiedtime":"20190109152311","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"}]

print(info_list[0]['galTitle'])

#2,4,6,8번째 방의 합들을 구하시오
num = [1,2,3,4,5,6,7,8,9,10]
print(num[2]+num[4]+num[6]+num[8])

num_input = int(input("숫자를 입력하세요"))

if num_input in num:
    print("{}은 있습니다!".format(num_input))
else:
    print("{}은 없습니다 ㅜㅜ!".format(num_input))