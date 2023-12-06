class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        for i,word in enumerate(list1):
            if word not in index_map:
                index_map[word] = i
        print(index_map)
        min_index_sum = float('inf') 
        common_words = []
        for j, word2 in enumerate(list2):
            if word2 in index_map:
                ind_word1 = index_map[word2]
                if  j+ind_word1 < min_index_sum:
                    common_word = [word2]
                    min_index_sum = j+ind_word1
                elif j+ind_word1 == min_index_sum:
                    common_word.append(word2)
        # return min_index_sum
        return common_word


  