from riroschool import riroschool

with open("account.txt", "r") as f:
    lines = f.readlines()
    id = lines[0] # 아이디
    pw = lines[1] # 패스워드

rs = riroschool(id, pw)

assignment_list = rs.recv_assignment(2)
for i in assignment_list:
    print(i)