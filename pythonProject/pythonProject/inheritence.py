class books:
    @staticmethod
    def usage():
        print("I give you knowledge")
class physics(books):
    def specific_usage(self):
        print("I give You Knowledge about Science")
        self.price="420 Rs."
class maths(books):
    def specific_usage(self):
        print("I give you knowledge about mathematics")
        self.price="500 Rs."
c=physics()
c.usage()
c.specific_usage()
print(c.specific_usage())
