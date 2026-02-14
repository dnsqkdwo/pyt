import random

# 1부터 100 사이의 랜덤 숫자 생성
secret_number = random.randint(1, 100)
attempts = 0

print("🎮 숫자 맞추기 게임!")
print("1부터 100 사이의 숫자를 맞춰보세요.\n")

while True:
    try:
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1
        
        if guess < secret_number:
            print("⬆️ 더 큰 숫자입니다!")
        elif guess > secret_number:
            print("⬇️ 더 작은 숫자입니다!")
        else:
            print(f"🎉 정답입니다! {attempts}번 만에 맞추셨네요!")
            break
    except ValueError:
        print("❌ 올바른 숫자를 입력해주세요!")

print("\n게임 종료!")