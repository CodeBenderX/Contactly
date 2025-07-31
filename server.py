from flask import Flask, request

app = Flask (__name__)

#create contacts
contacts = [{'id': '1','name': 'Shaun', 'phone': '123-456-7890'},
            {'id': '2', 'name': 'Jane', 'phone': '987-654-3210'},
           {'id': '3', 'name': 'John', 'phone': '555-555-5555'},
           {'id': '4', 'name': 'Alice', 'phone': '444-444-4444'}]

@app.get('/contacts')
def list_contacts():
  return {'contacts': contacts}

@app.get('/contacts/<id>')
def read_single_contact(id):
  for contact in contacts:
    if contact['id'] == id:
      return contact
    
  return 'That contact does not exist!', 404

@app.post('/contacts')
def create_contact():
  print(request.json)
  return 'Thank you for the data!'

#GET /contacts - list all contacts
#GET /contacts/<id> - read a single contact by id
#POST /contacts - create a new contact

if __name__ == '__main__':
  app.run(debug=True)