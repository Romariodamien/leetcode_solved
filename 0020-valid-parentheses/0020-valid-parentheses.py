class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={"[":"]","(":")","{":"}"}
        for i in s:
            if i in d.keys():
                st.append(i)
            else:
                if st==[]:
                    return 0
                else:
                    if d[st[-1]] == i:
                        st.pop()
                    else:
                        return 0
        if st==[]:
            return 1
        else:
            return 0