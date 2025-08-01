from flask import Flask, request

app = Flask (__name__)

#create contacts
contacts = [{'id': '1','name': 'Shaun', 'phone': '123-456-7890'},
            {'id': '2', 'name': 'Jane', 'phone': '987-654-3210'},
           {'id': '3', 'name': 'John', 'phone': '555-555-5555'},
           {'id': '4', 'name': 'Alice', 'phone': '444-444-4444'}]

next_id = 5

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
  global next_id

  new_contact = {
    'id': f'{next_id}',
    'name': request.json['name'],
    'phone': request.json['phone']
  }

  next_id += 1
  contacts.append(new_contact)
  return new_contact, 201

@app.put('/contacts/<id>')
def update_contact(id):
  for contact in contacts:
    if contact['id'] == id:
      contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
      contact['phone'] - request.json['phone'] if 'phone' in request.json else contact['phone']
      return contact
    
    return 'That contact does not exist!', 404

@app.delete('/contacts/<id>')
def delete_contact(id):
   for contact in contacts:
     if contact['id'] == id:
       contacts.remove(contact)
       return f'Contact with id {id} has been deleted!', 200

   return 'There is no contact with that id!', 404

#GET /contacts - list all contacts
#GET /contacts/<id> - read a single contact by id
#POST /contacts - create a new contact
#PUT /contacts/<id> - update a contact by id
#DELETE /contacts/<id> - delete a contact by id

if __name__ == '__main__':
  app.run(debug=True)