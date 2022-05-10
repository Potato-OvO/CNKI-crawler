import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_product(key):
    """搜索论文名"""
    driver.find_element_by_css_selector('#txt_SearchText').send_keys(key)
    driver.find_element_by_css_selector('.search-form div input.search-btn').click()

    driver.implicitly_wait(10)  # 隐式等待
    driver.maximize_window()  # 最大化浏览器


def drop_down():
    """模拟人去滚动鼠标向下浏览页面"""
    for x in range(1, 11, 2):
        time.sleep(0.5)
        j = x / 10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
    time.sleep(0.5)


def downPdf(url, count):
    print(f'第{count}个文件正在下载,该文件为{url}')
    try:
        driver.find_element_by_css_selector('#pdfDown').click()
        time.sleep(5)
    except:
        print("无该文献！！")


def readCsvList():
    with open('url地址1.csv', 'r') as f:
        reader = csv.reader(f)
        items = [item for item in reader]
        items = list(items)
        # items.pop(0)
        items = items[0:]
        # print(items)
        # print(len(items))
    return items


if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    # download.default_directory  selnium程序的下载地址位置
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'C:\Users\12241\OneDrive\浏览器下载地\googel\知网数据'}
    options.add_experimental_option('prefs', prefs)
    # options.add_argument('headless')  # 浏览器隐式启动  确认程序无误后可以关闭

    # 使用指定浏览器打开
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

    url_list = readCsvList()
    # print(url_list)
    count = 0
    for url in url_list[1:]:
        url = url[0]
        # print(url)
        count = count + 1
        driver.get(url)
        drop_down()
        downPdf(url, count)
    driver.quit()
