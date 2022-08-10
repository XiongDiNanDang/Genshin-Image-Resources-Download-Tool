import requests, time, random, \
    os  # 引入requests库，用于网页数据爬取和文件读写；引入time库，用于调用sleep()函数；引入random库，用于调用randint()函数；引入os库，用于创建文件夹


def portrait():
    chara_zh_name_list = ["七七", "丽莎", "九条裟罗", "云堇", "五郎", "优菈", "八重神子", "凝光", "凯亚", "刻晴", "北斗", "可莉", "埃洛伊", "安柏", "宵宫",
                          "托马", "旅行者", "早柚", "枫原万叶", "温迪", "烟绯", "珊瑚宫心海", "班尼特", "琴", "甘雨", "申鹤", "砂糖", "神里绫人", "神里绫华",
                          "罗莎莉亚", "胡桃", "芭芭拉", "荒泷一斗", "莫娜", "菲谢尔", "行秋", "诺艾尔", "辛焱", "达达利亚", "迪卢克", "迪奥娜", "重云", "钟离",
                          "阿贝多", "雷泽", "雷电将军", "香菱", "魈", "夜兰", "久岐忍", "鹿野院平藏"]  # 角色中文名称列表
    chara_Eng_name_list = ["Qiqi", "Lisa", "Kujou Sara", "Yun Jin", "Gorou", "Eula", "Yae Miko", "Ningguang", "Kaeya",
                           "Keqing", "Beidou", "Klee", "Aloy", "Amber", "Yoimiya", "Thoma", "Traveler", "Sayu",
                           "Kaedehara Kazuha", "Venti", "Yanfei", "Sangonomiya Kokomi", "Bennett", "Jean", "Ganyu",
                           "Shenhe", "Sucrose", "Kamisato Ayato", "Kamisato Ayaka", "Rosaria", "Hu Tao", "Barbara",
                           "Arataki Itto", "Mona", "Fischl", "Xingqiu", "Noelle", "Xinyan", "Tartaglia", "Diluc",
                           "Diona",
                           "Chongyun", "Zhongli", "Albedo", "Razor", "Raiden Shogun", "Xiangling", "Xiao", "Yelan",
                           "Kuki Shinobu", "Shikanoin Heizou"]  # 角色英文名称列表

    if not os.path.exists("角色头像"):  # 判断是否存在文件夹，如不存在，继续
        os.mkdir("角色头像")  # 新建文件夹

    for i in range(0, len(chara_zh_name_list)):
        URL = "https://bbs.hoyolab.com/hoyowiki/picture/character/" + chara_Eng_name_list[i] + "_icon.png"  # 网址
        print("\n正在获取角色", chara_zh_name_list[i], "的角色头像……")  # 提示信息
        webPage_info = requests.get(URL)  # 初步定位网址中的信息
        # 将二进制信息(因为是图片)返回给变量，这里重复利用了变量 webPage_info ，用于节省内存
        webPage_info = webPage_info.content
        doc_name = chara_zh_name_list[i] + ".png"  # 文件名称
        # 以二进制形式(因为是图片)的写入权限新创建(如已有，则覆盖其内容)一个 角色名.png 文件
        spritePage = open("角色头像\\" + doc_name, "wb")
        # 向文件 角色名.png 写入变量 webPage_info 中的内容(获取到的图片的二进制的信息码)
        spritePage.write(webPage_info)
        spritePage.close()  # 将文件保存并关闭
        print("角色", chara_zh_name_list[i], "的角色头像", doc_name, "保存成功！")  # 提示信息
        if i == len(chara_zh_name_list) - 1:  # 如果是最后一个角色，则不等待
            pass
        else:  # 随机等待2~5秒的时间，防止被服务器禁IP
            num = random.randint(2, 5)
            print("\n等待", num, "秒，模拟真人手动操作，欺骗对方服务器……")
            for n in range(1, num + 1):
                time.sleep(1)
                print("已等待", n, "秒。")
