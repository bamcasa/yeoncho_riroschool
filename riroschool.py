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

        self.session = requests.Session()

        url = "https://yeoncho.riroschool.kr/ajax.php"
        login_req = self.session.post(url, data=self.LOGIN_INFO)

        response = json.loads(login_req.text)
        if login_req.status_code != 200:
            raise NameError('연결 오류')
        if response.get("result") != "success":
            raise NameError("비밀번호나 아이디가 틀림")

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

        if type == "board":
            pass

        return result

    def recv_assignment(self, grade, subject="전체", page=1):
        if grade == 1:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1552"
        elif grade == 2:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1553"
        elif grade == 3:
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1554"
        else:
            raise NameError('학년이 맞지 않음')

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

        url += f"&page={page}"  # 페이지 추가

        post_one = self.session.get(url)
        # print(post_one)
        soup = bs(post_one.text, 'html.parser')
        body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tr")
        del body[0]
        assignments = []

        for title in body:
            temp = self.Classify_body(title)
            assignments.append(temp)

        return assignments

    def recv_creative_experience(self, activity, subject="전체", page=1):
        if activity == "창체" or activity == "creative":
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1502"
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

        elif activity == "수행" or activity == "performance":
            url = "https://yeoncho.riroschool.kr/portfolio.php?db=1551"

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
        else:
            raise NameError('창체/수행이 아님')

        url += f"&page={page}"  # 페이지 추가

        post_one = self.session.get(url)
        # print(post_one)
        soup = bs(post_one.text, 'html.parser')
        body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tr")
        del body[0]
        assignments = []

        for title in body:
            temp = self.Classify_body(title)
            assignments.append(temp)

        return assignments

    def recv_board(self, subject="", page=1):
        if subject == "안내":  # 안내
            url = "https://yeoncho.riroschool.kr/board.php?db=1001"
        elif subject == "취합":  # 취합
            url = "https://yeoncho.riroschool.kr/board_msg.php?db=1901"
        elif subject.strip() == "1학년공지":  # 1학년 공지
            url = "https://yeoncho.riroschool.kr/board.php?db=2"
        elif subject.strip() == "2학년공지":  # 2학년 공지
            url = "https://yeoncho.riroschool.kr/board.php?db=1"
        elif subject.strip() == "3학년공지":  # 3학년 공지
            url = "https://yeoncho.riroschool.kr/board.php?db=1002"
        elif subject == "진로진학":  # 진로진학
            url = "https://yeoncho.riroschool.kr/board_msg.php?db=1905"
        elif subject == "요청게시판":  # 요청게시판
            url = "https://yeoncho.riroschool.kr/board_msg.php?db=1903"
        elif subject == "수업자료":  # 수업자료
            url = "https://yeoncho.riroschool.kr/board.php?db=3"
        else:
            raise NameError('알맞는 과목이 아님')

        url += f"&page={page}"  # 페이지 추가

        post_one = self.session.get(url)
        # print(post_one)
        soup = bs(post_one.text, 'html.parser')
        body = soup.select("#container > div > div.renewal_wrap.portfolio_wrap > table > tr")
        del body[0]
        boards = []
        for title in body:
            temp = self.Classify_body(title)
            boards.append(temp)

        return boards
