class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        
        l=sentence.split()
        n=len(l)
        v=['a','e','i','o','u','A','E','I','O','U']
        
        res=[]
        for i in range(len(l)):
            k='ma'
            st=l[i]
            p='a'
            rr=p*(i+1)
            k=k+rr

            if(st[0] in v):
                st=st+k
                res.append(st)
                
            if(st[0] not in v):
                ll=[]
                for i in st:
                    ll.append(i)
                
                mm=ll.pop(0)
                ll.append(mm)
                ms=""
                for i in ll:
                    ms+=i
                
                ms=ms+k
                res.append(ms)

            k=""
                  
        
        fres = ""
        for i in res:
            fres = fres + i 
            fres = fres + ' '

        return fres.strip()
        





        
