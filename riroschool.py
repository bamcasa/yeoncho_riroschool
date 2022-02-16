from bs4 import BeautifulSoup as bs
import requests

class riroschool:
    def __init__(self,id,pw):
        self.id = id
        self.pw = pw

        self.LOGIN_INFO = {
            'mid': self.id,
            'mpass': self.pw
        }

    def Classify_body(self,tr_body):
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

    def recv_assignment(self,grade):
        if grade == 1:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1552"
        elif grade == 2:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1553"
        elif grade == 3:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1554"
        else:
            raise NameError('not grade')
        with requests.Session() as s:
            login_req = s.post('https://yeoncho.riroschool.kr/user.php', data=self.LOGIN_INFO)
            if login_req.status_code != 200:
                raise NameError('login error')

        post_one = s.get(url)
        soup = bs(post_one.text, 'html.parser')
        body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tr")
        del body[0]
        assignments = []

        for title in body:
            temp = self.Classify_body(title)
            assignments.append(temp)

        return assignments
