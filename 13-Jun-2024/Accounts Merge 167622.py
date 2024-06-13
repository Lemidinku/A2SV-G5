# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                parent[(name, email)] = (name,email)
        # print(parent)
        
        def find(i):
            if parent[i]==i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
             
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX!=parentY:
                parent[parentX] = parentY

        for account in accounts:
            name = account[0]
            for i in range(1,len(account)-1):
                union((name,account[i]), (name, account[i+1]))
        
        groups = defaultdict(list)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in groups[find((name,email))]:
                    groups[find((name,email))].append(email)

        ans = [[] for _ in range(len(groups))]
        for i, group in enumerate(groups):
            ans[i].append(group[0])
            groups[group].sort()
            for email in groups[group]:
                ans[i].append(email)

        # print(groups)
            



        return ans

            