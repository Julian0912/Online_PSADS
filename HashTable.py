# -*- coding:utf8 -*-
# Author: Julian Black
# Description:
#


class HashTable(object):
    """使用Remainder Method和Chaining创建的哈希表"""

    def __init__(self, capacity=11):
        """容量建议取素数

        capacity: 哈希表总容量
        slots: 哈希表的位置
        data: 哈希表对应位置上的值，遇到collisions则以列表形式按顺序存储多个值
        size: 当前哈希表中存在的键值对数
        """
        self.capacity = capacity
        self.slots = [[] for _ in range(capacity)]
        self.data = [[] for _ in range(capacity)]
        self.size = 0

    def put(self, key, value):
        """将key-value添加进哈希表

        key: int
        """
        if not isinstance(key, int):
            raise ValueError('当前版本key必须为整数')
        slot = self.__hash_function(key)  # 获取一个位置
        if key in self.slots[slot]:  # 如果key已存在
            k = self.slots[slot].index(key)  # 获取索引
            self.data[slot][k] = value  # 修改data中的对应值
        else:
            self.slots[slot].append(key)  # 添加key-value
            self.data[slot].append(value)
            self.size += 1

    def get(self, key):
        """返回key对应的value，若不存在则返回None"""
        if not isinstance(key, int):
            raise ValueError('当前版本key必须为整数')
        slot = self.__hash_function(key)
        if key in self.slots[slot]:  # 如果key存在
            k = self.slots[slot].index(key)  # 获得索引
            value = self.data[slot][k]
            return value
        else:
            return None

    def __hash_function(self, key):
        """Remainder Method

        key: int
        """
        return key % self.capacity

    def __len__(self):
        return self.size

    def __del__(self):
        """暂时（190804）不会用"""
        pass

    def __getitem__(self, key):
        """方法与get()相同"""
        if not isinstance(key, int):
            raise ValueError('当前版本key必须为整数')
        slot = self.__hash_function(key)
        if key in self.slots[slot]:  # 如果key存在
            k = self.slots[slot].index(key)  # 获得索引
            value = self.data[slot][k]
            return value
        else:
            return None

    def __setitem__(self, key, value):
        """方法与put()相同"""
        if not isinstance(key, int):
            raise ValueError('当前版本key必须为整数')
        slot = self.__hash_function(key)  # 获取一个位置
        if key in self.slots[slot]:  # 如果key已存在
            k = self.slots[slot].index(key)  # 获取索引
            self.data[slot][k] = value  # 修改data中的对应值
        else:
            self.slots[slot].append(key)  # 添加key-value
            self.data[slot].append(value)
            self.size += 1

    def __str__(self):
        head = "HashTable("
        for i in range(self.capacity):
            for j in range(len(self.slots[i])):
                body = "'{}':'{}'".format(self.slots[i][j], self.data[i][j])  # 未考虑value中含"'"的情况
                head += body+', '
        tail = ")"
        return head + tail


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H)
