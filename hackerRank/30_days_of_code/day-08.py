# n = int(input())
# name_numbers = [input().split() for i in range(n)]
# phone_book = {k: v for k,v in name_numbers}
# print(name_numbers)

# n = int(input())
# items = [input().split() for i in range(n)]
# dict = {k:v for k,v in items}
#
# while True:
#     try:
#         name = input()
#         if name in dict:
#             print('%s=%s'%(name,dict[name]))
#         else:
#             print("Not found")
#     except:
#         break


# print(dict)
n=int(input())
for i in range(n):
    l,r,a=map(int,input().split())
    ans = r//a + r%a
    m = r//a*a-1
    if l<=m:
        ans=max(ans,m//a+m%a)
    print(ans)



