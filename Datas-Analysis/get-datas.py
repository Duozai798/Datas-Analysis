# -*- coding: utf-8 -*-
# @Time : 2023/3/13 9:18
# @Author : Ding Jun Ming

from bs4 import BeautifulSoup
import requests
import re
import os

class get_datas():
    @staticmethod
    def douban_top250_mine():
        for start_num in range(0,250,25):
            # 自定义请求头(模仿浏览器发出的请求)） 程序发出的请求服务器拦截
            header = {"user-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
            response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers = header)
            content = BeautifulSoup(response.text , 'html.parser')   # html.parser:指定解析器，解析HTML内容
            # content就是BeautifulSoup类的实例对象 实例.方法可以调用BeautifulSoup类方法
            # print(content.p)          # 返回第一个p标签，即文本段落元素，包括p元素下所有标签
            # print(content.img)        # 返回一个图片存放路径

            # BeautifulSoup对象的find_all方法：根据标签，类找出所有符合条件的元素 并返回一个可迭代对象
            movie_name = content.findAll("span",attrs = {'class' : 'title'})       # 参数：标签名，条件(字典形式 如类='title')
            movie_name_li = []
            for name in movie_name:
                movie_name_li.append(name.string)       # 只提取标签中string属性的内容添加到列表
            # print(bool(re.search('/', '霸王别姬')))
            for i in movie_name_li:
                if re.search(r'/',i):                   # 正则匹配去除外语电影名
                     movie_name_li.remove(i)
                else:
                    continue
            print(len(movie_name_li),movie_name_li)     # 打印电影数量与电影名

            for item in movie_name_li:
                print(f'豆瓣评分TOP250的电影是:{item}')

    @staticmethod
    def douban_top250_bilibili():
        for start_num in range(0,50,25):
            header = {"user-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
            response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers = header)
            content = BeautifulSoup(response.text , 'html.parser')   # html.parser:指定解析器，解析HTML内容
            movie_name = content.findAll("span",attrs = {'class' : 'title'})
            for name in movie_name:
                title = name.string
                if '/' not in title:
                    print(f'豆瓣评分TOP250的电影是:{title}')

    # html页面标签没有共性的内容 例如：a标签 即文件存放路径 a标签属性值不一样
    @staticmethod
    def get_label_a():
        res = requests.get("http://books.toscrape.com/").text
        soup = BeautifulSoup(res , 'html.parser')
        book_titles = soup.findAll("h3")         # 检查网页所需元素a在同一标签h3下
        for title in book_titles:
            items = title.findAll('a')           # 将提取的h3元素再次循环 提取a元素
            for i in items:
                print(i.string)                  # 最后提取a元素的文字内容
