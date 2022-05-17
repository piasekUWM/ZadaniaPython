import numpy as np

#   # Zad_1
# a = 4 * (np.arange(1, 21))
# print(a)



#   # Zad_2
# a = np.arange(11, dtype='float')
# b = a.astype('int32')
# print(a)
# print(b)



#   # Zad_3
# def zad3(n):
#     a = np.arange(1, n*n+1)
#     a = a.reshape(n, n)
#     return(2**a)
# n = 2
# print(zad3(int(n)))



#   # Zad_4
# def zad4(n, i):
#     return np.logspace(1, i, num=i, endpoint=True, base=n)
# print(zad4(int(input("podaj n: ")), int(input("podaj i: "))))



#   # Zad_5
# def zad5(n):
#     a = np.arange(n, 0, -1)
#     print(a)
#     b = np.diag(a, k=2)
#     print(b)
# zad5(int(input("n: ")))



#   # Zad_7
# def zad7(n):
#     a = np.diag(np.linspace(2, 2, num=n, dtype=int))
#     for i in range(n - 1):
#         b = np.diag(np.linspace(2 * (i + 2), 2 * (i + 2), num=n, dtype=int), k=i + 1)
#         b = b[:n, :n]
#         c = np.diag(np.linspace(2 * (i + 2), 2 * (i + 2), num=n, dtype=int), k=-i - 1)
#         c = c[:n, :n]
#         a = a + b + c
#     return a
# print(zad7(int(input("n: "))))



#   # Zad_8
# def zad8(n, kierunek):
#     if n % 2 == 1:
#         print("Prosze wpisac parzyste n")
#     else:
#         if n < 0:
#             print("Prosze wpisac dodatnie n")
#         else:
#             a = np.arange(1, n * n + 1)
#             a = a.reshape(n, n)
#             print(a)
#             if kierunek == 'poziomo':
#                 print(a[:(n // 2)])
#                 print(a[(n // 2):])
#             if kierunek == 'pionowo':
#                 print(a[:, :(n // 2)])
#                 print(a[:, (n // 2):])
# zad8(int(input("n: ")), input("kierunek: "))



#   # Zad_9
# a1 = int(input("a1: "))
# r = int(input("r: "))
# n = a1 + 25 * r
# wynik = np.arange(a1, n, r)
# wynik = wynik.reshape(5, 5)
# print(wynik)
