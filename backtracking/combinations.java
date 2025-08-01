class Solution {
    List<List<Integer>> list = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        List<Integer> temp = new ArrayList<>();
        backtrack(1, n, k, temp);
        return list;    
    }

    private void backtrack(int start, int n, int k, List<Integer> temp){
        if(k == 0){
            list.add(new ArrayList<>(temp));
            return;
        }

        for(int i = start; i <= n; i++){
            temp.add(i);
            backtrack(i + 1, n, k - 1, temp);
            temp.remove(temp.size() - 1);
        }
    }
}