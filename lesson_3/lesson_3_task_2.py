from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iphone 14", "+79011999999")
phone2 = Smartphone("Samsung", "Galaxy S23", "+79022999999")
phone3 = Smartphone("Xiaomi", "Redmi note 12", "+79033999999")
phone4 = Smartphone("Poco", "C 40", "+79044999999")
phone5 = Smartphone("Google", "Pixel 7", "+79055999999")

catalog. appened(phone1)
catalog. appened(phone2)
catalog. appened(phone3)
catalog. appened(phone4)
catalog. appened(phone5)

for phone in catalog:
    print(f"{phone.brand} {phone.model} - {phone.phone_number}")

