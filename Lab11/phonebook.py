import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="2006",
    port=5432
)
cur = conn.cursor()

def inputData():
    name = input("Введите ваше имя: ")
    number = input("Введите ваш номер телефона: ")
    cur.execute('INSERT INTO phonebook("personname", "phonenumber") VALUES (%s, %s);', (name, number))
    conn.commit()


def update_contact(PersonName, PhoneNumber):
    cur.execute('UPDATE phonebook SET "phonenumber" = %s WHERE "personname" = %s;', (PhoneNumber, PersonName))
    conn.commit()

def queryData():
    cur.execute('SELECT * FROM phonebook;')
    data = cur.fetchall()
    with open("queredData.txt", "w") as f:
        for row in data:
            if len(row) >= 3:  # Ensure the tuple has at least 3 elements
                f.write(f"name: {row[1]}\nnumber: {row[2]}\n")
            else:
                print(row)
    conn.commit()

def deleteData():
    personName = input("Какое имя вы хотите удалить?\n")
    cur.execute(f'DELETE FROM phonebook WHERE "personname" = %s;', (personName,))
    conn.commit()

def deleteAllData():
    cur.execute('DELETE FROM phonebook;')
    conn.commit()

def searchRecords(pattern):
    cur.execute('SELECT * FROM phonebook WHERE "personname" LIKE %s OR "phonenumber" LIKE %s;', ('%' + pattern + '%', '%' + pattern + '%'))
    data = cur.fetchall()
    with open("searchedData.txt", "w") as f:
        for row in data:
            try:
                f.write(f"name: {row[1]}\nnumber: {row[2]}\n")
            except IndexError:
                print("Row:", row)
    conn.commit()

def insertOrUpdateUser(name, phone):
    cur.execute('SELECT 1 FROM phonebook WHERE "personname" = %s;', (name,))
    existing_user = cur.fetchone()
    if existing_user:
        # User exists, update phone number
        cur.execute('UPDATE phonebook SET "phonenumber" = %s WHERE "personname" = %s;', (phone, name))
    else:
        # User doesn't exist, insert new user
        cur.execute('INSERT INTO phonebook("personname", "phonenumber") VALUES (%s, %s);', (name, phone))
    conn.commit()


def queryDataWithPagination(limit, offset):
    cur.execute('SELECT * FROM phonebook LIMIT %s OFFSET %s;', (limit, offset))
    data = cur.fetchall()
    with open("pagedData.txt", "w") as f:
        for row in data:
            if len(row) >= 3:  # Ensure the tuple has at least 3 elements
                f.write(f"name: {row[1]}\nnumber: {row[2]}\n")
            else:
                print (row)

def deleteDataByUsernameOrPhone(identifier):
    cur.execute('DELETE FROM phonebook WHERE "personname" = %s OR "phonenumber" = %s;', (identifier, identifier))
    conn.commit()

while True:
    print("Что вы хотите сделать?\n\
          1. Ввести данные вручную\n\
          2. Обновить существующий контакт\n\
          3. Запросить данные из таблицы\n\
          4. Удалить данные по имени\n\
          5. Удалить все данные из таблицы\n\
          6. Поиск записей по шаблону\n\
          7. Вставить или обновить пользователя по имени и телефону\n\
          8. Запросить данные с пагинацией\n\
          9.  Удалить данные по имени пользователя или телефону\n\
          10. Выход")

    choice = input("Введите номер действия (1-10):\n")
    if choice == '1':
        inputData()
    elif choice == '2':
        name = input("Введите имя и новый номер через пробел: ").split()
        update_contact(*name)
    elif choice == '3':
        queryData()
    elif choice == '4':
        deleteData()
    elif choice == '5':
        deleteAllData()
    elif choice == '6':
        pattern = input("Введите шаблон для поиска: ")
        searchRecords(pattern)
    elif choice == '7':
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        insertOrUpdateUser(name, phone)
    elif choice == '8':
        limit = int(input("Введите лимит: "))
        offset = int(input("Введите смещение: "))
        queryDataWithPagination(limit, offset)
    elif choice == '9':
        identifier = input("Введите имя пользователя или номер телефона для удаления: ")
        deleteDataByUsernameOrPhone(identifier)
    elif choice == '10':
        break

cur.close()
conn.close()