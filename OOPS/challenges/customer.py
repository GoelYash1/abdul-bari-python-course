class Customer:
    def __init__(self,name, phoneno):
        self.name = name
        self.phoneno = phoneno

    def get_name(self):
        return self.name

    def get_phoneno(self):
        return self.phoneno

    def set_phoneno(self, newphoneno):
        self.phoneno = newphoneno

c1 = Customer('Yash Goel', 8168236961)

print("Name:",c1.get_name(),"\nPhone:", c1.get_phoneno())

c1.set_phoneno(8168236960)
print("New Phone:", c1.get_phoneno())
