# 컨테이너 변수 - 리스트[] 튜플() 딕셔너리{} 셋{}
#딕셔너리{} 키:값
person = {'이름':'방재운', 
          '나이':17 , 
          '키':177, 
          '집주소':'남동구 만수동'}
print(person['이름'])
print(person)
person["몸무게"] = 70 
print(person)
person["키"]= 180
print(person)
del person["나이"]
print(person)
print(person.get("집주소"))

print("나이" in person)
print("이름" in person)
print("방재운" in person.values())