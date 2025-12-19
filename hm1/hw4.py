class Contact:
    def __init__(self, name, phone_number, contact_id):
        self.name = name
        self.phone_number = phone_number
        self.id = contact_id

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Некорректный номер телефона")
        cls.last_id += 1
        contact = Contact(name, phone_number, cls.last_id)
        cls.all_contacts.append(contact)

    @classmethod
    def remove_contact(cls, contact_id):
        cls.all_contacts = [
            contact for contact in cls.all_contacts if contact.id != contact_id
        ]
