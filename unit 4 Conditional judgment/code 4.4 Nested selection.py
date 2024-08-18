# 嵌套选择(不推荐）
score = int(input('请输入分数：'))
if score >= 90:
    if score == 100:
        print('A+')
    else:
        print('A')
else:
    if score >= 80:
        print('B')
    else:
        if score >= 70:
            print('C')
        else:
            if score >= 60:
                print('D')
            else:
                print('E')