############ HOMEWORK #################
# 20 masala
'''
n = int(input("Sonlar sonini kiriting: "))
numbers = list(map(int, input("Sonlarni kiriting: ").split()))

result = []
for i in range(n - 1):
    if numbers[i] < numbers[i + 1]:
        result.append(numbers[i])
print(result)
'''

# 21 masala
'''
n = int(input("Elementlar sonini kiriting: "))
print("Elementlarni kiriting:")
ssorted = True
prev = int(input())
for i in range(1, n):
    curr = int(input())
    if prev > curr:
         ssorted = False
    prev = curr
if ssorted:
    print("true")
else:
    print("false")

'''

# 22 masala
# n = int(input("Elementlar sonini kiriting: "))
# print("Elementlarni kiriting:")
# is_sorted = True
# prev = int(input())
# for i in range(1, n):
#     curr = int(input())
#     if prev > curr:
#         is_sorted = False
#     prev = curr
# if is_sorted:
#     print("true")
# else:
#     print("false")


# 23 masala
'''
n = int(input("Sonlar sonini kiriting: "))
numbers = list(map(int, input("Sonlarni kiriting: ").split()))

buzgan = []
for i in range(1, n - 1):
    if not ((numbers[i - 1] < numbers[i] > numbers[i + 1]) or (numbers[i - 1] > numbers[i] < numbers[i + 1])):
        buzgan.append(numbers[i])
print("Qoidani buzgan elementlar:", buzgan)
'''

# 24 masala
'''
n = int(input("Sonlar sonini kiriting: "))
numbers = list(map(int, inp ut("Sonlarni kiriting: ").split()))

first= -1
last = -1

for i in range(n):
    if numbers[i] == 0:
        if first == -1:
            first_zero = i
        last_zero = i

if first != -1 and last != -1 and first != last:
    total = sum(numbers[first + 1:last])
    print("Yigindi:", total)
else:
    print("Nol orasida sonlar yoq.")
'''

# 25 masala
'''
print("Sonlarni bitta qatorga kiriting (bosh joy bilan ajratib):")
data = input().split()
n = len(data)

first_zero_found = False
nollar_orasidagi_sum = 0

for i in range(n):
    num = int(data[i])
    if num == 0:
        if first_zero_found:
            break
        first_zero_found = True
    elif first_zero_found:
        nollar_orasidagi_sum += num

if first_zero_found:
    print("Birinchi va oxirgi nol orasidagi yigindi:", nollar_orasidagi_sum)
else:
    print("Birinchi nol topilmadi.")

'''

# 26 masala
'''
print("n va k ni bosh joy bilan ajratib kiriting:")
data = input().split()
n = int(data[0])
k = int(data[1])

natija = 1
for i in range(k):
    natija *= n

print(f"{n} ning {k} darajasi:", natija)

'''

# 27 masala
'''
n = int(input("n ni kiriting: "))
for i in range(1, n + 1):
    natija = 1
    for j in range(i):
        natija *= n
    print(f"{n} ning {i} darajasi:", natija)

'''

# 28 masala
'''
n = int(input("n ni kiriting: "))
for i in range(n, 0, -1):
    natija = 1
    for j in range(i):
        natija *= n
    print(f"{n} ning {i} darajasi:", natija)

'''

# 29 masala
'''
k = int(input("Toplamlar sonini kiriting: "))
total_sum = 0
for i in range(k):
    print(f"{i + 1}-to‘plamni kiriting (elementlarni bosh joy bilan ajrating):")
    m = int(input("Toplamdagi sonlar sonini kiriting: "))
    for j in range(m):
        num = int(input())
        total_sum += num
print("Barcha sonlar yigindisi:", total_sum)
'''