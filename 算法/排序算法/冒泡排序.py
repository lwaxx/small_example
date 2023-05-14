"""
冒泡排序
时间复杂度: O(n^2)
"""

def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


# 优化之后
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False       # 当不进行交换的时候，说明已经排好序了，直接退出
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
            exchange = True
        if not exchange:
            return


li = [9,8,7,1,2,3,4,5,6]
bubble_sort(li)
print(li)