class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        index = 0
        for id, charr in enumerate(s):
            import pdb
            pdb.set_trace()
            if id < index:
                break

            if charr == "I":
                if id != len(s)-1 and s[id+1] == "V":
                    num += 4
                    index += 2
                elif id != len(s) - 1 and s[id+1] =="X":
                    num += 9
                    index += 2
                else:
                    num += 1
                    index += 1
            elif charr == "V":
                num += 5
                index += 1
            elif charr == "X":
                if id != len(s)-1 and s[id+1] == "L":
                    num += 40
                    index += 2
                elif id != len(s) - 1 and s[id+1] =="C":
                    num += 90
                    index += 2
                else:
                    num += 10
                    index += 1
            elif charr == "L":
                num += 50
                index += 1
            elif charr == "C":
                if id != len(s)-1 and s[id+1] == "D":
                    num += 400
                    index += 2
                elif id != len(s) - 1 and s[id+1] =="M":
                    num += 900
                    index += 2
                else:
                    num += 100
                    index += 1
            elif charr == "D":
                num += 500
                index += 1 
            elif charr == "M":
                num += 1000
                index += 1
        return num
                

                
if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))