# Crawling-knowledge-network-vanadium-titanium-paper-data
## 爬取知网钒钛论文数据：
###1、项目背景：
 &ensp; &ensp; &ensp;大数据环境下，海量的信息层出不穷，如何能在复杂的信息中能够高效快捷的寻找到有用的信息。
而网络爬虫技术能够自动收集、能够对网页数据进行抓取，提升了搜索引擎的能力。 该项目主要爬取知网论文数据，并将爬取的数据下载为.pdf格式的文件， 并通过爬取的论文数据分析数据并建立钒钛词库(只开源了爬虫部分) 

### 2、采用的技术：requests库，selenium库，ORM操作数据库，TF-IDF，jieba , 随机森林

### 3、主要功能（介绍网络爬虫）：搜索需要爬取的论文数据的关键字，并根据实际情况输入爬取的页数,下载文.pdf文件的格式
### 4、功能简述：  
>1、运行 thesisurlcrawling_db.py 或 thesisurlcrawling_dv.py(两者区别见具体操作①)后输入要爬取的论文的关键字如：“苹果”，并根据实际情况输入要爬取
>的页数（不要超过实际的页数）否则报错。并将爬取的论文URl保存到数据库 或 .csv文件。
><br> &ensp; &ensp; &ensp;注：网页结构随时会更改，该项目发布时可正常运行，如若代码不能运行，请结合实际情况更改代码，本人会不定期运行。另外该项目未设置代理ip，如若爬取过快可能会导致ip被封，建议爬取时每页间隔时间可设置稍微长点。  
> 
> 2、运行paperdownload.py后可将爬取的数据下载为.pdf文件
> <br>&ensp; &ensp; &ensp;注：下载时需要登录账号(该项目最不完美的地方)，如果是学生连入校园，该问题可解决！！！！！最好每篇论文之间下载的时间设置长点，避免一些输入验证码等反扒措施

### 5、操作步骤：
> 1、导入requirements.txt  
具体导入方法 pip install -r requriements.txt  
> 
>2、运行 thesisurlcrawling_db.py 或 thesisurlcrawling_dv.py  
> 注： ①thesisurlcrawling_db.py将爬取的论文地址存入数据库  
> &ensp; &ensp; &ensp; ②thesisurlcrawling_dv.py 将爬取的论文地址存入.csv文件  
> 
> 3、运行paperdownload.py下载论文
> <br>注：该.py文件运行可能chromedriver.exe版本与浏览器的版本不对应，请自行进去官网下载 https://registry.npmmirror.com/binary.html?path=chromedriver/

## 注：学习交流，不要用于商业爬取，该项目自开源了爬虫部分，其他部分未开源
  


