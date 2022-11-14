from library import books
#вводим атора
def search():
    while True:
        author = input("Введите автора:")
        if author in books:
            writer = books[author]
        elif author not in books:
            print("Такого автора нет")
            continue

#вводим книгу
        book = input(("Введите книгу:"))
        if book not in writer:
            print("такой книги нет")
            continue
        for i, show in enumerate(writer):
            if book in writer[i]:
                print("Вот ваша книга")
                new = writer[i]
                writer[i] = new
                return show, author
                break

print(search())

def addbook():
    while True:
            user = input("Может хотите добавить книгу? Нажмите " "'add'" ", если хотите пропустить напишите " "'skip':")
            if user == "skip":
                break
            elif user == "add":
                added = input("Введи автора которого хочешь дополнить книгой")
                if added  not in books:
                    print("такого автора нет")
                    continue
                elif added in books:
                    bookadd = books[added]
                    addedbook = input("Введи книгу данного автора которую мы забыли указать")
                    if addedbook in bookadd:
                        print("Такая книга есть")
                    elif addedbook not in bookadd:
                            bookadd.append(addedbook)
                            print("Список книг обновлен,не веришь? Убедись сам :)")
                            print(bookadd)
           # print(added)
print(addbook())
def delete():
    while True:
        user = input("Может хотите удалить книгу? Нажмите " "'del'" ", если хотите пропустить напишите" "'skip':")
        if user == "skip":
            break
        elif user == "del":
            user = input("Введите автора книги которую хотим удалить")
            if user not in books:
                print("такого автора нет")
                continue
            elif user in books:
                bookdel = books[user]
                delbook = input("Введи книгу мы ее удалим")
                if delbook not in bookdel:
                    print("Увы, мы не можем удалить того, чего нет :)")
                elif delbook in bookdel:
                    bookdel.remove(delbook)
                    print("Список книг изменен")
                    print(bookdel)
print(delete())
def pop():
    while True:
        user = input("Хотите Выбрать другую книгу?")
        if user == "yes":
            print("А вы любите читать )")
            return search()
        elif user == "no":
            print("Приятного чтения")
            break
print(pop())



