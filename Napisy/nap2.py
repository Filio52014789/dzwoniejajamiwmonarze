a = input()
b = input()
X, Y = list(a), list(b)
X.sort()
Y.sort()
a = "".join(X)
b = "".join(Y)
if a == b:
  print("TAK")
else: 
  print("NIE")

#anagramy przez tablice
a = input()
b = input()
X = [0] * 200
Y = [0] * 200
for i in range(len(a)):
  X[ord(a[i])] += 1
for j in range(len(b)):
  Y[ord(b[j])] += 1
if X == Y:
  print("TAK")
else: 
  print("NIE")


# zad 1
# s = input()
# print(a[0], a[-1])
# print(a[0], a[len(a)-1])

#zad 2
# b = input()
# for i in range(1, len(b)-1):
#   print(b[i], end="")
# print()

#zad 3
c = input()
L = list(c)
L.reverse()
c = "".join(L)
print(c[:4])
