import pymysql.cursors
from model.group import Group
from model.new_contact_data import ContactData

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home ,mobile, work, email,email2,email3, address from addressbook where deprecated is NULL")
            for row in cursor:
                (id,firstname,lastname,home,mobile,work,email,email2,email3, address) = row
                list.append(ContactData(id=str(id), firstname=firstname, lastname=lastname, email1=email,email2=email2, email3=email3, mobilephone=mobile, address=address, homephone=home,workphone=work))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()