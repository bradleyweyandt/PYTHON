for i in range(0,151):
    print(i)

for i in range(5,1001, 5):
    print(i)

for i in range(1,101):
    if i % 10 == 0:
        print("Coding")
    elif i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)

sum = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum += i
print(sum)

start_num = 2018
while start_num > 0:
    print(start_num)
    start_num -= 4

low = 2
high = 9
mult = 3

for i in range(low, high + 1):
    if i % mult == 0:
        print(i)