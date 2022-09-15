from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)

port = int(os.environ.get('PORT', 47046))

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

@app.route('/api/all', methods=['GET'])
def api_name():
    persons = []
    for person in pep_small.objects:
        persons.append(person)
    return make_response(jsonify(persons),200)


'''Return people belonging to certain datasets.'''
@app.route('/api/dataset/<dataset>', methods = ['GET'])
def api_dataset(dataset):
    found = pep_small.objects(dataset__icontains=dataset)
    if found: 
        return make_response(jsonify(found),200)
    else: 
        return make_response("Not found", 404)


'''Unspecific search for name, returns a person if a name contains something in the parameter. If nothing is found using get, you can add a document to the database with the name you searched for.'''
@app.route('/api/name/<name>', methods=['GET', 'POST'])
def api_uname(name):
    if request.method == "GET":
        found = pep_small.objects(name__icontains=name)
        if found:
            return make_response(jsonify(found),200)
        else: return make_response("404 Not found", 404)
    elif request.method == "POST":
        new_person = pep_small(
        pid = "",
        schema = "",
        name = name,
        aliases = "",
        birth_date = "",
        countries = "",
        identifiers = "",
        sanctions = "",
        phones = "",
        emails = "",
        dataset = "",
        last_seen = "",
        first_seen = ""
        )       
        new_person.save()
        return make_response("Success", 200)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)