import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient('mongodb+srv://Hajdu:renato@cluster0.4rfc7.mongodb.net/system?retryWrites=true&w=majority')

db = client.gettingStarted
people = db.people


personDocument = {
    "name": {"first": "Alan", "last": "Turing"},
    "birth": datetime.datetime(1912, 6, 23),
    "death": datetime.datetime(1954, 6, 7),
    "contribs": ["Turing machine", "Turing test", "Turingery"],
    "views": 1250000
}
people.insert_one(personDocument)

answer = input('Insert or export data? (I|E)')
if answer == 'I' or answer == 'i':
    fn = input('First name:')
    ln = input('Last name:')
    ge = input('Gender:')
    pw = input('Password:')
    new_data = {
        'fname': fn,
        'lname': ln,
        'gender': ge,
        'passw': pw
    }
    data.insert_one(new_data)
elif answer == 'E' or answer == 'e':
    for output in data.find():
        print(output)