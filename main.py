from riroschool import riroschool

with open("account.txt", "r") as f:
    lines = f.readlines()
    id = lines[0] # 아이디
    pw = lines[1] # 패스워드

rs = riroschool(id, pw)

# assignment_list = rs.recv_assignment(3,"과학",1)
#
# for i in assignment_list:
#     print(i)
#
# li = rs.recv_creative_experience("창체","자율",1)
# for i in li:
#     print(i)


# li2 = rs.recv_board("안내",1)
# for i in li2:
#     print(i)


