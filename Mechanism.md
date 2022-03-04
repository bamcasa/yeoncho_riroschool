# 작동원리
```python
from bs4 import BeautifulSoup as bs
import requests
import json

class riroschool:
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

        self.LOGIN_INFO = {
            "app": "user",
            "mode": "login",
            "userType": 1,
            "id": self.id,
            "pw": self.pw,
            "is_start": False
        }
```
- 입력받은 아이디와 비밀번호를 이용하여 json형식으로 post할때 같이 보낼 data를 만든다.
```python
        self.session = requests.Session()

        url = "https://yeoncho.riroschool.kr/ajax.php"
        login_req = self.session.post(url, data=self.LOGIN_INFO)

        response = json.loads(login_req.text)
        if login_req.status_code != 200:
            raise NameError('연결 오류')
        if response.get("result") != "success":
            raise NameError("비밀번호나 아이디가 틀림")
```
- session를 만들어 준후 https://yeoncho.riroschool.kr/ajax.php에 ```LOGIN_INFO```와 함께 post를 한다.
```python
    def Classify_body(self, tr_body, type):
        result = []
        if type == "portfolio":
            td_list = tr_body.select("td")
            result.append(td_list[0].get_text())  # 순번
            status = td_list[1].get_text()  # 마감 or 제출
            status = status.strip()
            result.append(status)

            name = td_list[2].get_text()  # 과제 제목
            name = name.strip()
            result.append(name)

            my_status = td_list[3].get_text()  # 내가 냈는지 안 냈는지
            my_status = my_status.strip()
            result.append(my_status)

            count = td_list[4].get_text()  # 제출 수
            count = count.strip()
            result.append(count)

            teacher = td_list[5].get_text()  # 선생님
            teacher = teacher.strip()
            result.append(teacher)

            date = td_list[6].text  # 마감일짜
            date = date.strip()
            start_date = date[0:11]
            finish_date = date[11:]

            result.append(start_date)
            result.append(finish_date)
```
- ```type```이 portfolio일경우 형식에 맞게 분할하여 ```result```라는 리스트 변수에 넣어 반환한다.
- 형식
  - ```[번호, 제출/마감, 글제목, 내가 제출한 게시물인지 아닌지, 제출자수, 선생님 이름, 게시일, 마감일]```
```python
        if type == "board":
            td_list = tr_body.select("td")

            # print(td_list[0].text)  # 번호
            number = td_list[0].get_text()
            result.append(number)

            temp = td_list[1].get_text()
            temp = temp.replace("\xa0","")
            finish = temp.rfind("\n")
            name = temp[1:finish]
            result.append(name)

            # print(td_list[3].text)  # 이름
            teacher = td_list[3].get_text()
            result.append(teacher)

            # print(td_list[4].text)  # 날짜
            date = td_list[4].get_text()
            result.append(date)

            # print(td_list[5].text)  # 조회
            count = td_list[5].get_text()
            result.append(count)
```
- ```type```이 board일경우 형식에 맞게 분할하여 ```result```라는 리스트 변수에 넣어 반환한다.
- 형식
  - ```[번호, 글제목, 선생님 이름, 게시일, 마감일]```
```python
        if type == "board_msg":
            td_list = tr_body.select("td")

            number = td_list[0].get_text()
            result.append(number)

            temp1 = td_list[1].select("a")
            temp1 = temp1[0].text
            status = temp1[0:2]
            result.append(status)


            finish = temp1.rfind("]")
            start = temp1.rfind("[")


            name = temp1[3:finish - (finish - start)]  # 제목
            result.append(name)

            count = temp1[start + 1:finish]
            result.append(count)

            teacher = td_list[3].text  # 선생님 이름
            result.append(teacher)

            views = td_list[4].text  # 조회수
            result.append(views)

            date = td_list[5].text  # 날짜
            result.append(date)

        return result
```
- ```type```이 board_msg일경우 형식에 맞게 분할하여 ```result```라는 리스트 변수에 넣어 반환한다.
- 형식
  - ```[번호, 제출/마감, 글제목, 제출수 , 선생님 이름, 조회수, 게시일, 마감일]```
