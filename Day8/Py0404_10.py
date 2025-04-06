# 문서 읽어오기 - r
# 일반 문서 읽어오기 - rb
f = open('Day8/a.jpg', 'rb')
fData = f.read()
f.close()
print('파일 읽어오기')

ff = open('Day8/b.jpg', 'wb')
len = ff.write(fData)
print(f"파일 크기: {len} 바이트")
ff.close

print("파일 저장 완료")

# 문서 저장 w,a
# 파일 저장 wb
# 폴더 존재 확인: os.path.exists() 폴더 1개 c:/down/aaa/a.jpg
# 폴더 생성 : os.makedirs() 모든 폴더 생성 c:/down/aaa/a.jpg

while True:
    fData = f.read(1)
    if not fData: break
    # len = ff.write(fData)
f.close()
print("파일 읽어오기 완료")