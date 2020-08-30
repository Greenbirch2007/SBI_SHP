# -*- coding:utf-8 -*-
import datetime
import re
import time
import requests
from requests.exceptions import RequestException
import os
import pymysql

from lxml import etree
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import wget
import os
import urllib.request
import subprocess
from selenium import webdriver

def mkdir(path):
    # 引入模块
    import os

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')

        return False









def list_str(item):
    f =["".join(item)]
    return f



def removeDot(item):
    f_l = []
    for it in item:
        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l


def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into SBI_SHP (num_coding,num_industry,num_title,updateD,RT_confirmM,F_confirm,RT_URL,first_Content,first_STnum,first_Other) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass




if __name__=="__main__":
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    options = webdriver.ChromeOptions()

    # sql 语句 coding,industry,title
    for num in range(1, 3573):
        big_list = []
        sql = 'select * from js_infos_finanData where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        num_coding = data['coding']
        num_industry = data['industry']
        num_title = data['title']
        print(num_coding,num_industry,num_title)
        try:  # 解析就用

            url = 'https://www.sbisec.co.jp/ETGate/?_ControlID=WPLETsiR001Control&_PageID=WPLETsiR001Idtl60&_DataStoreID=DSWPLETsiR001Control&_ActionID=DefaultAID&s_rkbn=&s_btype=&i_stock_sec=&i_dom_flg=1&i_exchange_code=&i_output_type=5&exchange_code=TKY&stock_sec_code_mul={0}&ref_from=1&ref_to=20&wstm4130_sort_id=&wstm4130_sort_kbn=&qr_keyword=&qr_suggest=&qr_sort='.format(num_coding)

            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            selector = etree.HTML(html)
            updateD = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[1]/td/p/text()')
            RT_confirmM = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[2]/td/p/text()')
            F_confirm = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[3]/td/p/text()')
            RT_URL = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[4]/td/p/a/@href')

            first_Content = selector.xpath('//*[@id="main"]/div[8]/table/tbody/tr/td[1]/p/text()')
            first_STnum = selector.xpath('//*[@id="main"]/div[8]/table/tbody/tr/td[2]/p/text()')
            first_Other = selector.xpath('//*[@id="main"]/div[8]/table/tbody/tr/td[3]/div/p/text()')

            patt = re.compile('<img name="subimg\d+" src="(.*?)" width="77"', re.S)
            # 1.创建文件夹 2.将突破下载到文件夹中  3. 将文本保存成txt文件放到文件夹中
            # 都存到数据库算了，保存成txt文件有问题
            items = re.findall(patt, html)
            print(updateD, RT_confirmM, F_confirm, RT_URL, first_Content, first_STnum, first_Other)
            lpath = os.getcwd()
            f_intoDB = [num_coding]+[num_industry]+[num_title]+updateD+RT_confirmM+F_confirm+RT_URL+list_str(first_Content)+list_str(first_STnum)+list_str(first_Other)
            print(f_intoDB)
            if len(updateD+RT_confirmM)!=0:
                f_path = lpath + "/" + num_title + num_coding + num_industry

                mkdir(f_path)
                for img_url in items:
                    urllib.request.urlretrieve(img_url, '{0}/{1}.PNG'.format(f_path,
                                                                             num_title + num_coding + num_industry + img_url[
                                                                                                                     -6:]))
            else:
                pass
            # 遍历列表，替换[]为字符串
            f_intoDB =["" if i == [] else i for i in f_intoDB]
            print(f_intoDB)
            big_list_tuple = tuple(f_intoDB)
            finanl_content = []
            finanl_content.append(big_list_tuple)  # 是要带着元括号操作，
            print(finanl_content)
            insertDB(finanl_content)



        except:
            pass



#num_coding,num_industry,num_title,updateD,RT_confirmM,F_confirm,RT_URL,first_Content,first_STnum,first_Other
# create table SBI_SHP(
# id int not null primary key auto_increment,
# num_coding text,
# num_industry text,
# num_title text,
# updateD  text,
# RT_confirmM  text,
# F_confirm  text,
# RT_URL  text,
# first_Content  text,
# first_STnum  text,
# first_Other  text
# ) engine=InnoDB default charset=utf8;


