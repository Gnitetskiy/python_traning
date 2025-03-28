from sys import maxsize

class ContactData:
    def __init__(self, firstname=None, lastname=None, address=None, email1=None, email2=None, email3=None, homephone=None, mobilephone=None, workphone=None, fax=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname  and self.firstname==other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

