from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")

url = "https://www.baidu.com/"

driver.get("https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CAPJ&dbname=CAPJLAST&filename=HDJJ20220222005")
