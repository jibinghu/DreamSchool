from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # 导入TimeoutException
import sys

# 输入参数处理
date = sys.argv[1]  # 日期，格式为YYYYMMDD
currency = sys.argv[2]  # 货币代号，如USD

# 设置Selenium Webdriver
driver = webdriver.Edge() #使用edge浏览器，也可根据实际情况使用其他
driver.get("https://www.boc.cn/sourcedb/whpj/")

# print(currency)
# 将下拉菜单中英文代码与查询所需中文对应
currency_dict = {
    "GBP": "英镑",
    "HKD": "港币",
    "USD": "美元",
    "CHF": "瑞士法郎",
    "DEM": "德国马克",
    "FRF": "法国法郎",
    "SGD": "新加坡元",
    "SEK": "瑞典克朗",
    "DKK": "丹麦克朗",
    "NOK": "挪威克朗",
    "JPY": "日元",
    "CAD": "加拿大元",
    "AUD": "澳大利亚元",
    "EUR": "欧元",
    "MOP": "澳门元",
    "PHP": "菲律宾比索",
    "THB": "泰国铢",
    "NZD": "新西兰元",
    "KRW": "韩元",
    "RUB": "卢布",
    "MYR": "马来西亚林吉特",
    "TWD": "新台币",
    "ESP": "西班牙比塞塔",
    "ITL": "意大利里拉",
    "NLG": "荷兰盾",
    "BEF": "比利时法郎",
    "FIM": "芬兰马克",
    "INR": "印度卢比",
    "IDR": "印尼卢比",
    "BRL": "巴西里亚尔",
    "AED": "阿联酋迪拉姆",
    "ZAR": "南非兰特",
    "SAR": "沙特里亚尔",
    "TRY": "土耳其里拉"
}

try:
    # 等待日期输入框加载
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "nothing"))
    )

    # 输入日期
    date_input = driver.find_element(By.NAME, "nothing")
    date_input.clear()
    date_input.send_keys(date)
    
    # 选择货币
    currency_input = driver.find_element(By.ID, "pjname")
    currency_input.send_keys(currency_dict[currency])
    
    # 点击查询按钮
    search_button = driver.find_element(By.XPATH, "(//input[@type='button'])[2]")
    search_button.click()

    # 等待结果加载,并检测第一种异常
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='BOC_main publish']/table/tbody/tr[2]/td[4]"))
        )
    except TimeoutException:
        print("对不起，没有检索结果，请换其他检索词重试！")
        sys.exit()  # 终止程序运行



    # 获取现汇卖出价
    exchange_rate = driver.find_element(By.XPATH, "//div[@class='BOC_main publish']/table/tbody/tr[2]/td[4]").text
    
    # print(exchange_rate)
    # 第二种异常处理
    if exchange_rate:
        # 将数据写入result.txt文件中
        print(exchange_rate)
        with open("result.txt","w") as file:
            file.write(exchange_rate)
    else:
        print("当日现汇卖出价为空，请另寻日期！")

finally:
    driver.quit()
