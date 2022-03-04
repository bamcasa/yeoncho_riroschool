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
- 로그인파트
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
```python
    def recv_assignment(self, grade, subject="전체", page=1):
        if grade == 1:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1552"
        elif grade == 2:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1553"
        elif grade == 3:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1554"
        else:
            raise NameError('학년이 맞지 않음')
```
- ```grade```의 값에 따라 맞는 웹사이트 주소로 변경
- ```grade```이 1,2,3이 아닐경우 에러
```python
        if subject != "전체":
            if subject == "korean" or subject == "국어":  # 국어
                url += "&t_doc=1"
                # print("국어")

            elif subject == "english" or subject == "영어":  # 영어
                url += "&t_doc=2"
                # print("영어")

            elif subject == "math" or subject == "수학":  # 수학
                url += "&t_doc=3"
                # print("수학")

            elif subject == "science" or subject == "과학":  # 과학
                url += "&t_doc=4"
                # print("과학")

            elif subject == "social" or subject == "사회":  # 사회
                url += "&t_doc=5"
                # print("사회")

            elif subject == "arts&sports" or subject == "예체능":  # 예체능
                url += "&t_doc=6"
                # print("예체능")

            elif subject == "technology" or subject == "정보기술":  # 정보기술
                url += "&t_doc=7"
                # print("정보기술")

            elif subject == "2stlanguage" or subject == "제2외국어":  # 제2외국어
                url += "&t_doc=8"
                # print("제2외국어")

            elif subject == "culture" or subject == "교양":  # 교양
                url += "&t_doc=9"
                # print("교양")
            else:
                raise NameError('알맞는 과목이 아님')
```
- ```subject```값에 맞는 웹사이트 주소로 변경
```python
        url += f"&page={page}"  # 페이지 추가
```
- ```page```값에 따라 웹사이트 주소 변경
```python
        post_one = self.session.get(url)
        soup = bs(post_one.text, 'html.parser')
        body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tr")
        del body[0]
```
- 웹사이트 주소로 get를 한후 bs4로 필요한 부분만 추출한다
- ```body[0]```은 필요없는 부분이어서 삭제한다.
```python
        assignments = []

        for title in body:
            temp = self.Classify_body(title, "portfolio")
            assignments.append(temp)

        return assignments
```
- 받은 과제들의 html들을 Classify_body함수에 넣는다.
- 즉 형식대로 분류를 하는 것이다.
- 원격수업과제방은 portfolio형식으로 되어있으므로 Classify_body함수의 인자로 "portfolio"를 넣는다.
- 그후 반환한다. 
```python
    def recv_creative_experience(self, activity, subject="전체", page=1):
        if activity == "창체" or activity == "creative":
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1502"
```
- ```activity```이 창체일경우
```python
            if subject != "전체":
                if subject == "autonomy" or subject == "자율":  # 자율
                    url += "&t_doc=1"

                elif subject == "volunteer" or subject == "봉사":  # 봉사
                    url += "&t_doc=2"

                elif subject == "club" or subject == "동아리":  # 동아리
                    url += "&t_doc=3"

                elif subject == "course" or subject == "진로":  # 진로
                    url += "&t_doc=4"

                elif subject == "reading" or subject == "독서":  # 독서
                    url += "&t_doc=5"

                elif subject == "competition" or subject == "기타교내대회":  # 기타교내대회
                    url += "&t_doc=6"

                elif subject == "curriculum" or subject == "공동교육과정":  # 공동교육과정
                    url += "&t_doc=7"
                else:
                    raise NameError('알맞는 과목이 아님')
```
- ```subject```의 값에 따라 웹사이트 주소 변경
```python
        elif activity == "수행" or activity == "performance":
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1551"
```
- ```activity```이 수행일경우
```python
            if subject != "전체":
                if subject == "korean" or subject == "국어":  # 국어
                    url += "&t_doc=1"
                    # print("국어")

                elif subject == "english" or subject == "영어":  # 영어
                    url += "&t_doc=2"
                    # print("영어")

                elif subject == "math" or subject == "수학":  # 수학
                    url += "&t_doc=3"
                    # print("수학")

                elif subject == "social" or subject == "사회":  # 사회
                    url += "&t_doc=4"
                    # print("사회")

                elif subject == "science" or subject == "과학":  # 과학
                    url += "&t_doc=5"
                    # print("과학")

                elif subject == "arts&sports" or subject == "예체능":  # 예체능
                    url += "&t_doc=6"
                    # print("예체능")
                else:
                    raise NameError('알맞는 과목이 아님')
```
- ```subject```의 값에 따라 웹사이트 주소 변경
```python
        else:
            raise NameError('창체/수행이 아님')
```
- ```activity```의 값이 올바르지 않을경우 에러
```python
        url += f"&page={page}"  # 페이지 추가
```
- 페이지 추가
```python
        post_one = self.session.get(url)
        # print(post_one)
        soup = bs(post_one.text, 'html.parser')
        body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tr")
        del body[0]
```
- 웹사이트 주소로 get를 한후 bs4로 필요한 부분만 추출한다
- ```body[0]```은 필요없는 부분이어서 삭제한다.
```python
        assignments = []

        for title in body:
            temp = self.Classify_body(title, "portfolio")
            assignments.append(temp)

        return assignments
```
- 받은 과제들의 html들을 Classify_body함수에 넣는다.
- 즉 형식대로 분류를 하는 것이다.
- 원격수업과제방은 portfolio형식으로 되어있으므로 Classify_body함수의 인자로 "portfolio"를 넣는다.
- 그후 반환한다. 
```python
    def recv_board(self, subject="", page=1):
        if subject == "안내":  # 안내
            url = "https://yeoncho.riroschool.kr/board.php?db=1001"
            type = "board"
        elif subject == "취합":  # 취합
            url = "https://yeoncho.riroschool.kr/board_msg.php?db=1901"
            type = "board_msg"
        elif subject.strip() == "1학년공지":  # 1학년 공지
            url = "https://yeoncho.riroschool.kr/board.php?db=2"
            type = "board"
        elif subject.strip() == "2학년공지":  # 2학년 공지
            url = "https://yeoncho.riroschool.kr/board.php?db=1"
            type = "board"
        elif subject.strip() == "3학년공지":  # 3학년 공지
            url = "https://yeoncho.riroschool.kr/board.php?db=1002"
            type = "board"
        elif subject == "진로진학":  # 진로진학
            url = "https://yeoncho.riroschool.kr/board_msg.php?db=1905"
            type = "board_msg"
        elif subject == "요청게시판":  # 요청게시판
            url = "https://yeoncho.riroschool.kr/board_msg.php?db=1903"
            type = "board_msg"
        elif subject == "수업자료":  # 수업자료
            url = "https://yeoncho.riroschool.kr/board.php?db=3"
            type = "board"
        else:
            raise NameError('알맞는 과목이 아님')
```
- ```subject```에 따라 웹사이트 주소 변경
- ```subject```이 올바르지 않으면 에러
```python

        url += f"&page={page}"  # 페이지 추가
        # print(url)
        post_one = self.session.get(url)
        # print(post_one.text)
        soup = bs(post_one.text, 'html.parser')
        body = soup.select("#container > div.container_inner > table > form > tr > td > table.all-table > tr")
        # print(body)
        del body[0]
        boards = []
        for title in body:
            temp = self.Classify_body(title, type)
            boards.append(temp)

        return boards
```
