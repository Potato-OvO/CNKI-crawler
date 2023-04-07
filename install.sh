#!/bin/bash
echo "正在创建Python虚拟环境..."
python -m venv cnki_venv
echo "正在安装依赖库..."
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/
echo "请检查上方是否有错误，如果没有错误即可运行程序。"