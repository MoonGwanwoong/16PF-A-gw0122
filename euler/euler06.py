sum_square = 0
square_sum = 0
for a in range(1,101) :
    sum_square = sum_square + a
    square_sum = square_sum + a * a
sum_square = sum_square * sum_square
print "sum_square = ", sum_square
print "square_sum = ", square_sum
difference = sum_square - square_sum
print "sum_square - square_sum = " ,difference
