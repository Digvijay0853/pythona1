# # #      1 2 3 4 5 6 7 8 9
# # #    1         *
# # #    2       * * *
# # #    3     * * * * *
# # #    4   * * * * * * *
# # #    5 * * * * * * * * *
# # #    6   * * * * * * *
# # #    7     * * * * *
# # #    8       * * *
# # #    9         *
# #
# #
# # # for i in range(1,6):
# # #     for j in range(1,6-i):
# # #         print(' ',end=' ')
# # #     for k in range(i):
# # #         print('*',end=' ')
# # #     for a in range(i-1):
# # #         print('*',end=' ')
# # #     print()
# # #
# # # for b in range(1,5):
# # #     for c in range(b):
# # #         print(' ',end=' ')
# # #     for d in range(5-b):
# # #         print('*',end=' ')
# # #     for d in range(5-b-1):
# # #         print('*',end=' ')
# # #     print()
# #
# #
# #
# # #  #  * * * * * *
# # #  #  *         *
# # #  #  *         *
# # #  #  *         *
# # #  #  * * * * * *
# # # # end =
# # # for i  in range(1,6):
# # #     if i == 1 or i == 5:
# # #         for a in range(1,7):
# # #             print('*',end=' ')
# # #     else:
# # #         for j in range (1,7):
# # #             if j == 1 or j == 6:
# # #                 print('*',end=' ')
# # #             else:
# # #                 print(' ',end=' ')
# # #     print()
# #
# # #    1 2 3 4 5 6
# # #  1 *
# # #  2 * *
# # #  3 *   *
# # #  4 *     *
# # #  5 *       *
# # #  6 *     *
# # #  7 *   *
# # #  8 * *
# # #  9 *
# #
# #
# # # end = 9
# # # for i in range(1,6):
# # #     if i in [1,2]:
# # #         for j in range(i):
# # #             print('*',end=' ')
# # #     else:
# # #         for a in range(1):
# # #             print('*',end=' ')
# # #         for b in range(i-2):
# # #             print(' ',end=' ')
# # #         for c in range(1):
# # #             print('*',end=' ')
# # #     print()
# # # for i in range(6,0,-1):
# # #     if i in [1,2]:
# # #         for j in range(i):
# # #             print('*',end=' ')
# # #     else:
# # #         for a in range(1):
# # #             print('* ',end=' ')
# # #         for b in range(i-2):
# # #             print(' ',end=' ')
# # #         for c in range(1):
# # #             print('*',end=' ')
# # #     print()
# #
# # #    1 2 3 4 5 6 7 8 9 10
# # #  1         *
# # #  2       *   *   # 1
# # #  3     *       *   # 3
# # #  4   *           *  # 5
# # #  5 *               * # 7
# # #  6   *           *
# # #  7     *       *
# # #  8       *   *
# # #  9         *
# #
# # for i in range(1,6):
# #     for j in range(1,6-i):
# #         print(' ',end=' ')
# #     for k in range(1):
# #         print('*',end=' ')
# #     if i != 1:
# #         if i == 2:
# #             for a in range(1):
# #                 print(' ',end=' ')
# #         elif i == 3 :
# #             for b in range(i):
# #                 print(' ',end=' ')
# #         elif i == 4 :
# #             for c in range(i+1):
# #                 print(' ',end=' ')
# #         else:
# #             for d in range(i+2):
# #                 print(' ',end=' ')
# #     for e in range(1):
# #         print('*',end=' ')
# #     print()
#
# #4string ""aaabbccccdaa"" will be compressed to ""a3b2c4d1a2"".
# s = "aaabbccccdaa"
#
#
# def compress(s):
#     new = ""
#     current_char = s[0]
#     count = 1
#     for char in s[1::]:
#         if current_char == char:
#             count+=1
#         else:
#             new+= current_char+str(count)
#             current_char = char
#             count = 1
#     new+=current_char+str(count)
#     return new
#
# # print(compress(s))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

l = [114,12,4,2,7,8]
print(bubble_sort(l))
