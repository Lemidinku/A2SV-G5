class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ["a", "e", "i", "o", "u"]
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels: vowel_count +=1
        max_count = vowel_count
        right = k
        for left in range(n-k):
            if s[left] in vowels: vowel_count-=1
            if s[right] in vowels: vowel_count+=1

            max_count = max(max_count,vowel_count)

            right+=1
        return max_count
