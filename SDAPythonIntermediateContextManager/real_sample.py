user = 'Julia Roberts'

class Contact:

    def __init__(self, name, age, phone, address):
        pass

    def save(self):
        print("Saving the contact")

    def update(self):
        print("Updating the contact")


from contextlib import contextmanager

@contextmanager
def record_change(user, contact):
    print(f"User {user} started to change the contact {contact}")
    yield contact
    print(f"User {user} has changed the contact {contact}")


def create_contact():

    contact = Contact('Aecio', 23, '533293847', 'Liivalaia')

    with record_change(user, contact):
        contact.save()


def update_contact():

    contact = Contact('Aecio', 23, '533293847', 'Old town')

    with record_change(user, contact):
        contact.update()


update_contact()
