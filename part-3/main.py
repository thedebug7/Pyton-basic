for i in range(5):
    print("Check")
    print(i)

for i in range(3):
    print("Welcome to the Loop...")


for i in range(1, 10+1):
    print(i);

print()
count = 0
while count < 5+1:
    print(count)
    count = count + 1


print()


for num in range(1, 10):
    if num == 5:
        break
    print(num)


print()


for num in range(1, 10+1):
    if num == 5:
        continue
    print(num)


print()

tnum = int(input("Enter a number: "))
for num in range(1, 10+1):
    print(f'{tnum} * {num} = {tnum * num}')

print()
#   Sum of First N Natural Numbers

n = int(input("Enter a number: "))
sum = 0

for num in range(1, n+1):
    sum = sum + num

print(f"Sum of first {n} numbers: {sum}")


