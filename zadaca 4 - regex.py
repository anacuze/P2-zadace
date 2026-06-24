import re

regex = r"^M(?=.*[0-5])(?=.*\s).*T$"

tekst = input("Unesi string: ")

if re.match(regex, tekst):
    print("Podudaranje postoji")
else:
    print("Nema podudaranja")
