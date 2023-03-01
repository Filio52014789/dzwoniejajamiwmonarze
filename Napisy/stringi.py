# s = input()
# L = list(s)
# print(s, L)
# L.sort()
# print(s,L)
# s = "".join(L)
# print(s,L)

s = input()
L = list(s)
R = list(s)
R.reverse()
if L == R:
  print("TAK")
else:
  print("Nie")