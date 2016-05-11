#-*-coding:cp949
#http://euler.synap.co.kr/prob_detail.php?id=1

#10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
#1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

sum = 0

for a in range(1, 1000) :
    if a%3 == 0 :
        print "There is %d!!" %a
        sum = sum + a
        print "Now sum is %d" %sum
    elif a%5 == 0 :
        print "There is %d!!" %a
        sum = sum + a
        print "Now sum is %d" %sum

print "Finally, Sum is %d" %sum
