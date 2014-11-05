class User:
    def __init__ (self, name):
        self.name = name
    def __repr__(self):
        return "User name = %s" % self.name
user = User("Tom")
print user