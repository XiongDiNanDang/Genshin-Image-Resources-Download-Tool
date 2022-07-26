# -*- coding:utf-8 -*-

# 作者：兄弟难当
# 版本：1.11.5
# 最早出品/开源时间：2022/7/22 14:22:00


import requests, time, random, os
from drawing import drawing
from card import card
from portrait import portrait
from talent import talent
from constellation import constellation
from costume import costume

text = "如果想获取角色立绘，请输入数字“1”后按下Enter(回车)键；\n如果想获取角色头像，请输入数字“2”后按下Enter(回车)键；\n如果想获取角色卡片，请输入数字“3”后按下Enter(回车)键；\n如果想获取角色天赋图标，请输入数字“4”后按下Enter(回车)键；\n如果想获取角色命之座图标，请输入数字“5”后按下Enter(回车)键；\n如果想获取角色衣装立绘，请输入数字“6”后按下Enter(回车)键；\n如果想直接退出，请输入数字“7”后按下Enter(回车)键。"
print(
    "欢迎使用原神图像资源爬虫！\n\n作者：兄弟难当。\n软件版本：1.11.5(64-bit)。\n采用分析官方wiki图片源的方式进行爬取。\n获取期间，请勿在窗口内点击，否则会使进程暂停。如发生误触或画面卡住，请尝试轻按Enter键。如仍无法解决，请重启程序。\n\n您想获取什么？\n" + text)
get_input = input("请输入：")

while True:
    if get_input == "1":
        drawing()
        print("\n全部保存成功！\n\n您还想获取什么？\n" + text)
        get_input = input("请输入：")

    if get_input == "2":
        portrait()
        print("\n全部保存成功！\n\n您还想获取什么？\n" + text)
        get_input = input("请输入：")

    if get_input == "3":
        card()
        print("\n全部保存成功！\n\n您还想获取什么？\n" + text)
        get_input = input("请输入：")

    if get_input == "4":
        talent()
        print("\n全部保存成功！\n\n您还想获取什么？\n" + text)
        get_input = input("请输入：")

    if get_input == "5":
        constellation()
        print("\n全部保存成功！\n\n您还想获取什么？\n" + text)
        get_input = input("请输入：")

    if get_input == "6":
        costume()
        print("\n全部保存成功！\n\n您还想获取什么？\n" + text)
        get_input = input("请输入：")

    if get_input == "7":
        break

    else:
        print("\n输入有误。")
        get_input = input("请重新输入：")
