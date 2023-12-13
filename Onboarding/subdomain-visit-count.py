
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        table = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            domains = list(domain.split("."))
            for i in range(len(domains)):
                table[".".join(domains[i:])] += int(count)
        return [str(b)+ " " + a for a, b in table.items()]