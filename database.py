import view
import json
import datetime


def add_bd(data):  # 1 > добавить заметку
    with open('note.csv', 'a', encoding='utf-8') as f:
        f.writelines(data)
    print('данные успешно внесены')


def print_bd():  # 2 > вывод списка заметок
    with open('note.csv', 'r', encoding='utf-8') as f:
        print(f.read())


def sort_bd(value_sorting):  # 3 > сортировка заметок
    with open('note.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        data.sort(key=lambda x: x.split(';')[value_sorting])
        with open('note.csv', 'w', encoding='utf-8') as f:
            f.writelines(data)


def printName_bd(value_print):  # 4 > вывести заголовки заметок
    with open('note.csv', 'r', encoding='utf-8') as f:
        result = f.readlines()
        for i in result:
            print(i.split(';')[value_print])


def search_bd(scan):  # 5 > поиск заметки
    with open('note.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        flag = False
        for i in data:
            if scan in i:
                print(i)
                flag = True
        if not flag:
            print('заметка не найдена!')


def rewriteNode_bd(val):  # 6 > корректировка заметки полная
    with open('note.csv', 'r', encoding='utf-8') as f:
        result = f.readlines()
        for i, v in enumerate(result):
            print(i, v.split(';')[val])
        print('------------------')
        value_change = int(input('Введите цифру соответствующую выбранной заметке для внесения изменений: '))
        new_data = view.inputNote()
        # print(new_data)
        for i, v in enumerate(result):
            if i == value_change:
                result[i] = new_data
            #     print(result[i])
            # print(i, v.split()[val])
        print('-->  информация обновлена')
        with open('note.csv', 'w', encoding='utf-8') as f:
            f.writelines(result)


def correctionNote_bd():  # 7 > корректировка заголовка заметки
    with open('note.csv', 'r', encoding='utf-8') as f:
        result = f.readlines()
        value_user = str(input('Введите заголовок существующей заметки для ее изменения: '))
        for i, v in enumerate(result):
            if value_user in v.split(';')[1]:
                print(i, value_user)
        value_user_change = int(input('Введите номер изменяемой позиции: '))
        val_new = str(input('Введите новые данные: '))
        for i, v in enumerate(result):
            if i == value_user_change:
                # print(result[i].split(';')[value])
                result[i] = result[i].replace((result[i].split(';')[1]), " ЗАГОЛОВОК: " + val_new, 1)
                print('->', result[i])
        print('информация обновлена')
        with open('note.csv', 'w', encoding='utf-8') as f:
            f.writelines(result)


def deleteNote_bd(name):  # 8 > удалить заметку
    with open('note.csv', 'r', encoding='utf-8') as f:
        result = f.readlines()
        for i, v in enumerate(result):
            print(i, v.split(';')[name])
        print('------------------')
        value_del = int(input('Введите цифру соответствующую удаляемой заметке: '))
        for i, v in enumerate(result):
            if i == value_del:
                del result[i]
        print('-->  заметка успешно удалена!')
        with open('note.csv', 'w', encoding='utf-8') as f:
            f.writelines(result)


def expImport_bd(value_expImp):  # 9 > экспорт файла (в формате json)
    if value_expImp == 0:
        with open('note.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
        with open('json_note.json', 'w', encoding='utf-8') as f:
            json_note = json.dump(data, f)
            print('Объект записан в формате json')
    elif value_expImp == 1:  # 9 > импорт файла в формате json
        with open('json_note.json', 'r', encoding='utf-8') as f:
            result = json.load(f)
            # print(result)
        with open('note.csv', 'a') as f:
            f.writelines(result)
        print('данные из файла импортированы в приложение')


def saveLog_bd(message):  # логирование работы прогр.
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    # print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')
