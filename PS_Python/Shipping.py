class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    # Local Scopre -> Defined variables on the init method
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

# Class Atributes
# Class atributes are shared within all instances of a particular class, example:
#class MyClass:
    # Class Atributes are defined here
#    class_attribute = "Something"
#    class_constant = "constant"

#    def __init__(self):
#        self.instance_attribute = "instante attribute"

#Class -> Global Scope
