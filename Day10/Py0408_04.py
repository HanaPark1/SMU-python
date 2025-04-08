# []가 3번 중첩되어 있는 리스트
a = [[1,2,3],[4,[5,6]],7,[8,9]]

for i in a:
    if type(i) == list:
        for j in i:
            print(j,end=" ")
    else:
        print(i,end=" ")

def flatten(data):      
    output = []
    for i in data:
        if type(i) == list:
            output.extend(flatten(i))
        else:
            output.append(i)
    return output
print(flatten(a))

