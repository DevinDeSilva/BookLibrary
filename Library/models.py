import os
import re

from django.conf import settings


# Create your models here.

def getBooks(search_str, search_by):
    books = readTxt(search_str, search_by)
    print("get books")
    return books


def addBook(title, author, genre, height, publication, file_name='books_list.txt',
            data_dir=os.path.join(settings.BASE_DIR, 'Library\\data')):
    data_file = open(os.path.join(data_dir, file_name), "a+")
    data_file.write(f"\n{','.join([title, author, genre, height, publication])}")
    data_file.close()
    print("addBook")


def deleteBook(title, file_name='books_list.txt',
               data_dir=os.path.join(settings.BASE_DIR, 'Library\\data')):
    data_file = open(os.path.join(data_dir, file_name), "r+")
    lines = []
    while data_file:
        line = data_file.readline()
        if line == "":
            break

        data = text_to_dic(line)
        if data['title'] == title:
            continue

        lines.append(line)
    data_file.truncate(0)
    total_text = "".join(lines)
    total_text = total_text[:-1] if total_text[-1] == '\n' else total_text
    print(total_text)
    data_file.write(total_text)
    data_file.close()
    print("deleteBook")


def text_to_dic(line):
    list_data = line.split(",")
    if len(list_data) == 5:
        dic_data = {
            "title": list_data[0],
            "author": list_data[1],
            "genre": list_data[2],
            "height": list_data[3],
            "publisher": list_data[4][:-1] if list_data[4][-1] == '\n' else list_data[4],
        }
        return dic_data
    if len(list_data) == 6:
        dic_data = {
            "title": list_data[0],
            "author": ','.join([list_data[1], list_data[2]]),
            "genre": list_data[3],
            "height": list_data[4],
            "publisher":list_data[5][:-1] if list_data[5][-1] == '\n' else list_data[5],
        }
        return dic_data

    if len(list_data) == 7:
        dic_data = {
            "title": ','.join([list_data[0], list_data[1]]),
            "author": ','.join([list_data[2], list_data[3]]),
            "genre": list_data[4],
            "height": list_data[5],
            "publisher": list_data[6][:-1] if list_data[6][-1] == '\n' else list_data[6],
        }

        return dic_data


def readTxt(search_str, search_by, file_name='books_list.txt',
            data_dir=os.path.join(settings.BASE_DIR, 'Library\\data')):
    data_file = open(os.path.join(data_dir, file_name), "r")
    books = []
    while data_file:
        line = data_file.readline()
        print(line)
        if line == "":
            break

        data = text_to_dic(line)
        if data['title'] == 'Title':
            continue

        if search_str is not None and search_by is not None:
            if search_by == "name":
                search_key = 'title'
            else:
                search_key = 'genre'

            reg_result = re.match(f'({search_str[:-1]})\w+', data[search_key], re.IGNORECASE)
            if not reg_result:
                data = None

        if data is not None:
            books.append(data)

    data_file.close()

    return books
