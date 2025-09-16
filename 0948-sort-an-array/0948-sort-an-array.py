class Solution:
    def marge(self, arr, st:int, mid:int, end:int):
        temp = []
        i,j = st, mid+1
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=end:
            temp.append(arr[j])
            j+=1
        arr[st:end+1] =temp
                
        
    def margeSort(self, arr, st:int, end:int):
        if st < end:
            mid = st+(end-st)//2
            self.margeSort(arr,st, mid)
            self.margeSort(arr, mid+1, end)
            self.marge(arr,st, mid, end)
         
        
    def sortArray(self, nums: list[int]) -> list[int]:
        self.margeSort(nums, 0, len(nums)-1)
        return nums
        