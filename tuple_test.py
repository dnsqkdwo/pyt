'''
#컨테이너 변수 - 리스트[],튜플(),셋{},딕셔너리{}
#튜플 변수 : 변경 불가, 변경하면 안되는 값을 튜플 변수로 지정 
my_tuple=("사과","메론","포도","토마토")
#my_tuple.append("수박") 튜플은 값 추가 불가
#my_tuple.remove("사과") 튜플은 값 삭제 불가 
print(my_tuple[:3]) #0~2번지까지 출력
print(len(my_tuple))
print("샤인머스켓" not in my_tuple)
'''

my_tuple=("사과","메론","포도")#패킹
(f1,f2,f3)=my_tuple #언패킹
number = (1,2,3,4,5,6,7,8,9,10)#패킹
(*others,n9,n10) =number
print(others)
