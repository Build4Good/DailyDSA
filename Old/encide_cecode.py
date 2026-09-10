class Solution:
    def encode(self, strs):
        """
        @param: strs: A list of strings
        @return: A single string
        """
        encoded=[]
        for st in strs:
            s=str(len(st))+"#"+st
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s):
        """
        @param: s: A string
        @return: A list of strings
        """
        res=[]
        i=0

        while i<len(s):
            j=s.find("#",i)  ##finding location of J starting from ith Location
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        
        return res

solver=Solution()
enc=solver.encode(["lint", "code", "love", "you"])
print(enc)

print(solver.decode(enc))