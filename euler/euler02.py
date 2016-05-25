#-*-coding:cp949
fibo = [1,2]
n=0
while fibo[n] < 50 :
    fibo.append(fibo[n]+fibo[n+1])
    n = n+1

print fibo
