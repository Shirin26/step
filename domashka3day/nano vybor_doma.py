j раraion = input('Введите район: ')
str_mat = input('Введите стройматериал: ')
price = int(input('Введите стоимость: '))
size = int(input('Введите размер участка: '))

if raion == 'чон арык' or raion == 'байтик' or raion == 'орто сай':
    print('Ваш район: ', raion)
    if str_mat == 'кирпич'  and  size <= 4 and price <= 50000:
        print('Ваш дом стоит не более', price)
    elif str_mat == 'пескоблок'  and  size <= 5 and price <= 45000:
        print('Ваш дом стоит не более', price)
    else:
        print('Ваши зарактеристика не подошли под условия' )
else:
    print('нет такого района')
