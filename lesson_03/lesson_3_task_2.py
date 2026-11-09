from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro Max", "+79876543210"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79123456789"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79012345678"),
    Smartphone("Huawei", "P60 Pro", "+79876543211"),
    Smartphone("Google", "Pixel 8", "+79123456780")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
