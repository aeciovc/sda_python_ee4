
class Contact:

    def __init__(self, name, home_phone=None, mobile_phone=None, email=''):

        if home_phone is None and mobile_phone is None:
            raise ValueError

        if not home_phone.startswith('+372'):
            raise ValueError

        if '@' in email:
            self.email = email
        else:
            self.email = ''
