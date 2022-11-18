from library import books
def search():
    #search writer
    writersearch = input("Введите автора")
    if writersearch in books:
        author = books[writersearch]
        print("Такой автор есть")
    else:
        return "Такого автора нет"
    booksearch = input("Введите книгу")
    if booksearch not in author:
        return  "Такой книги нет"
    for i, show in enumerate(author):
        if booksearch in author[i]:
            print("Такая книга есть")
            new = author[i]
            author[i] = new
        return show, writersearch
print(search())
from library import books
def add():
    while True:
        user1 = input("Введите 'da' если хотите добавить или 'net' если не хотите?")
        if user1 == "net":
            break
        elif user1 == "da":
            writersearch = input("Введите автора")
            if writersearch in books:
                author = books[writersearch]
            elif writersearch not in books:
                print("Такого автора нет, выбретие автора из настоящего списка")
                continue
            user = input("введи книгу")
            if user in author:
                print("Книга есть")
                continue
            elif user not in author:
                for i, show in enumerate(author):
                    if user not in author[i]:
                        new = author[i]
                        author[i] = new
                        author.append(user)
                        print("Книга добавлена")
                        print(author)
                        break
print(add())
from library import books
def delete():
    while True:
        user1 = input("Хотите удалить книгу 'da' или 'net' ")
        if user1 == "net":
            break
        elif user1 == "da":
            writersearch = input("Введите автора")
            if writersearch in books:
                author = books[writersearch]
            elif writersearch not in books:
                print("Такого автора нет, выбретие автора из настоящего списка")
                continue
            bookdel = input("Введите книгу автора")
            for i, show in enumerate(author):
                if bookdel not in author:
                    print("такой книги нет")
                    break
                elif bookdel in author[i]:
                    new = author[i]
                    author[i] = new
                    author.remove(bookdel)
                    print("книга удалена")
                    print(author)
                    break
print(delete())
from library import books
def addauthor():
    user = input("Хотите ли добавить автора?")
    if user == "da":
        author = input("Введите автора которого хотите добавить")
        if author in books:
            return "Такой автора уже сть"
        elif author not in books:
            books[author] = []
            print(books.keys())
print(addauthor())
def repeat():
    user = input("может хотите выбрвть другую книгу?")
    if user == "da":
        return search()
    if user == "net":
        print("Приятного чтения")
print(repeat())
















