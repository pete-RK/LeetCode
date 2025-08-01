class Solution {
    public String findSmallestRegion(List<List<String>> regions, String region1, String region2) {
        Map<String, String> parent = new HashMap<>();
        Set<String> check = new HashSet<>();
        for (List<String> region : regions){
            for ( int i = 1; i < region.size(); i++) {
                parent.put(region.get(i), region.get(0));
            }
        }
        
        check.add(region1);
        while (parent.containsKey(region1)) {
            region1 = parent.get(region1);
            check.add(region1);
        } while (!check.contains(region2)) {
            region2 = parent.get(region2);
        }
        return region2;
    }
}