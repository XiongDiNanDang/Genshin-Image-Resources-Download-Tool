# 作者：兄弟难当
# 版本：1.0.7


# 选择utf-8编码，因为chara_name_list中有生僻字
# -*- coding:utf-8 -*-

import requests, time, random, os  # 引入requests库，用于网页数据爬取和文件读写；引入time库，用于调用sleep()函数；引入random库，用于调用randint()函数；引入os库，用于创建文件夹

chara_name_list = ["七七", "丽莎", "九条裟罗", "云堇", "五郎", "优菈", "八重神子", "凝光", "凯亚", "刻晴", "北斗", "可莉", "埃洛伊", "安柏", "宵宫", "托马", "早柚", "枫原万叶", "温迪", "烟绯", "珊瑚宫心海", "班尼特", "琴", "甘雨", "申鹤", "砂糖", "神里绫人", "神里绫华", "罗莎莉亚", "胡桃", "芭芭拉", "荒泷一斗", "莫娜", "菲谢尔", "行秋", "诺艾尔", "辛焱", "达达利亚", "迪卢克", "迪奥娜", "重云", "钟离", "阿贝多", "雷泽", "雷电将军", "香菱", "魈", "夜兰", "久岐忍", "鹿野院平藏"]  # 角色名称列表
print("欢迎使用原神角色立绘爬虫脚本！\n\n作者：兄弟难当\n版本：1.0.7(64-bit)\n角色立绘共50张，采用分析官方wiki图片源的方式进行爬取\n已开始获取，这将花费您4分钟左右的时间。")

if not os.path.exists("角色立绘"):  # 判断是否存在文件夹，如不存在，继续
    os.mkdir("角色立绘")  # 新建文件夹

for i in range(0, len(chara_name_list)):
    URL = "https://bbs.hoyolab.com/hoyowiki/picture/character/" + chara_name_list[i] + "/avatar.png"  # 网址
    print("\n正在获取角色", chara_name_list[i], "的角色立绘……")  # 提示信息
    webPage_info = requests.get(URL)  # 初步定位网址中的信息
    webPage_info = webPage_info.content  # 将二进制信息(因为是图片)返回给变量，这里重复利用了变量 webPage_info ，用于节省内存
    doc_name = chara_name_list[i]+".png"  # 文件名称
    spritePage = open("角色立绘\\"+doc_name, "wb")  # 以二进制形式(因为是图片)的写入权限新创建(如已有，则覆盖其内容)一个 角色名.png 文件
    spritePage.write(webPage_info)  # 向文件 角色名.png 写入变量 webPage_info 中的内容(获取到的图片的二进制的信息码)
    spritePage.close()  # 将文件保存并关闭
    print("角色", chara_name_list[i], "的角色立绘", doc_name, "保存成功！")  # 提示信息
    if i == len(chara_name_list)-1:  # 如果是最后一个角色，则不等待
        pass
    else:  # 随机等待2~6秒的时间，防止被服务器禁IP
        num = random.randint(2, 6)
        print("\n等待",num,"秒，模拟真人手动操作，欺骗对方服务器……")
        for n in range(1, num + 1):
            time.sleep(1)
            print("已等待", n, "秒。")


input("\n全部保存成功！\n按Enter键退出……")  # 给用户查看进程日志的机会，让用户主动关闭窗口，而不是自动关闭
