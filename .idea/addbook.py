from library import books as b

def search():
    n = input("Введите автора:")
    if n in b:
        author = b[n]
        print(author)
print(search())
def add():
        a = input("vvedite book")
        if a in author:
            print("такая книга есть")
        elif a not in author:
            author.append(a)
            return author
        else:
            print("u vas hui v jope")
print(search())