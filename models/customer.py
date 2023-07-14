class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, full_name, email):
        self.id = id
        self.full_name = full_name
        self.email = email
