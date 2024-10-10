class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        translations = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r", "s"],
            8:["t","u","v"],
            9:["w","x","y", "z"],
        }

        def dfs(str):
            if(len(str) == 0):
                return [""]
            else:
                starts = translations[int(str[0])]
                ends = dfs(str[1:])
                res = []
                for start in starts:
                    for end in ends:
                        res.append(start + end)
                return res
        
        if(digits == ""):
            return []
        return dfs(digits)
