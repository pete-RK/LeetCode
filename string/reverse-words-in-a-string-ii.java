class Solution {
    private void reverse(char[] s, int start, int end) {
        while (start < end) {
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;

            start++;
            end--;
        }
    }
    public void reverseWords(char[] s) {
        reverse(s, 0, s.length-1);
        int start = 0;
        
        for (int i = 0; i < s.length; i++) {
            if (s[i] == ' ') {
                reverse(s, start, i-1);
                start = i + 1;
            }
            else if (i == s.length-1){
                reverse(s, start, i);
            }
        }
    }
}