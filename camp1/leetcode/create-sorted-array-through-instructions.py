class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)
        minns = [0]*n
        def countLess(left_half, right_half):
            left_half.append(float("inf"))
            left, right = 0, 0
            while left<len(left_half) and right<len(right_half):
                if left_half[left]<float("inf") and  instructions[left_half[left]] < instructions[right_half[right]]:
                    left += 1
                else:
                    minns[right_half[right]] += left
                    right+=1
            left_half.pop()

        maxxs = [0]*n
        def countGreater(left_half, right_half):
            left_half.insert(0, float('-inf'))
            left, right = len(left_half)-1, len(right_half)-1
            while left>=0 and right>=0:
                if left_half[left]>float("-inf") and instructions[left_half[left]] > instructions[right_half[right]]:
                    left -= 1
                else:
                    maxxs[right_half[right]] += len(left_half)-left-1
                    right-=1
            left_half.pop(0)

        def merge(left_half, right_half):
            i , j= 0, 0
            merged = []
            while i<len(left_half) and  j<len(right_half):
                if instructions[left_half[i]]<= instructions[right_half[j]]:
                    merged.append(left_half[i])
                    i+=1
                else:
                    merged.append(right_half[j])
                    j+=1
            merged.extend(left_half[i:])
            merged.extend(right_half[j:])
            return merged

        def mergeSort(left, right, arr):
            if left+1>=right: 
                return [arr[left]]
            mid = (right+left)//2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid, right, arr)
            countLess(left_half, right_half)
            countGreater(left_half, right_half)
            return merge(left_half, right_half)
        mergeSort(0, n, [x for x in range(n)])
        print(minns)
        print(maxxs)
        ans = 0
        for a,b in zip(minns, maxxs):
            ans += min(a,b)
        return ans % (10**9 + 7)