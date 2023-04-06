import requests
import re
import parsel
import csv

# 构造请求参数
url = "https://kns.cnki.net/KNS8/Brief/GetGridTableHtml"
headers = {
    "Host": "kns.cnki.net",
    "Origin": "https://kns.cnki.net",
    "Referer": "https://kns.cnki.net/kns8/defaultresult/index",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
}
param = {}
# url列表
url_list = []
SearchSql = []


def Parsed_pages(subject_name, num):
    """
    解析需要爬取的所有的href连接，传参给get_url()
    :return:
    """
    for i in range(1, num):
        print(f"正在获取第{i}页数据")
        if i == 1:
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
                # 'CurrSortField': '%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27)',
                "CurrSortFieldType": "desc",
                "IsSentenceSearch": "false",
                "Subject": "",
            }
            response = requests.post(url=url, headers=headers, data=data)
            html_text = response.text
            # print("===", datas)
            selector = parsel.Selector(html_text)
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
                # print(title)
                if data.css(" td.author a::text"):
                    author = data.css(" td.author a::text").getall()
                else:
                    author = data.css(" td.author::text").get().strip()
                
                try:
                    source = data.css(' td.source > a::text').get().strip()
                except:
                    pass
                date = data.css(' td.date::text').get().strip()
                quote = data.css(' td.name::text').get().strip()
                if not quote:
                    quote = 0
                if data.css(" td.download a::text"):
                    download = data.css(' td.download a::text').get().strip()
                else:
                    download = 0
                print(title, author, source, date, quote, download)
            search = selector.css('#sqlVal').css('::attr(value)').get()
            SearchSql.append(search)
        else:
            data = {
                "IsSearch": "false",
                "SearchSql": SearchSql[0],
                "QueryJson": '{"Platform":"","DBCode":"CFLS","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"'
                + subject_name
                + '","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
                "PageName": "defaultresult",
                "HandlerId": "11",
                "DBCode": "CFLS",
                "KuaKuCodes": "CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN",
                "CurPage": str(i),
                "RecordsCntPerPage": "20",
                "CurDisplayMode": "listmode",
                "CurrSortField": "",
                "CurrSortFieldType": "desc",
                "IsSortSearch": "false",
                "IsSentenceSearch": "false",
                "Subject": "",
            }

            response = requests.post(url=url, headers=headers, data=data)
            html_text = response.text
            # print("===", datas)
            selector = parsel.Selector(html_text)
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
                # print(title)
                if data.css(" td.author a::text"):
                    author = data.css(" td.author a::text").getall()
                else:
                    author = data.css(" td.author::text").get().strip()
                
                try:
                    source = data.css(' td.source > a::text').get().strip()
                except:
                    pass
                date = data.css(' td.date::text').get().strip()
                quote = data.css(' td.name::text').get().strip()
                if not quote:
                    quote = 0
                if data.css(" td.download a::text"):
                    download = data.css(' td.download a::text').get().strip()
                else:
                    download = 0
                print(title, author, source, date, quote, download)


if __name__ == "__main__":
    # subject_name = input("输入要查询的论文主题名：")
    # num = int(input("输入爬取的页数（不要输入过多以免超出范围）："))
    # Parsed_pages(subject_name, num)
    import yaml

    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    print(config)
    Parsed_pages(config["keyword"], config["page"])
