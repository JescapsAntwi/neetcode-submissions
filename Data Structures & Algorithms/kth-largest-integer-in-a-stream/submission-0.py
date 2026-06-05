class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
#stream means we can still add more numbers to the list of numbers 
#we are guaranteed to have k elements when we call the 'add' function 
#add/ pop in min heap is log n time 
# get the minimum value of the min heap is O(1) time 
#we have to keep popping elements until we have k elements in the min heap 
#this is an O(n) operation 
#heapify turns an array into a heap 