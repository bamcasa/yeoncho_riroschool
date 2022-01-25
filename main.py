from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def Classify_body(tr_body):
    result = []
    td_list = tr_body.select("td")
    result.append(td_list[0].text)  # 순번

    temp_txt = td_list[1].text
    status = temp_txt[1:3] #마감 or 제출
    name = temp_txt[4:-1] #과제 제목
    result.append(status)
    result.append(name)

    teacher = td_list[2].text
    result.append(teacher) #선생님

    date = td_list[3].text #마감일짜
    result.append(date)

    submission_number = td_list[4].text
    result.append(submission_number)
    return result


with open("account.txt", "r") as f:
    lines = f.readlines()
    id = lines[0] # 아이디
    pw = lines[1] # 패스워드

# one_grade =


# 웹드라이버
# driver = webdriver.Chrome('webdriver/chromedriver.exe') #구버전
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://yeoncho.riroschool.kr/user.php"
driver.get(url)
driver.implicitly_wait(3)

# 로그인
driver.find_element(By.NAME, 'mid').send_keys(id)
driver.find_element(By.NAME, 'mpass').send_keys(pw)
driver.find_element(By.XPATH, '//*[@id="container"]/div/form/div/div[5]/a').click()

driver.find_element(By.XPATH, '//*[@id="container"]/div/div/ul/li[8]/em').click()
driver.find_element(By.XPATH, '//*[@id="container"]/div/div/ul/li[8]/ul/li[2]/span').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()
body = soup.select("#container > div > table.all-table.mt-5 > tbody > tr")
del body[0]

assignments = []

for title in body:
    temp = Classify_body(title)
    assignments.append(temp)
    print(temp)

# print(assignments)
