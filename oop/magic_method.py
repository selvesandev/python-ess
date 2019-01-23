class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return 100

    def __del__(self):
        print('You deleted Book object')


b = Book('Python', 'Selvesan')
print(b)

print(len(b))

del b
