import requests
import parsel

import pandas as pd

from config import config


data_list = []
SearchSql = []


def save_csv_file(datas_list, file_name):
    """保存为csv文件

    Args:
        datas_list (数据列表): 数据列表
        unique_id (str): csv文件名
        path (str): 保存的文件路径
    """
    df = pd.DataFrame(datas_list)
    df.to_csv(
        config["path"] + "/" + f"{file_name}.csv",
        mode="w",
        index=False,
        encoding="utf_8_sig",
    )


def parse_data(selector):
    """解析数据

    Args:
        selector (parsel.selector.Selector): selector对象
    """

    datas = selector.css(".result-table-list tr")
    for data in datas[1:]:
        title_re = data.css(" td.name a")
        if title_re.css("font::text"):
            text_content = title_re.xpath("string()").get().strip()
            font_content = title_re.css("font::text").get().strip()
            title = text_content + font_content
            title = title[:-2]
        else:
            title = title_re.css("::text").get().strip()
        if data.css(" td.author a::text"):
            author = data.css(" td.author a::text").getall()
        else:
            author = data.css(" td.author::text").get().strip()

        try:
            source = data.css(" td.source > a::text").get().strip()
        except:
            source = None
        date = data.css(" td.date::text").get().strip()
        data_o = data.css(" td.data::text").get().strip()
        quote = data.css(" td.name::text").get().strip()
        if not quote:
            quote = 0
        if data.css(" td.download a::text"):
            download = data.css(" td.download a::text").get().strip()
        else:
            download = 0
        data_dict = {"title": title, "author": author, "source": source, "date": date, "data": data_o, "quote": quote, "download": download}
        data_list.append(data_dict)


def request_data(data):
    """发送请求

    Args:
        data (dic): 构造的请求data

    Returns:
        parsel.selector.Selector): selector对象
    """
    url = "https://kns.cnki.net/KNS8/Brief/GetGridTableHtml"
    headers = {
        "Host": "kns.cnki.net",
        "Origin": "https://kns.cnki.net",
        "Referer": "https://kns.cnki.net/kns8/defaultresult/index",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    response = requests.post(url=url, headers=headers, data=data)
    html_text = response.text
    selector = parsel.Selector(html_text)
    parse_data(selector)
    return selector


def construct_data(subject_name):
    """构造请求data

    Args:
        subject_name (str): 搜索关键字

    Returns:
        dict: 构造的请求数据字典
    """
    data = {
        "IsSearch": "true",
        "QueryJson": '{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CJFN,CCJD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"'
        + subject_name
        + '","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
        "PageName": "DefaultResult",
        "DBCode": "SCDB",
        "KuaKuCodes": "CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CJFN,CCJD",
        "CurPage": "1",
        "RecordsCntPerPage": "20",
        "CurDisplayMode": "listmode",
        "CurrSortFieldType": "desc",
        "IsSentenceSearch": "false",
        "Subject": "",
    }
    return data


def run(subject_name, page):
    """程序启动

    Args:
        subject_name (str): 搜索关键字
        page (int): 爬去的页数
    """
    for i in range(1, page):
        print(f"正在获取第{i}页数据")
        if i == 1:
            data = construct_data(subject_name)
            selector = request_data(data)
            search = selector.css("#sqlVal").css("::attr(value)").get()
            SearchSql.append(search)
        else:
            data = construct_data(subject_name)
            data["IsSearch"] = False
            data["SearchSql"] = SearchSql[0]
            data["CurPage"] = str(i)
            data["HandlerId"] = "11"
            data["DBCode"] = "CFLS"
            request_data(data)


if __name__ == "__main__":
    run(config["keyword"], config["page"])
    save_csv_file(data_list, config["keyword"])
