class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0: return '0'
        ans=[]
        if (numerator<0)^(denominator<0): ans.append('-')
        num=abs(numerator)
        den=abs(denominator)

        q, r=divmod(num, den)
        ans.append(str(q))

        if r==0: return "".join(ans)
        ans.append('.')
        mp={}
        frac=[]
        
        i=0
        while r!=0:
            if r in mp:
                frac.insert(mp[r], '(')
                frac.append(')')
                break
            mp[r]=i
            r*=10
            frac.append(str(r//den))
            r%=den
            i+=1
        return "".join(ans+frac)