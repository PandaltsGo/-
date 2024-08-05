import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 获取网页地址
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
path=Service('D:\\Program_tools\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=path)
driver.get(url)
#查询条件
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/select/option[2]').click()
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[6]/div[2]/select/option[3]').click()
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[8]/a[1]').click()
#获取总页数
paper_need = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/ul/li[1]/span/span').text
paper_need = int(paper_need)
paper_num = 1

while paper_num < paper_need+1:
    #获取每页长度
    title_list = driver.find_element(By.XPATH,'//*[@id="sheet-bond-market"]/div[1]/div/table/tbody/tr[last()]')
    value=title_list.get_attribute("data-row")
    value=int(value)

    for i in range(1,value+1):
        ISIN = driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td/span/a').text
        Bond_Code = driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[2]/span/a').text
        issure= driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[3]/span').text
        Bond_Type = driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[4]/span').text
        Issue_Date = driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[5]/span').text
        Latest_Rating = driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[6]/span').text
        res = f"{ISIN},{Bond_Code},{issure},{Bond_Type},{Issue_Date},{Latest_Rating}".replace(
            "\n", "") + "\n"
        with open(f'data.csv', 'a', encoding='gbk') as f:#写入csv文件
            f.write(res)
        print(res)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a').click()
    time.sleep(1)
    paper_num += 1

time.sleep(500000)
driver.back()
