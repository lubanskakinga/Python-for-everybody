def computepay():
    if hrs != 0 :
        pay = h * r # 420
    return pay

hrs = input("Enter Hours:") # 40
rate = input("Enter Rate:") # 10.50

h = float(hrs)
r = float(rate)

p = computepay() + (1.5 * r) * float(5)
print("Pay", p)