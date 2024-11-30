#문자열 인덱싱  
my = "저는 인평자동차고등학교 ai 소프트웨어과 1학년 1반 방재운입니다"

school = my[3:12:1]
print(school)
print(my[1:15:2])
major = my[13:22]
print(major)


text = 'python programming'
print(text)
print(text[7:11]) #-인덱싱
print(text[-7:-3]) #-인덱싱#7번지부터 끝까지
print(text[7:]) #7번지부터 끝까지#처음부터6-1번지까지 출력
print(text[:6]) #처음부터6-1번지까지 출력
print(text[-13:-19:-1])
print(text[7::2])
print(text[:15:3])




major = "AI소프트웨어과"
print(major[2:8])

#문자열 함수
# len 글자수세기
# count 특정 문자를 셀수있다
# 내장함수 메소드 .명령어() 

print(len(major))
major = "Ai software"
print(major.count("!"))
print(major.upper()) #모두 대문자로 변경
print(major.lower()) #모두 소문자로 변경
major= major.replace("AI","Happy AI") #값 대체
print(major)









