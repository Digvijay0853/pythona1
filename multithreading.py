# from threading import *
# import time
# # # def demo():
# # #     for i in range(1,10):
# # #         print(current_thread().name)
# # #
# # # t1=Thread(target=demo,name="Thread one")
# # # t2 = Thread(target=demo,name="Thread Two")
# # # t1.start()
# # # t2.start()
# #
# # def doubles(n):
# #     for i in n:
# #         time.sleep(1)
# #         print(f'Double:{i+i}')
# # def squares(n):
# #     for j in n:
# #         time.sleep(1)
# #         print(f'Squares:{j*j}')
# # l = [1,2,3,4,5,6]
# # start = time.time()
# # doubles(l)
# # squares(l)
# # print('time taken for execute above program is ',time.time()-start)
# #
# # l = [1,2,3,4,5,6]
# #
# # def doubles(n):
# #         print(active_count())
# # def squares(n):
# #         print(active_count())
# #
# # print(active_count())
# # t1 = Thread(target=doubles,args=(l,))
# # t2 = Thread(target=squares,args=(l,))
# # print(active_count())
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# # print(active_count())
# # from threading import *
# # class Demo:
# #
# #     def even_numbers(self):
# #         for i in range(1,21):
# #             if i%2 == 0:
# #                 print(current_thread().name)
# #
# #     def odd_number(self):
# #         for j in range(1,21):
# #             if j%2 != 0:
# #                 print(current_thread().name)
# # obj = Demo()
# # t1=Thread(target=obj.even_numbers)
# # t2=Thread(target=obj.odd_number)
# # t1.start()
# # t2.start()
#
#
#
# class Demo(Thread):
#       def hello(self):
#         print('in hello')
#
#       def run(self):
#               for i in range(1,11):
#                       print(current_thread().name)
#
# obj = Demo()
# obj.start()
#
# for i in range(1,11):
#         print(current_thread().name)
import time
from threading import *
l= Semaphore(2)
def greeting(name):
        l.acquire()
        for i in range(1,6):
                print(f'Good morning ',end='')
                time.sleep(2)
                print(name)
                print(current_thread().name)
        l.release()

t1 = Thread(target=greeting,args=('Dhoni',))
t2 = Thread(target=greeting,args=('Yuvraj',))
t3 = Thread(target=greeting,args=('Rohit',))
t4 = Thread(target=greeting,args=('Virat',))
t5 = Thread(target=greeting,args=('Chahal',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()