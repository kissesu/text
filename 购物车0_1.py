# 登陆
login_name = input("请输入用户名: ")
login_pwd = input("请输入密码:")

with open('shoppingCart.txt','r',encoding='utf-8') as f:
    temp = f.read()
    # print(len(temp))
    # print(type(temp))
    # print(temp)
    if len(temp) == 0:
        temp = {}
        f.close()
    else:
        temp = eval(temp)
        if temp[login_name] in temp:
            print(temp[login_name][-1])
    # 充值
        else:
            if temp[login_name][-1] == 0:
            balance = 0
            print("余额为0,请充值后再购买商品")
            balance = int(input("请输入充值金额(元): "))
            print('+++++++++++++++++++++++++++')
            print("现余额为\033[1;31m %s \033[0m元" % balance)
            print('+++++++++++++++++++++++++++')

            # 设置退出标签
            # 设置购物车空列表
            shoppingCart = []
            exit_flag = False
            while not exit_flag:
                # 商品列表
                goods = [
                    {"name": "Apple iPad Pro", "price": 5538},
                    {"name": "Apple iMac", "price": 12499},
                    {"name": "Apple Mac Pro", "price": 19888},
                    {"name": "Mac Book Pro", "price": 16999},
                    {"name": "Mac book Air", "price": 7399},
                ]

                # 打印商品列表
                print("------------ 商 品 列 表 ------------")
                for index, item in enumerate(goods):
                    print("\033[0;30m{:3}.  {:15}  {:10}\033[0m".format(index, item["name"], item["price"]))
                print("-------------- E N D --------------")

                # 选择商品
                choice = input("输入编码(0~4)购买商品\n输入字母 'q' 或 'Q' 退出: ")

                # 计算余额
                if choice.isdigit():
                    if 0 <= eval(choice) <= 4:
                        shoppingCart.append(goods[eval(choice)])
                        balance -= goods[eval(choice)]["price"]
                        while balance < 0:
                            balance = int(input("現余额为\033[1;31m %s \033[0m元,已不足,请输入充值金额(元): " % (balance))) + balance
                            print('+++++++++++++++++++++++++++')
                            print("现余额为\033[1;34m %s \033[0m元" % balance)
                            print('+++++++++++++++++++++++++++')
                    else:
                        print("-----> 输入错误! ")
                        print("-----> 请输入(0~4)之间的编码 或 字母(q or Q)退出 ")
                elif choice.lower() == 'q':
                    # f.write(temp[login_name]=shoppingCart)
                    print("┏━━━━━━━━━━━━ 购物车 ━━━━━━━━━━━┓")
                    for index, item in enumerate(shoppingCart):
                        print("\033[1;31m{:3}.  {:15}  {:7}\033[0m".format(index, item["name"], item["price"]))
                        # count += 1
                    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                    print("余额:\033[1;34m %s \033[0m" % (balance))
                    shoppingCart.append(balance)
                    temp[login_name] = shoppingCart
                    print(temp)
                    with open('shoppingCart.txt','a+',encoding='utf-8') as f:
                        f.write(str(temp))
                        f.close()
                    exit_flag = True
                elif choice.lower == 'c':
                    temp = eval(temp)
                    # print(temp)
                    for k, v in temp.items():
                        if login_name == k:
                            # print(temp[login_name])
                            for k, v in enumerate(temp[login_name]):
                                print(k, v['name'], v['price'])
