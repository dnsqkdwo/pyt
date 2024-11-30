#예외처리 
#클래스
#파일처리  폴더(디렉토리)

f = open('live.txt','wt')
f.write('''삶이 그대를 속일지라도
슬퍼하거나 노하지 말라
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리다''')
f.close()
while True:
    f = open('live.txt','rt')
    text = f.read(10)
    if len(text) ==0:
        break
    print(text)
print(text,end='')
f.close()