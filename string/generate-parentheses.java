class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        backtracking(n, 0, 0, "", res);
        return res;
        
    }
    public void backtracking(int n, int openC, int closedC, String curr, List<String> res){
        if (openC + closedC == 2*n){
            res.add(curr);
            return;
        }

        if (openC < n){
            backtracking(n, openC+1, closedC, curr+"(", res);
        }

        if (closedC < openC){
            backtracking(n, openC, closedC+1, curr+")", res);
        }

    }
}