# -*- coding: utf-8 -*- #
def links():
    with open('porn/porn.txt', 'r') as r:
        readlines = r.readlines()
        title = str(readlines[0]).split('\n')
        types_con_1 = str(readlines[1]).split('\n')
        file_id_con_1 = str(readlines[2]).split('\n')
        types_con_2 = str(readlines[3]).split('\n')
        file_id_con_2 = str(readlines[4]).split('\n')
    with open('porn/porn.txt', 'r') as r:
        text = r.read()
        text = "\n".join(text.split("\n")[6:])

    with open('porn/porn.txt', 'w') as w:
        w.write(text)
    return title[0], types_con_1[0], file_id_con_1[0], types_con_2[0], file_id_con_2[0]
