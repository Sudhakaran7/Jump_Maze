class Solution(object):
    def reachDesti(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k%2
val=Solution()
reach=int(input())
print(val.reachDesti(reach))
