class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def flip_invert(lis):
            #use two pointers
            i=0
            j=len(lis)-1
            while i<j:
                #reverse the list
                lis[i], lis[j] = (lis[j]+1)%2, (lis[i]+1)%2 #invert while flipping
                i+=1
                j-=1
            # modify the middle element if len(lis) is odd
            if i==j: lis[i] = (lis[i]+1)%2

            return lis
        #modify the image in-place
        for i in range(len(image)):
            image[i] = flip_invert(image[i])
        return image
