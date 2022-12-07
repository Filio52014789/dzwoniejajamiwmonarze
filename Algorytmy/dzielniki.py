# n = int(input())
# for i in  range(1, n+1) :
#   if n % i == 0:
#     print(i, end=" ")


# while True:
# n = int(input())
# licznik = 0 
# for i in range(2, n):
#   if n % i == 0:
#     licznik += 1

# if licznik == 0:
#   print("Liczba jest pierwsza")
# else:
#   print("Liczba nie jest pierwsza")
# znak = input("Chcesz kolejną liczbę? T/N")
# if znak == 'N':
#   break

# 2. Generowanie liczb pierwszych (w przedziale [p,q])
# p, q = int(input()), int(input())

# for j in range(p, q+1):
#     flaga = True
#     for i in range(2, j):
#       if j % i == 0:
#         flaga = False
#         break
#     if flaga == True:
#       print(j, end=" ")
# 3. Generowanie liczb pierwszych (pierwsze n liczb pierwszych)
# n = int(input("Podaj ile chcesz liczb pierwszych "))

# k = 2
# ilosc = 0
# while 1:
#     flaga = True
#     for i in range(2, k):
#       if k % i == 0:
#         flaga = False
#         break
#     if flaga == True:
#       print(k, end=" ")
#       ilosc = ilosc + 1
#     if ilosc == n:
#         break
#     k = k + 1