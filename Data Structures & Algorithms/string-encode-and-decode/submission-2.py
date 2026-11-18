class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeRes = ""
        for string in strs:
            length = len(string)
            encodeRes += str(length) + "#"
            encodeRes += string
        print("encode: " + encodeRes)
        return encodeRes
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == "0":
                res.append("")
                i += 2
                continue
            else:
                number = ""
                while s[i] != "#":
                    number += s[i]
                    i += 1
                i += 1
                word = ""
                print("index: " + str(i))
                print(number)
                j = 0
                while i < len(s) and j < int(number):
                    word += s[i]
                    i += 1
                    j += 1

                print(word)
                res.append(word)
            
                print()
                

        

        return res