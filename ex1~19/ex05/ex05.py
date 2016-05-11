my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height_inch = 74.00 #inches
cm_to_inch = 1*2.54
my_height_cm = my_height_inch * cm_to_inch
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
height = my_height_inch*2.54

print "Let's talk about %r." % my_name
print "He's %r inches tall." % my_height_inch
print "And also he is %d centimeters tall." % height
print "AND also he is %r centimeters tall." % my_height_cm
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height_inch, my_weight, my_age + my_height_inch + my_weight)