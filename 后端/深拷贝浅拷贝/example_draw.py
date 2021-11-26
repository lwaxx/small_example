# coding=utf8

import random
import time
import copy

"""
抽奖实例
按照概率随机在luxury_shops_gift_info中抽取一个礼物
其中luxury_shops_gift_info[6]为随机在luxury_shops_random_gift_info中抽取的一个小礼物
"""

luxury_shops_gift_info = [
    {'gift_id': 1, 'num': 1, 'prob': 1000, 'price': 88, 'tp': 2, 'name': '兰博基尼'},
    {'gift_id': 2, 'num': 1, 'prob': 8000, 'price': 19, 'tp': 2, 'name': '飞船'},
    {'gift_id': 3, 'num': 1, 'prob': 19000, 'price': 20, 'tp': 2, 'name': '派对'},
    {'gift_id': 4, 'num': 1, 'prob': 30000, 'price': 38, 'tp': 2, 'name': '待定'},
    {'gift_id': 5, 'num': 1, 'prob': 50000, 'price': 29, 'tp': 2, 'name': '唱片'},
    {'gift_id': 6, 'num': 1, 'prob': 173000, 'price': 18, 'tp': 2, 'name': '打call'},
    {'gift_id': 0, 'num': 0, 'prob': 719000, 'price': 1, 'tp': 2, 'name': '随机礼物'},
]

luxury_shops_random_gift_info = {
    1: {'gift_id': 10, 'name': '棒棒糖'},
    2: {'gift_id': 11, 'name': '甜甜圈'},
    3: {'gift_id': 12, 'name': '情侣'},
    4: {'gift_id': 13, 'name': '玫瑰'},
    5: {'gift_id': 14, 'name': '情书'},
    6: {'gift_id': 15, 'name': '小票'},
}

list1 = []

def store2021GetReward():
    ## 此处使用deepcopy，最后得到的结果是正常的
    prob_config = copy.deepcopy(luxury_shops_gift_info)
    ## 如果考虑直接赋值，list1d的随机小礼物最后会被最后一次抽到的小礼物覆盖，从而造成错误的抽奖结果
    # prob_config = luxury_shops_gift_info

    get_random_gift(prob_config)
    random.seed(time.time())
    i = random.randint(1, 1000000)
    prob = 0
    for row in prob_config:
        prob = prob + row['prob']
        if i <= prob:
            return row
    return {}

def get_random_gift(prob_config):
    gift_info = luxury_shops_random_gift_info[random.randint(1, 6)]
    gift_num = random.randint(30, 60)
    prob_config[6]["gift_id"] = int(gift_info["gift_id"])
    prob_config[6]["num"] = int(gift_num)
    prob_config[6]["name"] = gift_info["name"]


def test():
    # list1 = []
    for i in range(10):
        reward = store2021GetReward()
        print(id(reward))
        list1.append(reward)
    return list1


print(test())
