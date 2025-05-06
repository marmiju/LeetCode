class Solution:
    def search(self, a: List[int], tar: int) -> int:
        st = 0; end=len(a)-1

        while(st<=end):
            mid = st + (end -st)//2
            if a[mid] ==tar:
                return mid
            if (a[st]<= a[mid]): #left sorted
                if a[st] <= tar and tar <= a[mid]:
                    end = mid -1
                else:
                    st = mid +1
            else: #right sorted
                if a[mid] <= tar and tar <= a[end]:
                    st = mid + 1
                else:
                    end =mid -1

        return -1        





        