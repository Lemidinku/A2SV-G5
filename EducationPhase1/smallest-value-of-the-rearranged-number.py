class Solution:
    def smallestNumber(self, num: int) -> int:

        if num >=0:
            num_list = [x for x in str(num)]
            min_ind = 0
            for i in range(len(num_list)):
                if num_list[min_ind] > num_list[i] and num_list[i]!="0":
                    min_ind = i

            min_val = num_list.pop(min_ind)
            num_list.sort()
            result = str(min_val) + "".join(num_list)

            return int(result)
        else:
            num_list = [x for x in str(num)[1:]]
            num_list.sort(reverse=True)
            result = "".join(num_list)

            return -int(result) 

        return 0

            





