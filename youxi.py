import random

def guess_number():
    # 生成一个1-100之间的随机数
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        # 接收用户输入的数字
        guess = int(input("请猜一个1-100之间的数字："))
        attempts += 1
        if guess == secret_number:
            print(f"恭喜你，你猜对了！你用了{attempts}次尝试。")
            break
        elif guess < secret_number:
            print("你猜的数字太小了，请再试一次。")
        else:
            print("你猜的数字太大了，请再试一次。")

if __name__ == '__main__':
    guess_number()
