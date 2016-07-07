# __ involves name managling
# _ does the override.


class B:
    def __init__(self):
        self.__private = 0
    def _private_method(self):
        print('B.__private_method', self.__private)

    def public_method(self):
        self._private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1      # Does not override B.__private
    # Does not override B.__private_method()
    def _private_method(self):
        print('C._private_method')

c = C()
c.public_method()  #expected C._private_method

