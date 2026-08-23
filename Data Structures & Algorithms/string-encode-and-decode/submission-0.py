class Solution:

    def encode(self, strs: List[str]) -> str:

        result = "" 
        for s in strs: 
            result += str(len(s)) + "#" + s 

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 
        # this part is reading the length like i:j slicing
        while i < len(s): 
            j = i 
            while s[j] != "#":
                j+=1

            length = int(s[i:j]) #grab the number
            j += 1
            
            result.append(s[j:j+length])
            i = j + length
        return result 


