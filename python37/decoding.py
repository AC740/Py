# Implement your function below.
# def most_frequent(given_list):
#     max_item = None
#     maxcount = 0
#     listD = {}
#     for i in given_list:
#         if i in listD:
#             listD[i] += 1
#         else:
#             listD[i] = 1
#         if maxcount < listD[i]:
#             maxcount = listD[i]
#             max_item = i
    
#     return max_item

# # NOTE: The following input values will be used for testing your solution.
# # most_frequent(list1) should return 1
# list1 = [1, 3, 1, 3, 2, 1]
# # most_frequent(list2) should return 3
# list2 = [3, 3, 1, 3, 2, 1]
# # most_frequent(list3) should return None
# list3 = []
# # most_frequent(list4) should return 0
# list4 = [0]
# # most_frequent(list5) should return -1
# list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]



# def common_elements(list1, list2):
#     result = []
#     processing = True
#     pointA, pointB = 0, 0
#     while (processing):
#         if list1[pointA] == list2[pointB]:
#             result.append(list1[pointA])
#             pointA+=1 
#             pointB+=1
#         elif list1[pointA] > list2[pointB]:
#             pointB+=1
#         else:
#             pointA+=1
#         if pointA >= len(list1) or pointB >= len(list2):
#             processing = False    
#     return result


# # NOTE: The following input values will be used for testing your solution.
# list_a1 = [1, 3, 4, 6, 7, 9]
# list_a2 = [1, 2, 4, 5, 9, 10]
# # common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

# list_b1 = [1, 2, 9, 10, 11, 12]
# list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# # common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

# list_c1 = [0, 1, 2, 3, 4, 5]
# list_c2 = [6, 7, 8, 9, 10, 11]
# # common_elements(list_b1, list_b2) should return [] (an empty list).



# def is_rotation(list1, list2):
#     if len(list1) == len(list2) and sum(list1) == sum(list2) and list1[0] in list2:
         

#     return False

# # NOTE: The following input values will be used for testing your solution.
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# # is_rotation(list1, list2a) should return False.
# list2b = [4, 5, 6, 7, 1, 2, 3]
# # is_rotation(list1, list2b) should return True.
# list2c = [4, 5, 6, 9, 1, 2, 3]
# # is_rotation(list1, list2c) should return False.
# list2d = [4, 6, 5, 7, 1, 2, 3]
# # is_rotation(list1, list2d) should return False.
# list2e = [4, 5, 6, 7, 0, 2, 3]
# # is_rotation(list1, list2e) should return False.
# list2f = [1, 2, 3, 4, 5, 6, 7]
# # is_rotation(list1, list2f) should return True.
# list2g = [7, 1, 2, 3, 4, 5, 6]
# # is_rotation(list1, list2g) should return True.

import math
a = 2.5

print(math.ceil(a))
print(math.floor(a))
