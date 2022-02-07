from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def Classify_body(tr_body):
    result = []
    td_list = tr_body.select("td")
    result.append(td_list[0].get_text())  # 순번
    status = td_list[1].get_text() #마감 or 제출
    status = status.strip()
    result.append(status)

    name = td_list[2].get_text() #과제 제목
    name = name.strip()
    result.append(name)

    my_status = td_list[3].get_text() #내가 냈는지 안 냈는지
    my_status = my_status.strip()
    result.append(my_status)

    count = td_list[4].get_text() #제출 수
    count = count.strip()
    result.append(count)

    teacher = td_list[5].get_text() #선생님
    teacher = teacher.strip()
    result.append(teacher)

    date = td_list[6].text #마감일짜
    date = date.strip()
    result.append(date)

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

driver.find_element(By.XPATH, '//*[@id="popnoti_noti"]/div/div/a[2]').click()

driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/ul/li[8]/em').click()
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/ul/li[8]/ul/li[2]/span').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()
body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tbody > tr")
print(len(body))
del body[0]
assignments = []

for title in body:
    temp = Classify_body(title)
    assignments.append(temp)
    print(temp)

# print(assignments)
