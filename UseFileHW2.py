import Homework2Question1 as usefile

print("The patient's score is ", 2,1,2,3,1,4,5,3)
print(usefile.superhealthyscore(2,1,2,3,1,4,5,3))
#output is 0.004373464883199951


#let's see if it works. Should give 1.000
print("This is a test score where all categories were 1. The patient's score is ", 1,1,1,1,1,1,1,1)
print(usefile.superhealthyscore(1,1,1,1,1,1,1,1))
#output is 1.0


#Should give 0.000?
print("This is a test score where all categories were 5 or 6 (whatever is max). The patient's score is ", 6,6,5,6,6,5,6,5)
print(usefile.superhealthyscore(6,6,5,6,6,5,6,5))
#it gave me -0.35902730636441177. What's going on?
