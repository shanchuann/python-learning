cards = []
def menu():
    print("名片管理系统".center(30, "*"))
    print("1.添加名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 35)

def new_card(name, phone, qq, email):
    user = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }
    cards.append(user)
    return True

def show_card():
    for user in cards:
        print("姓名:%s\n电话:%s\nQQ:%s\n邮箱:%s" % (user["name"], user["phone"], user["qq"], user["email"]))
    if len(cards) == 0:
        print("无名片信息")

def quary_card(kw):
    for code in cards:
        for k, v in code.items():
            if kw == v:
                print("姓名:%s\n电话:%s\nQQ:%s\n邮箱:%s" % (code["name"], code["phone"], code["qq"], code["email"]))
                return code
    print("无此名片信息")

def modify_card():
    name = input("请输入姓名:")
    for code in cards:
        for k, v in code.items():
            if name == v:
                phone = input("请输入电话:")
                qq = input("请输入QQ:")
                email = input("请输入邮箱:")
                code["phone"] = phone
                code["qq"] = qq
                code["email"] = email
                print("修改成功")
                return True
    print("修改失败")

def del_card():
    name = input("请输入姓名:")
    for code in cards:
        for k, v in code.items():
            if name == v:
                cards.remove(code)
                print("删除成功")
                return True
    print("删除失败")

def quit():
    print("退出系统")

def main():
    menu()
    while True:
        op = input("请输入操作:")
        if op == "1":
            name = input("请输入姓名:")
            phone = input("请输入电话:")
            qq = input("请输入QQ:")
            email = input("请输入邮箱:")
            result = new_card(name, phone, qq, email)
            if result:
                print("添加成功")
            else:
                print("添加失败")
        elif op == "2":
            show_card()
        elif op == "3":
            kw = input("请输入查询关键字:")
            quary_card(kw)
            op2 = input("是否修改,删除名片信息(1.是 2.否)")
            if op2 == "1":
                op3 = input("请选择操作(1.修改 2.删除)")
                if op3 == "1":
                    modify_card()
                elif op3 == "2":
                    del_card()
                else:
                    print("输入有误,请重新输入")
            elif op2 == "2":
                print("返回主菜单")
            else:
                print("输入有误,请重新输入")
        elif op == "0":
            quit()
            break
        else:
            print("输入有误,请重新输入")
