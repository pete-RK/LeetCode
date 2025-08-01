class Solution {
    public String applySubstitutions(List<List<String>> replacements, String text) {
        Map<String, String> reps = new HashMap<>();
        for(int i=0; i<replacements.size(); i++) {
            reps.put(replacements.get(i).get(0), replacements.get(i).get(1));
        }

        while(text.contains("%")) {
            StringBuilder output = new StringBuilder();
            String[] split = text.split("%");
            for(int i=0; i<split.length; i++) {
                if(i%2==0) {
                    output.append(split[i]);
                } else {
                    output.append(reps.get(split[i]));
                }
            }
            text = output.toString();
        };

        return text;
    }
}