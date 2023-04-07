# CNKI-crawler

知网数据论文信息爬取

# 功能描述

可根据关键搜索爬去论文相关数据。可爬取的字段如下:

|中文名|题名|作者|来源|发表时间|数据库|被引数|下载数|
|-|-|-|-|-|-|-|-|
|csv文件对应名|title|author|source|date|data|quote|download|

# 准备工作（安装）

## 方式一：

首次运行时，需要完成 Python 虚拟环境的创建以及依赖库的安装。

在终端使用`install.bat`（windows）或`install.sh`（Linux, Mac）脚本进行自动安装，或者使用以下命令手动安装。

## 方式二：

**若使用了方式一安装请忽略该方法**

### 1.创建 Python 虚拟环境

使用下面的命令创建 Python 虚拟环境

```python
# (cnki_venv可自定义名字)
python -m venv cnki_venv
```

### 2.安装依赖

使用下面的命令安装依赖库

```
pip install -r requirements.txt
```

# 具体操作

在具体操作之前请确保上面的安装步骤已经完成。

## 配置文件 config.yaml

```yaml
keyword: 'xxxx'
page: 3
path: 'xxxxx'
```

参数解释:

    keyword: 搜索的论文关键字
    page: 爬取的论文页数
    path: 爬取的论文数据保存路径

## 程序运行

### 方式一:
在终端使用`run.bat`（windows）或`run.sh`（Linux, Mac）脚本进行自动安装，或者使用以下命令手动安装。

### 方式一:
```python
python cnki.py
```
