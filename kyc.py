from msilib import schema
from unicodedata import name
from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

username = "Test"
password = "Test123"
database = "API"

DB_URI = "mongodb+srv://{}:{}@cluster0.bsd7r3w.mongodb.net/{}?retryWrites=true&w=majority".format(username, password, database)
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine(app)


class pep_small(db.Document):
    _id = db.ObjectIdField()
    score = db.FloatField()
    pid = db.StringField()
    schema = db.StringField()
    name = db.StringField()
    aliases = db.StringField()
    birth_date = db.StringField()
    countries = db.StringField()
    identifiers = db.StringField()
    sanctions = db.StringField()
    phones = db.StringField()
    emails = db.StringField()
    dataset = db.StringField()
    last_seen = db.StringField()
    first_seen = db.StringField()
    
    
  
    def to_json(self):
        return {
           "_id": self._id,
           "score": self.score,
           "pid": self.pid,
           "schema": self.schema,
           "name": self.name,
           "aliases": self.aliases,
           "birth_date": self.birth_date,
           "countries": self.countries,
           "identifiers": self.identifiers,
           "sanctions": self.sanctions,
           "phones": self.phones,
           "emails": self.emails,
           "dataset": self.dataset,
           "last_seen": self.last_seen,
           "first_seen": self.first_seen
           
        }



'''GET name will return the whole list, returns all documents in the database'''

@app.route('/api/name', methods=['GET'])
def api_name():
    persons = []
    for person in pep_small.objects:
        persons.append(person)
    return make_response(jsonify(persons),200)

'''Returns a specific person identified by name from the database.'''
@app.route('/api/<name>', methods = ['GET'])
def api_person(name):
    found_name = pep_small.objects(name=name).first()
    if found_name:
        return make_response(jsonify(found_name),200)
    else:
        return make_response("Not found",404)






if __name__ == '__main__':
    app.run()