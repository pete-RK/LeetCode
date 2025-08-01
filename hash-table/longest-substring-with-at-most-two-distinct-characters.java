class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        HashMap<Character, Integer> charMap = new HashMap<>();
        int l = 0, res = 0;

        for (int r = 0; r < s.length(); r++) {
            char rightChar = s.charAt(r);
            charMap.put(rightChar, charMap.getOrDefault(rightChar, 0) + 1);

            while (charMap.size() > 2){
                char leftChar = s.charAt(l);
                charMap.put(leftChar, charMap.get(leftChar) - 1);
                if (charMap.get(leftChar) == 0) {
                    charMap.remove(leftChar);
                }
                l++;
            }

            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}