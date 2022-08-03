class MyCalendar:
# https://www.youtube.com/watch?v=_owsTIT2JbQ
    def __init__(self):
        self.cal = [(0,0),(10**9,10**9)]
        

    def book(self, start: int, end: int) -> bool:
        #binary search
        l,r = 0,len(self.cal)
        while l<r:
            mid = (l+r)//2
            if end == self.cal[mid][0]:
                l = mid
                break
            elif end>self.cal[mid][0]:
                l = mid+1
            else:
                r = mid
        # l index
        if start < self.cal[l-1][1]:
            return False
        self.cal.insert(l,(start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)