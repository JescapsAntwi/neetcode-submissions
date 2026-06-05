class TimeMap:

    def __init__(self):
        self.keyStore = {} # key: list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #check if key is in hashmap else add its value and timestamp
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values_array = self.keyStore.get(key, [])

        #binary search comes in 
        l, r = 0, len(values_array) - 1
        while l <= r:
            m = (l + r) // 2
            if values_array[m][1] <= timestamp:
                res = values_array[m][0]
                l = m + 1
            else:
                r = m - 1
        return res 
'''
each key will have values and the values will be pairs:
the values themselves and the timestamp

constructor and the operations performed on the values

set O(1)
["foo", bar2, 1] = foo (key), bar2 (value), 1 (timestamp)

get O(1) because of binary search 
loop through hashmap and find timestamp that matches timestamp given
if similar, return it else return the closest and smallest value (in terms of timestamp)
compared to the timestamp given.

the list is already sorted by timestamp in ascending order by default

The binary search is designed to find the largest timestamp ≤ input timestamp.
'''