from model.new_contact_data import ContactData
from generator.group import random_string
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, arg=getopt.getopt(sys.argv[1:],"n:f:",["number of contacts", "file"])
except getopt.GetoptError as err:
    usage()
    sys.exit(2)

n=5
f= "data/contacts.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o== "-f":
        f=a

def random_phone(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters+ string.digits +string.punctuation+ " "*10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])+"@mail.ru"

testdata_contact = [ContactData(firstname="", lastname="", address="", email1="",
                email2="", email3="", homephone="", mobilephone="",
                workphone="", fax="")]+[
    ContactData(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10), address=random_string("address", 15),email1=random_email (20),email2=random_email( 25),email3=random_email( 35),homephone=random_phone( 15),mobilephone=random_phone( 15),workphone=random_phone(15),fax=random_phone(15) )
    for i in (range(5))]

file= os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata_contact))