import socket

dga = ['nbnmep.com', 'ovrngbmpcrhgovv.com', 'mja3mxbvakjjouxir0z.ru', 'nfpyijgtgff.com', 'bvxkqyylprbcroy.com']
legit = ['naver.com', 'google.com', 'daum.net', 'gmail.com', 'amazon.com']

for i in dga:
    print("=== DGA Query ===")
    dgaIP = socket.gethostbyname(i)
    print(i+" ==> "+dgaIP)


for i in legit:
    print("=== Legit Query ===")
    legitIP = socket.gethostbyname(i)
    print(i+" ==> "+legitIP)