# coding: utf-8

import random
import time


Coupon_Type = 1
Gift_Type = 2
Effect_Type = 3
Noble_Type = 4
Frame_Type = 5
Medal_Type = 6
Diamond_Type = 7
NoteGiftId = 379    # 音符礼物id
AnnualMedal = 11  # 冬日躺平
NewGiftId = 422
# 新礼物
luxury_shops_gift_info = [
    {'gift_id': 1, 'num': 1, 'prob': 1000, 'price': 2, 'tp': Gift_Type, 'name': '轮船', 'big': True},
    {'gift_id': 1, 'num': 1, 'prob': 8000, 'price': 2, 'tp': Gift_Type, 'name': '烟花', 'big': True},
    {'gift_id': 1, 'num': 1, 'prob': 25000, 'price': 2, 'tp': Gift_Type, 'name': '营地', 'tips': '全新', 'big': True},
    {'gift_id': 1, 'num': 1, 'prob': 50000, 'price': 2, 'tp': Gift_Type, 'name': '唱片', 'small': True},
    {'gift_id': 1, 'num': 1, 'prob': 171000, 'price': 2, 'tp': Gift_Type, 'name': '八音盒', 'small': True},
    {'gift_id': 0, 'num': 0, 'prob': 695000, 'price': 2, 'tp': Gift_Type, 'name': '随机'},
    {'gift_id': 1, 'num': 1, 'prob': 50000, 'price': 2, 'tp': Coupon_Type, 'name': '券'},
]


def GetRewardProbTest(reward_conf):
    prob_config = reward_conf
    result = {}
    j = 1
    num = 1000000
    while j <= num:
        # 这段为抽奖代码
        random.seed(time.time())
        i = random.randint(1, 1000000)
        prob = 0
        for row in prob_config:
            prob = prob + row['prob']
            if i <= prob:
                if result.has_key(row['gift_id']):
                    result[row['gift_id']] = result[row['gift_id']]+1
                else:
                    result[row['gift_id']] = 1
                break
                # return row
        # 到这
        j += 1
    
    gift_info = {}
    for i in prob_config:
        gift_info[i['gift_id']] = [i['name'], i['prob']]


    strin = "礼物ID: %d, 礼物名称: %s, 抽中次数: %d, 抽中概率: %f, 设定概率: %g"
    
    print('1000000抽奖结果公布:')
    for k, v in result.items():
        res_prob = float(v)/num
        set_prob = float(gift_info[k][1])/num
        string = strin % (k, gift_info[k][0], v, res_prob, set_prob)
        print(string)
    return result


def GetRewardProbTest1(reward_conf):
    prob_config = reward_conf
    result = {}
    j = 1
    while j <= 1000000:
        # 这段为抽奖代码
        random.seed(time.time())
        i = random.randint(1, 1000000)
        prob = 0
        for row in prob_config:
            prob = prob + row['prob']
            if i <= prob:
                if result.has_key(row['gift_id']):
                    result[row['gift_id']] = result[row['gift_id']]+1
                else:
                    result[row['gift_id']] = 1
                break
                # return row
        # 到这
        j += 1
    return result



if __name__ == "__main__":
    # print(GetRewardProbTest(draw_gift_info))
    # GetRewardProbTest(draw_gift_info)
    # print("幸运宝箱概率1")
    # GetRewardProbTest(winter2022_drawreward_list_level1)
    # print("\n")
    # print("幸运宝箱概率2")
    # GetRewardProbTest(winter2022_drawreward_list_level2)
    # print("\n")
    GetRewardProbTest(luxury_shops_gift_info)
