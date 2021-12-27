import csv


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt', ]
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files:
        with open(file, encoding='windows-1251') as data_file:
            for row in data_file:
                if 'Изготовитель системы' in row.split(':')[0]:
                    os_prod_list.append(row.split(':')[1].strip())
                if 'Название ОС' in row.split(':')[0]:
                    os_name_list.append(row.split(':')[1].strip())
                if 'Код продукта' in row.split(':')[0]:
                    os_code_list.append(row.split(':')[1].strip())
                if 'Тип системы' in row.split(':')[0]:
                    os_type_list.append(row.split(':')[1].strip())
        main_data.append(
            [
                os_prod_list[-1],
                os_name_list[-1],
                os_code_list[-1],
                os_type_list[-1]
            ])
    return main_data


def write_csv(file):
    with open(file, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in get_data():
            csv_writer.writerow(row)


write_csv("new_csv.csv")
