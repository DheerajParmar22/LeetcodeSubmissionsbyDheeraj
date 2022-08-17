class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        map = {
            "a":".-",
            "b":"-...",
            "c":"-.-.",
            "d":"-..",
            "e":".",
            "f":"..-.",
            "g":"--.",
            "h":"....",
            "i":"..",
            "j":".---",
            "k":"-.-",
            "l":".-..",
            "m":"--",
            "n":"-.",
            "o":"---",
            "p":".--.",
            "q":"--.-",
            "r":".-.",
            "s":"...",
            "t":"-",
            "u":"..-",
            "v":"...-",
            "w":".--",
            "x":"-..-",
            "y":"-.--",
            "z":"--.."
        }
        
        s = ''
        l = list()
        for i in words:
            for c in i:
                s += map[c]
            l.append(s)
            s = ''
        return len(set(l))
        