import requests, time, random, \
    os  # 引入requests库，用于网页数据爬取和文件读写；引入time库，用于调用sleep()函数；引入random库，用于调用randint()函数；引入os库，用于创建文件夹


def card():
    chara_name_list_png = ["优菈", "八重神子", "埃洛伊", "宵宫", "早柚", "枫原万叶", "烟绯", "甘雨", "神里绫人", "神里绫华", "罗莎莉亚", "达达利亚", "迪奥娜",
                           "钟离"]  # 角色卡片格式为.png的角色名称列表
    chara_name_list_jpg = ["七七", "丽莎", "九条裟罗", "云堇", "五郎", "凝光", "凯亚", "刻晴", "北斗", "可莉", "安柏", "托马", "旅行者（无属性）", "温迪",
                           "珊瑚宫心海", "班尼特", "琴", "申鹤", "砂糖", "胡桃", "芭芭拉", "荒泷一斗", "莫娜", "菲谢尔", "行秋", "诺艾尔", "辛焱", "迪卢克",
                           "重云", "阿贝多", "雷泽", "雷电将军", "香菱", "魈", "夜兰", "久岐忍", "鹿野院平藏"]  # 角色卡片格式为.jpg角色名称列表
    list = [chara_name_list_png, chara_name_list_jpg]  # 用于循环

    if not os.path.exists("角色卡片"):  # 判断是否存在文件夹，如不存在，继续
        os.mkdir("角色卡片")  # 新建文件夹

    for m in list:
        for i in range(0, len(m)):
            if m == chara_name_list_png:  # 文件名称
                suf = ".png"
            elif m == chara_name_list_jpg:
                suf = ".jpg"
            URL = "https://bbs.hoyolab.com/hoyowiki/picture/character/" + m[i] + "/avatar_header" + suf  # 网址
            if m[i] == "旅行者（无属性）":  # 官方只放出了无属性卡片，所以优化了一下提示内容
                m[i] = "旅行者"
            else:
                pass
            print("\n正在获取角色", m[i], "的角色卡片……")  # 提示信息
            webPage_info = requests.get(URL)  # 初步定位网址中的信息
            # 将二进制信息(因为是图片)返回给变量，这里重复利用了变量 webPage_info ，用于节省内存
            webPage_info = webPage_info.content
            doc_name = m[i] + suf
            # 以二进制形式(因为是图片)的写入权限新创建(如已有，则覆盖其内容)一个 角色名.png 文件
            spritePage = open("角色卡片\\" + doc_name, "wb")
            # 向文件 角色名.png 写入变量 webPage_info 中的内容(获取到的图片的二进制的信息码)
            spritePage.write(webPage_info)
            spritePage.close()  # 将文件保存并关闭
            print("角色", m[i], "的角色卡片", doc_name, "保存成功！")  # 提示信息
            if i == len(m) - 1:  # 如果是最后一个角色，则不等待
                pass
            else:  # 随机等待2~5秒的时间，防止被服务器禁IP
                num = random.randint(2, 5)
                print("\n等待", num, "秒，模拟真人手动操作，欺骗对方服务器……")
                for n in range(1, num + 1):
                    time.sleep(1)
                    print("已等待", n, "秒。")
