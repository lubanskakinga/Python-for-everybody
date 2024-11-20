text = "X-DSPAM-Confidence:    0.8475"
value = text.find("0")
f = float(text[value:])
print(f)