# # # # # # # # s = 'hello'
# # # # # # # # s1=sorted(s)
# # # # # # # # print(s1)
# # # # # # # #
# # # # # # # # l = [5,4,3,2,1]
# # # # # # # # l1=sorted(l)
# # # # # # # # print(l1)
# # # # # # # #
# # # # # # # #
# # # # # # # # d = {'a':100,'b':0,'c':30}
# # # # # # # # d1=sorted(d.values())
# # # # # # # # print(d1)
# # # # # # # #
# # # # # # # # s = {5,54,78,2312,12}
# # # # # # # # s2 = sorted(s)
# # # # # # # # print(s2)
# # # # # # # #
# # # # # # # # a = (45,78,12,4,5)
# # # # # # # # a1 = sorted(a)
# # # # # # # # print(a1)
# # # # # # #
# # # # # # # l = ['hello','hi','bye','hii']
# # # # # # # var = sorted(l,key=len,reverse=True)
# # # # # # # print(var)
# # # # # # l = ['hii','bye','hello']
# # # # # # def last_chat(s):
# # # # # #     return s[-1]
# # # # # # var = sorted(l,key=last_chat)
# # # # # # print(var)
# # # # #
# # # # # l = [12,3,5,10,2,15,8,9]
# # # # # odd = [i for i in l if i% 2 != 0]
# # # # # odd.sort()
# # # # # even = [i for i in l if i%2 == 0]
# # # # # even.sort()
# # # # # print(even+odd)
# # # #
# # # #
# # l = ['hello','bye','hii']
# # def bubble_sort(arr):
# #     end = len(arr)
# #     for i in range(end):
# #         for j in range(end-1-i):
# #             if arr[j][-1] > arr[j+1][-1]:
# #                 arr[j],arr[j+1] = arr[j+1],arr[j]
# #     return arr
# # # l=[5,4,3,2,1]
# # print(bubble_sort(l))
# #
# # #
# # # def linear_Sreach(list,target):
# # #     for i,j in enumerate(list):
# # #         if j == target:
# # #             return i
# # #
# # # l=[1,2,3,4,5]
# # # print(linear_Sreach(l,4))
# #
# #
# # def binary_search(arr,target,start,end):
# #     mid = (start+end) // 2
# #     if arr[mid] == target:
# #         return mid
# #     elif  arr[mid] > target:
# #        return binary_search(arr,target,start,mid-1)
# #     else:
# #         return  binary_search(arr,target,mid+1,end)
# #
# # # l = [1,2,3,4,5]
# # # print(binary_search(l,1,0,4))
#
#
# s = 'hello everyone how are you everyone are fine ?'
# l = s.split(' ')
# repeated = [i for i in l if s.count(i)>1]
# l1 = sorted(repeated,key=len)
# print(l1[-1])
#
# s = 'hello everyone how are you everyone are fine ?'
# l = s.split(' ')
# repeated = [i for i in l if s.count(i)==1]
# l1 = sorted(repeated,key=len)
# print(l1[-1])

s = 'hello everyone how are you everyone are fine ?'
def sum(s):
    sum = 0
    for i in s :
        sum+=ord(i)
    return sum
l = s.split()
def bubble_sort(arr):
    end = len(arr)
    for i in range(end):
        for j in range(end-1-i):
            if sum(arr[j]) > sum(arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort(l))
