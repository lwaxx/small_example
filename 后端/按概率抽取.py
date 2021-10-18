# coding: utf-8

import random
import time


Coupon_Type = 1
Gift_Type = 2
Effect_Type = 3
Noble_Type = 4
Frame_Type = 5
Medal_Type = 6

TravelWordGiftId = 359
PhonographGiftId = 0
BlueRoseGiftId = 261
LoveBearGiftId = 1342
PinkFerrariEffectId = 1
PictureFrameId = 32
FallInLoveGiftId = 262
RoseGiftId = 9

fanpai2021_drawreward_list_low = [
    {'gift_id': TravelWordGiftId, 'num': 1, 'prob': 600, 'price': 999, 'tp': Gift_Type, 'big': True, 'name': '环游世界*1'},
    {'gift_id': PhonographGiftId, 'num': 1, 'prob': 12000, 'price': 299, 'tp': Gift_Type, 'big': True, 'name': '唱片机*1'},
    {'gift_id': BlueRoseGiftId, 'num': 1, 'prob': 25000, 'price': 99, 'tp': Gift_Type, 'name': '蓝玫瑰*1'},
    {'gift_id': LoveBearGiftId, 'num': 1, 'prob': 80000, 'price': 30, 'tp': Gift_Type, 'name': '爱心小熊*1'},
    {'gift_id': PinkFerrariEffectId, 'num': 1, 'prob': 80000, 'price': 0, 'tp': Effect_Type, 'name': '粉色跑车*1天'},
    {'gift_id': PictureFrameId, 'num': 1, 'prob': 205000, 'price': 0, 'tp': Frame_Type, 'name': '头像框*1天'},
    {'gift_id': FallInLoveGiftId, 'num': 1, 'prob': 297000, 'price': 13, 'tp': Gift_Type, 'name': '坠入爱河*1'},
    {'gift_id': RoseGiftId, 'num': 5, 'prob': 300400, 'price': 5, 'tp': Gift_Type, 'name': '玫瑰*5'},
]

fanpai2021_drawreward_list_high = [
    {'gift_id': TravelWordGiftId, 'num': 1, 'prob': 1300, 'price': 999, 'tp': Gift_Type, 'big': True, 'name': '环游世界*1'},
    {'gift_id': PhonographGiftId, 'num': 1, 'prob': 13000, 'price': 299, 'tp': Gift_Type, 'big': True, 'name': '唱片机*1'},
    {'gift_id': BlueRoseGiftId, 'num': 1, 'prob': 25000, 'price': 99, 'tp': Gift_Type, 'name': '蓝玫瑰*1'},
    {'gift_id': LoveBearGiftId, 'num': 1, 'prob': 79000, 'price': 30, 'tp': Gift_Type, 'name': '爱心小熊*1'},
    {'gift_id': PinkFerrariEffectId, 'num': 1, 'prob': 80000, 'price': 0, 'tp': Effect_Type, 'name': '粉色跑车*1天'},
    {'gift_id': PictureFrameId, 'num': 1, 'prob': 205000, 'price': 0, 'tp': Frame_Type, 'name': '头像框*1天'},
    {'gift_id': FallInLoveGiftId, 'num': 1, 'prob': 297700, 'price': 13, 'tp': Gift_Type, 'name': '坠入爱河*1'},
    {'gift_id': RoseGiftId, 'num': 5, 'prob': 299000, 'price': 5, 'tp': Gift_Type, 'name': '玫瑰*5'},
]


def fanPai2021GetReward(level):
    if level == "low":
        prob_config = fanpai2021_drawreward_list_low
    else:
        prob_config = fanpai2021_drawreward_list_high
    
    result = {}
    j = 1
    while j <= 100000:
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
    print(fanPai2021GetReward("low"))
    print(fanPai2021GetReward("high"))