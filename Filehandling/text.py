# # obj = open(r'dat.txt')
# # print(obj)
# '''
# read()
# readline()
# readlines()
# for loop
# '''
# # with open(r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\football.txt','r',encoding='utf-8') as file :
# #     print(file.read())
# #
# # with open(r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\football.txt','r', encoding='utf-8') as file:
# #     print(file.readline())
# #
# # with open(r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\football.txt','r', encoding='utf-8') as file:
# #     print(file.readlines())
#
# with open(r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\football.txt','r', encoding='utf-8') as file:
#     for i in file:
#        if 'Brazil' in i:
#            print(i)

with open('students_data.txt','a') as file:
    file.write('Hello my name is satyam')
file.close()


#
# with open('python_students_data.txt','a') as file:
#     file.writelines(['Hello my name is kartik\n',
#                      'Hello my name is shivam\n',
#                      'Hello my name is baburao\n'])
path = r'C:\Work\Python batches\PWA-PFFPTD-A2\files\extra_files\football.txt'
d ={}
with open(path,'r',encoding='utf-8') as read_file:
    header = next(read_file)
    for i in read_file:
        l = i.split('\t')
        with open(f'{l[1]}.txt','a',encoding='utf-8') as write_file:
            if l[1] not in d:
                d[l[1]] = 1
                write_file.write(header)
            write_file.write(i)
        write_file.close()
    read_file.close()


