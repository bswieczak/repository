import re

class InvalidEmail(Exception):
    pass

class EmailContainer:
    __regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    emails = None

    def __init__(self, email):
        self.valid(email)
        self.emails.append(email)

    def valid(self, email):
        if self.__regex.search(email) is not None:
            return email
        else:
            raise InvalidEmail('Podany email jest nie zgodny ze standardami')



test = EmailContainer("123@test.pl")

print(test.emails)
