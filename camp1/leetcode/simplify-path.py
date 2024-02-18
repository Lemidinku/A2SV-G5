class Solution:
    def simplifyPath(self, path: str) -> str:
        pathes = path.split("/")
        stack = []
        
        for path in pathes:
            if not path or path==".": continue
            if path=="..":
                if stack: stack.pop()
            
            else:
                stack.append(path)


        return "/"+"/".join(stack)