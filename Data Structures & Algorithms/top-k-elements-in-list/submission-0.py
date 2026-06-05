import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        use the top k elements technique 
       count frequency of numbers in a hashmap 
       initialize min_heap 
       iterate through dictionary, add (freq, nums) tuples to min_heap 
       if size of min_heap exceeds k, remove top element
       return top k frequent elements

        '''
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]