# # # # from _csv import *
# # # import csv
# # #
# # # path = r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\csv_files\employees.csv'
# # # # with open(path) as file:
# # # #     obj = csv.reader(file)
# # # #     for i in obj:
# # # #         print(i)
# # # #
# # # # with open(path) as file:
# # # #     obj = csv.DictReader(file)
# # # #     for i in obj:
# # # #         print(i)
# # #
# # # with open(path) as file:
# # #     obj = csv.reader(file)
# # #     for i in obj:
# # #         if i[2] == 'development':
# # #             print(i)
# # #
# # # with open(path) as reader_file:
# # #     obj1 = csv.DictReader(reader_file)
# # #     for i in obj1:
# # #         if i['team'] == 'development':
# # #             print(i)
# # import csv
# # path = r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\csv_files\test.csv'
# # with open(path) as file:
# #     next(file)
# #     obj = csv.reader(file)
# #     for i in obj:
# #         if float(i[2]) > 50:
# #             print(i)
# #     file.close()
# #
# #
# # with open(path) as reader_file:
# #     obj1 = csv.DictReader(reader_file)
# #     for j in obj1:
# #         if float(j['price']) > 50:
# #             print(j)
# import csv
# with open('data_csv.csv','a') as file:
#     obj = csv.writer(file)
#     obj.writerows([('satyam',45),
#                    ('tony',50),
#                    ('steve',500),
#                    ('thor',2000)])
#
# with open(r'dict_data.csv','w') as file:
#     obj = csv.DictWriter(file,['name','age'])
#     obj.writeheader()
# #
#
# with open(r'dict_data.csv','a') as file:
#     obj = csv.DictWriter(file,['name','age'])
#     obj.writerows([{'name':'baburao','age':50},
#                    {'name':'shyam','age':35},
#                    {'name':'raju','age':30}])
#
import csv
d={}
path = r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\csv_files\employees.csv'
with open(path) as reader_file:
    header = next(reader_file)
    obj = csv.reader(reader_file)
    for i in obj:
        with open(f'{i[2]}.csv','a') as write_file:
            w_obj = csv.writer(write_file)
            if i[2] not in d:
                d[i[2]] = 1
                w_obj.writerow(header)
            w_obj.writerow(i)
        write_file.close()
    reader_file.close()