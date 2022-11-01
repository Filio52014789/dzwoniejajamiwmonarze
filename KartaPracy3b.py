#zad 1
# for i in range(1, 31) :
#   print(i, end=" ")

#zad 2
# n = int(input())
# for i in range(n) :
#   print(i**2, end=" ")

#zad 3
# for i in range(1137,10000,379):
#   print(i, end=" ")

#zad 4
# for i in range(100,1000,5):
#   print(i, end=" ")
#   print("\n", "\n")
# for y in range(102,1000,6):
#   print(y, end=" ")
#   print("\n")
# for x in range(110,1000,11):
#   print(x, end=" ")
#   print("\n", "\n")

#zad 5
# n = int(input("Ile liczb wpiszesz?"))
# a = 0
# for i in range(n):
#   k = int(input())
#   a += k
#   print(a)

#zad 6
# k = int(input("Podaj liczbę parzystą"))
# suma = 0
# for i in range(0,2 * k,2) :
#   suma += i
# print(suma)
#zad 7
# m = int(input())
# for i in range(11,100,3):
#   print(i, end=" ")

#zad 8
W0 = int(input("Podaj kwotę wejściową "))
L = int(input("Podaj okres z dokładnością do pół roku "))
procent = 61
suma = W0 + procent
for i in range(W0,suma):
  print(i *L, end=" ")
#Zad 9
# n = int(input())
# suma = 0
# for i in range(21,n+1,100):
#   suma += i
# print(suma)
#Zad 10
# import math
# for i in range(1,1000):
#   if i % 10 == math.sqrt(i):
#     print(i)
#   elif i % 100 == math.sqrt(i):
#     print(i)