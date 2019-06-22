class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and abbr[j] != '0':
                num = ''
                while j < len(abbr) and abbr[j].isdigit():
                    num += abbr[j]
                    j += 1
                
                i += int(num)
            else:
                return False
                
        return i == len(word)
