score = input("Enter Score: ")

scr = float(score)

if scr < 0.0 or scr > 1.0:
    print("Error")
elif scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
elif scr < 0.6:
    print("F")    