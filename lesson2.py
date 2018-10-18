spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spisok2 = [1, 2, 3, 4, 5, 6, 7, 8, 10]


def pravilo1(sp):
    if 9 not in sp:
        print('Baaad')
        s = False
    else:
        print('list is good')
        s = True
    return s


list_result = []

result = pravilo1(spisok)
list_result.append(result)

print('*' * 50)

result = pravilo1(spisok2)
list_result.append(result)
print('*' * 50)

if list_result:
    print('good results')




print(list_result)
