from msilib import schema
from unicodedata import name
from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

database_name = "API"
DB_URI = "mongodb+srv://Tester:Testing123@cluster0.blkhw2n.mongodb.net/?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)

class pep_small(db.Document):
    score = db.FloatField()
    id = db.StringField()
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
            "score": self.score,
           "id": self.id,
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



''' GET will return the person that is in the pep list'''

@app.route('/api/name', methods=['GET'])
def api_name():
   
   return make_response(jsonify(pep_small.objects.get(name = "Oleg SLIZHEVSKIY")),201)

   







if __name__ == '__main__':
    app.run()