#출력 포메팅
name = "방재운"
age = 17
print("나의 이름은",name,"이고 나이는",age,"세입니다.")

#1
print("나의 이름은 %s이고 나이는 %d세입니다."%(name,age))
#2
print("나의 이름은 {}이고 나이는 {}세입니다.".format(name,age))
#3
print(f"나의 이름은 {name}이고 나이는 {age}세입니다.")
#실수 표현방식
print(f"{3.141592:0.4f}")
pi = 3.141592
print(format(pi,".4"))






