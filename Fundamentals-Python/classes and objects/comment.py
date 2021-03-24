class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment('user 1', 'I like this book')
print(comment.username)
print(comment.content)
print(comment.likes)


class Slido:
    def __init__(self,name, content, photo=None, likes=0, dislikes=0, date='now'):
        self.name = name
        self.content = content
        self.photo = photo
        self.likes = likes
        self.dislikes =dislikes
        self.date = date

    def present(self):
        return f'{self.name} -> {self.content} = {self.likes}/{self.dislikes}'

comment = Slido('Jhon','dobre sum')
comment.likes += 1
print(comment.present())