import re

regex = r"^A(?=.*[0-5])(?=.*\s).*C$"

tekst = input("Unesi string: ")

if re.match(regex, tekst):
    print("Podudaranje postoji")
else:
    print("Nema podudaranja")
