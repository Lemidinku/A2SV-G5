class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)


        for folder in paths:
            files = list(folder.split())
            folder_path = files[0]
            for File in files[1:]:
                file_name= File.split("(")[0]
                file_content = File.split("(")[1][:-1]
                duplicates[file_content].append(folder_path+ "/" + file_name)
        return [b for a,b in duplicates.items() if len(b)>1]
