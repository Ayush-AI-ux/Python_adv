# a = list(input())
# a = a[::-1]
# print(a)
# for i in range(len(a)):
#     if i<len(a) and a[i] > a[i+1]:
#         i = i+1
#         b = a[:i]
#         m = min(b)
#         b.remove(m)
#         a = [a[i]] + b[:-1] + [m] + [b[-1]] + a[i+1:]
#         a = a[::-1]
# #         break
# # s = ""
# # for i in a:
# #     s += str(i)
# # print(s)

# n= input().split()
# print(n)

# n=input()
# y=n[::-1]
# print((y==n) * "Palindrome" + (y!= n) * "Not a palindrome")

def bintodec(binary):
    decimal =0
    power=0
    while binary>0:
        l_digit = binary % 10
        decimal += l_digit * (2 ** power)
        binary //=10
        power +=1
    return decimal
l=[]
n=int(input())
for i in range(n):
    binary = int(input())
    l.append(bintodec(binary))

for i in l:
    print(i)

    