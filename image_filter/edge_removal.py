import cv2
import numpy as np
image_to_filter = cv2.imread('/Users/bhargavd/Desktop/project/technolamy/image_filter/Nord-ce2-lite-Blue.png')

BLACK_PIXEL = [0, 0, 0]

row_length = len(image_to_filter)
col_length = len(image_to_filter[0])


def pixel_detection():
    # n_tuple = [
    #            [(0, row_length, 1), (0, col_length, 1)],
    #            [(row_length - 1, 0, -1), (0, col_length, 1)],
    #            [(0, col_length, 1), (0, row_length, 1)],
    #            [(col_length - 1, 0, -1), (0, row_length, 1)]
    #            ]
    n_tuple = [
               [(0, row_length), (0, col_length)],
               [(0, col_length), (0, row_length)]
               ]
    values = []
    for m_tuple in n_tuple:
        print(m_tuple)
        for row_v in range(*m_tuple[0]):
            flag_v = 0
            for col_v in range(*m_tuple[1]):
                if list(image_to_filter[row_v][col_v]) != BLACK_PIXEL:
                    flag_v = 1
                    break
            if flag_v == 1:
                values.append((row_v, col_v))
                break
    return values


print(pixel_detection())
# for row in range(0, row_length):
#     flag = 0
#     for col in range(0, col_length):
#         if list(image_to_filter[row][col]) != BLACK_PIXEL:
#             print(image_to_filter[row][col])
#             print(row, col)
#             flag = 1
#             break
#     if flag == 1:
#         break
#
# for col in range(0, col_length):
#     flag = 0
#     for row in range(0, row_length):
#         if list(image_to_filter[row][col]) != BLACK_PIXEL:
#             print(image_to_filter[row][col])
#             print(row, col)
#             flag = 1
#             break
#     if flag == 1:
#         break
