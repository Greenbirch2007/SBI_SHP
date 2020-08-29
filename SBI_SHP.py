





# 需求：1.下载表格数据
# 2.下载图片
# 3. 下载文本
# -*- coding: utf-8 -*-

# 读取页面文本
# 按照标题，保存整个文本


# -*- coding:utf-8 -*-
import datetime
import re
import time
import requests
from requests.exceptions import RequestException

import pymysql

from lxml import etree
# from selenium import webdriver
#
# driver = webdriver.Chrome()


def get_first_page(url):
    # driver.get(url)
    # html = driver.page_source
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html= response.text
            selector = etree.HTML(html)
            name = selector.xpath('//*[@id="main"]/div[2]/div/table/tbody/tr/td[1]/h3/span[1]/text()')
            code = selector.xpath('//*[@id="main"]/div[2]/div/table/tbody/tr/td[1]/h3/span[2]/span/text()')
            updateD = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[1]/td/p/text()')
            RT_confirmM = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[2]/td/p/text()')
            F_confirm = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[3]/td/p/text()')
            RT_URL = selector.xpath('//*[@id="main"]/div[7]/table/tbody/tr[4]/td/p/a/@href')

            first_Content = selector.xpath('//*[@id="main"]/div[8]/table/tbody/tr/td[1]/p/text()')
            first_STnum = selector.xpath('//*[@id="main"]/div[8]/table/tbody/tr/td[2]/p/text()')
            first_Other = selector.xpath('//*[@id="main"]/div[8]/table/tbody/tr/td[3]/div/p/text()')

            patt = re.compile('<img name="subimg\d+" src="(.*?)" width="77"',re.S)
            items = re.findall(patt, html)
            print(html)


        return None
    except RequestException:
        return None














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



url ='https://www.sbisec.co.jp/ETGate/?_ControlID=WPLETsiR001Control&_PageID=WPLETsiR001Idtl60&_DataStoreID=DSWPLETsiR001Control&_ActionID=DefaultAID&s_rkbn=&s_btype=&i_stock_sec=&i_dom_flg=1&i_exchange_code=&i_output_type=5&exchange_code=TKY&stock_sec_code_mul=1333&ref_from=1&ref_to=20&wstm4130_sort_id=&wstm4130_sort_kbn=&qr_keyword=&qr_suggest=&qr_sort='
get_first_page(url)


