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

rs = riroschool(id, pw)

assignment_list = rs.recv_assignment(3,"국어") #3학년 국어 원격수업과제 불러오기
for i in assignment_list:
    print(i)

cs_list = rs.recv_creative_experience("창체","자율") #창체/수행|창의적 체험활동|자율활동 불러오기
for i in list:
    print(i)

board_list = rs.recv_board("안내") #안내게시판 불러오기
for i in board_list:
    print(i)
```
## Documentation


## Author
음상훈  
combeesang@gmail.com
