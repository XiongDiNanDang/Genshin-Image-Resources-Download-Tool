import requests, time, random, \
    os  # 引入requests库，用于网页数据爬取和文件读写；引入time库，用于调用sleep()函数；引入random库，用于调用randint()函数；引入os库，用于创建文件夹


def costume():
    chara_name_list = ["凝光", "刻晴", "安柏", "琴", "罗莎莉亚", "芭芭拉", "莫娜"]  # 角色名称列表

    if not os.path.exists("角色衣装立绘"):  # 判断是否存在文件夹，如不存在，继续
        os.mkdir("角色衣装立绘")  # 新建文件夹

    for i in range(0, len(chara_name_list)):
        URL = "https://bbs.hoyolab.com/hoyowiki/picture/character/" + chara_name_list[i] + "/costume.png"  # 网址
        print("\n正在获取角色", chara_name_list[i], "的角色衣装立绘……")  # 提示信息
        webPage_info = requests.get(URL)  # 初步定位网址中的信息
        # 将二进制信息(因为是图片)返回给变量，这里重复利用了变量 webPage_info ，用于节省内存
        webPage_info = webPage_info.content
        doc_name = chara_name_list[i] + ".png"  # 文件名称
        # 以二进制形式(因为是图片)的写入权限新创建(如已有，则覆盖其内容)一个 角色名.png 文件
        spritePage = open("角色衣装立绘\\" + doc_name, "wb")
        # 向文件 角色名.png 写入变量 webPage_info 中的内容(获取到的图片的二进制的信息码)
        spritePage.write(webPage_info)
        spritePage.close()  # 将文件保存并关闭
        print("角色", chara_name_list[i], "的角色衣装立绘", doc_name, "保存成功！")  # 提示信息
        if i == len(chara_name_list) - 1:  # 如果是最后一个角色，则不等待
            pass
        else:  # 随机等待2~5秒的时间，防止被服务器禁IP
            num = random.randint(2, 5)
            print("\n等待", num, "秒，模拟真人手动操作，欺骗对方服务器……")
            for n in range(1, num + 1):
                time.sleep(1)
                print("已等待", n, "秒。")
