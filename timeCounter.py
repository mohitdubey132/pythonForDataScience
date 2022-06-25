from time import time
import emoji
start = time()

print(start)

n = 1
skill=10
while n==1:
    print(n)
    skill*=2
    print(skill)

    n =n+1

# Python program to create acronyms
word = "Artificial Intelligence:h:"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)
c=1
while c<=500:
    print(emoji.emojize(":books::red_heart:"))