class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_self = False

    def send(self):
        self.is_self = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_self}'


emails = []
line = input()
while line != 'Stop':
    em = line.split(' ')
    email = Email(em[0], em[1], em[2])
    emails.append(email)
    line = input()
index_of_send_emails = list(map(lambda x: int(x), input().split(', ')))
for index in index_of_send_emails:
    emails[index].send()
for email in emails:
    print(email.get_info())
