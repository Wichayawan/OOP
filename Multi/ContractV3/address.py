class AddressHolder:
    def __init__(self, street, province, city, code):
        self.street = street
        self.province = province
        self.city = city
        self.code = code

    def __str__(self):
        return (
            f"Address:\n\tStreet: {self.street}\n\tProvince: {self.province}"
            f"\n\tCity: {self.city}\n\tCode: {self.code}"
        )

if __name__ == "__main__":
    a1 = AddressHolder("No Road", "Kamalasai", "Kalasin", "46000")
    print(a1)