
"""
不均等随机函数,值越大随机到的几率就越大
"""

# method1
import random
def weighted_random(items): 
    total = sum(w for _,w in items) 
    n = random.uniform(0, total)#在饼图扔骰子 
    for x, w in items:#遍历找出骰子所在的区间 
        if n<w: 
            break
        n -= w 
    return x 


# method2
def get_random_by_length(arr):
    """根据数组内数字的长度取值，长度都一样的时候没啥用"""
    # arr=[20, 34, 160,25,45,67,345,234]
    #arr_jangci为将高积分增加了参与抽奖的次数的抽奖池对像
    arr_jangci=[]
    for i in arr:
        ii=len(str(i))+1
    #先取每个积分的长度，长度是多少就在奖池内增加多少个抽奖样本，这样就增加了中奖概率
        for j in range(1,ii):
            arr_jangci.append(i)
    #查看重新组合过后的奖池数组
    print(arr_jangci)
    #在奖池里随机抽出一个对象作为中奖者
    drawed = random.sample(arr_jangci,1)
    print(drawed)
    return drawed


# method3
class WeightRandom: 
    def __init__(self, items): 
        weights = [w for _,w in items] 
        self.goods = [x for x,_ in items] 
        self.total = sum(weights) 
        self.acc = list(self.accumulate(weights)) 

    def accumulate(self, weights):#累和.如accumulate([10,40,50])->[10,50,100] 
        cur = 0
        for w in weights: 
            cur = cur+w 
        yield cur 

    def __call__(self): 
        return self.goods[bisect.bisect_right(self.acc , random.uniform(0, self.total))] 


def main(remix_uids):
    draw_result = {}
    i = 0
    while i < 1000:
        res = weighted_random(remix_uids)
        # print(res)
        if res in draw_result:
            draw_result[res] += 1
        else:
            draw_result[res] = 1
        i += 1
    print(draw_result)


if __name__ == "__main__":
    remix_uids = [
        (49486955542483969, 112),
        (124975991180219920, 22),
        (86923615620039604, 332),
        (21550172278152754, 43),
        (179174002594440594, 51),
        (169267235295094878, 63),
        (11944480065326593, 75),
        (134984527009757484, 8123),
        (134980710994225938, 9233),
        (134983159668748025, 1011),
        (133895169127066118, 11211)
    ]
    main(remix_uids)
