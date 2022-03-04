# yeoncho_riroschool
연초고 리로스쿨 페이지 불러오는 라이브러리 

## Requirements
Python 3.7  
beautifulsoup4 4.10.0  
requests 2.27.1

## Install
```
pip install yeoncho-riro
```
## example
```python
from riroschool import riroschool

id = 리로스쿨 아이디
pw = 리로스쿨 패스워드

rs = riroschool.riroschool(id, pw)

assignment_list = rs.recv_assignment(3,"국어") #3학년 국어 원격수업과제 불러오기
for i in assignment_list:
    print(i)

cs_list = rs.recv_creative_experience("창체","자율") #창체/수행|창의적 체험활동|자율활동 불러오기
for i in cs_list:
    print(i)

board_list = rs.recv_board("안내") #안내게시판 불러오기
for i in board_list:
    print(i)
```
## Documentation
[설명서](https://github.com/bamcasa/yeoncho_riroschool/blob/main/Document.md)를 봐주십시오.

## Mechanism
[작동원리](https://github.com/bamcasa/yeoncho_riroschool/blob/main/Document.md)를 봐주십시오.

## Author
음상훈  
combeesang@gmail.com

## As an aside
여담으로 고등학생 신분으로써의 마지막 프로젝트 일것같다.   
이제 앞으로 고3으로써 공부에 전념할 것으로 예상되므로 이 프로젝트를 마지막으로 근 1년간 프로그래밍에 손을 안 댈것같다.  
제작동기는 1년전 리로스쿨과 관련된 프로그램 아이디어가 있어 제작하고 싶었지만  
그때는 웹과 관련된 지식과 파이썬 관련 지식과 시간이 부족하여 제작을 못하였다.  
그래서 이번에 코로나로 인해 학교를 안가게 되어서 남는시간에 리로스쿨관련 라이브러리 제작하게 되었다.  
이제는 나와 같이 아이디어는 있지만 지식, 시간이 부족해서 못 만드는 상황이 나오지 않았으면 하기 때문이다.  
이 프로젝트는 내가 처음으로 도전해보는 파이썬 라이브러리 제작이다.  
파이썬 라이브러리 제작은 처음이어서 부족한점도 많고 라이브러리에 대한 설명도 부족한 점도 많지만 너그럽게 이해해주시길 바랍니다.
