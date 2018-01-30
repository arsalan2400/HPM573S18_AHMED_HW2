import Homework2Question1 as usefile

print("The patient's score is ", 2,1,2,3,1,4,5,3)
print(usefile.superhealthyscore(2,1,2,3,1,4,5,3))
#output is 0.004373464883199951


#let's see if it works. Should give 1.000
print("This is a test score where all categories were 1. The patient's score is ", 1,1,1,1,1,1,1,1)
print(usefile.superhealthyscore(1,1,1,1,1,1,1,1))
#output is 1.0
