class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pre = []
        summ =0
        ones = 0
        for num in boxes:
            summ += ones
            pre.append(summ)
            if int(num): ones += 1
        post = []
        summ =0
        ones = 0
        for  i in  range(len(boxes)-1, -1, -1):
            summ += ones
            post.insert(0,summ)
            if int(boxes[i]): ones += 1
        return [a+b  for a,b in zip(pre,post)]







        return []
        # [0,1,0,0,0,1,0,1,1]
        # [0,0,1,2,3,4,6,1,1]
