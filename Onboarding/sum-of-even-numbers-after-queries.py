class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum([x for x in nums if x%2==0])
        for val,i in queries:

            if nums[i]%2==0:
                even_sum -= nums[i]

            new_num =  nums[i] + val
            nums[i] += val
            if new_num%2==0:
                even_sum += new_num
            result.append(even_sum)

        return result


