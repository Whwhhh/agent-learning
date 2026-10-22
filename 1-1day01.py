print("Hello! Agent Developer!")

scores=[56,95,87,39,100]

for score in scores:
    if score<60:
        print(f"分数{score}:不及格，你需要加油！")

    elif score<90:
        print(f"分数{score}:良好，还需努力！")

    else:
          print(f"分数{score}:很棒，不要骄傲！")
    