print("Hello! Agent Developer!")

scores=[56,95,87,39,100]

for score in scores:
    if score<60:
        print(f"分数{score}:不及格，你需要加油！")

    elif score<90:
        print(f"分数{score}:良好，还需努力！")

    else:
          print(f"分数{score}:很棒，不要骄傲！")

#交互式键盘输入

score= int(input("请输入你的分数："))

if score<60:
    print(f"分数{score}:不及格，你需要加油！")

elif score<90:
    print(f"分数{score}:良好，还需努力！")

else:
    print(f"分数{score}:很棒，不要骄傲！")

#while 循环
secret_num=int(input("请输入1-100 之间的1个数字"))

flag=True

while flag:
    if secret_num>100 or secret_num<0 :
        print("输入有误！")
        flag=True
        secret_num=int(input("请重新输入1-100 之间的1个数字"))
    else:
        flag=False
        
print("我已经想好了一个 1-100 之间的数字，你来猜猜看！")

# 开始无限循环（while True 意思是一直循环，直到遇到 break）
while True:
    # 接收用户输入，并转换为整数
    guess = int(input("请输入你猜的数字："))
    
    # 判断逻辑
    if guess == secret_num:
        print("🎉 恭喜你，猜对了！")
        break  # break 的意思是“打破”循环，程序退出
    elif guess > secret_num:
        print("猜大了，往小了猜！")
    else:
        print("猜小了，往大了猜！")
    