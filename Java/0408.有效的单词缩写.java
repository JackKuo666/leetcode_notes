class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        if (word == null || abbr == null) {
            return false;
        }
        
        int i = 0;
        int j = 0;
        int m = word.length();
        int n = abbr.length();
        
        while (j < n && i < m) {
            char c = abbr.charAt(j);
            
            if (Character.isLetter(c)) {
                if (word.charAt(i++) != abbr.charAt(j++)) {
                    return false;
                }
            } else {
                if (c == '0') { // leading 0 is invalid
                    return false;
                }
                
                int num = 0;
                while (j < n && Character.isDigit(abbr.charAt(j))) {
                    num = 10 * num + abbr.charAt(j++) - '0';
                }
                
                i += num;
            }
        }
        
        return j == n && i == m;
    }
}
