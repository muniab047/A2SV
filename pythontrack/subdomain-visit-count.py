class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dic=defaultdict(int)
        fans=[]

        for cpdomain in cpdomains:
            ans=[]
            n, site= cpdomain.split()
            for i in range(len(site)-1,-1,-1):
                if site[i]=='.':
                    ans.append(n+" "+site[i+1:])

            ans.append(n+" "+site[:])

            for site in ans:
                n,s=site.split()
                n=int(n)

                dic[s]=dic[s]+n

        for key in dic:
            fans.append(f'{dic[key]} {key}')

        return fans




            

        


        