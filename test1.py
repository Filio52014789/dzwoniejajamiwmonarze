# zad 1
# W= "GGGGEEETTWWWWWWHHH"  # 4G3E2T6W3H
# W += "."
# ilosc = 1
# H= ""
# for i in range (len(W)-1):
#     if W[i] == W[i+1]:
#         ilosc += 1
#     else:
#       if ilosc > 1:
#           H += str(ilosc)
#       H += W[i]
#       ilosc = 1
# print(H)

#zad 2
# a= int(input())
# b= int(input())
# c= int(input())
# d= int(input())
# from math import gcd
# nwd= gcd(b,d)
# print(nwd)


T = [50,20,10,5,2,1]
x = int(input())
for i in T:
  ilosc = x // i
  x = x - ilosc * i 
print(i,ilosc)