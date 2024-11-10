hrs = input("Enter Hours:") # 40
rate = input("Enter Rate:") # 10.50

h = float(hrs)
r = float(rate)

pay = h * r 

if pay > 0:
    pay = pay + (1.5 * r) * float(5)
print(pay)
        