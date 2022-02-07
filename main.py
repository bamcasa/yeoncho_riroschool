from bs4 import BeautifulSoup as bs
import requests

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

LOGIN_INFO = {
    'mid': id,
    'mpass': pw
}

# one_grade =

with requests.Session() as s:
    login_req = s.post('https://yeoncho.riroschool.kr/user.php', data=LOGIN_INFO)

    # print(login_req.status_code)

    post_one = s.get('https://yeoncho.riroschool.kr/portfolio.php?db=1553')
    soup = bs(post_one.text, 'html.parser')

body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tr")
print(len(body))
del body[0]
assignments = []

for title in body:
    temp = Classify_body(title)
    assignments.append(temp)
    print(temp)

# print(assignments)
