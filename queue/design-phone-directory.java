class PhoneDirectory {
    private Set<Integer> phone;
    private List<Integer> assign;

    public PhoneDirectory(int maxNumbers) {
        phone = new HashSet<>();
        assign = IntStream.rangeClosed(0, maxNumbers - 1)
                         .boxed()
                         .sorted(Comparator.reverseOrder())
                         .collect(Collectors.toCollection(ArrayList::new));
    }
    
    public int get() {
        if (assign.isEmpty()) {
            return -1;
        }
        int val = assign.remove(assign.size() - 1);
        phone.add(val);
        return val;
    }
    
    public boolean check(int number) {
        return !phone.contains(number);
    }
    
    public void release(int number) {
        if (!phone.contains(number)) {
            return;
        }
        phone.remove(number);
        assign.add(number);
    }
}

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * boolean param_2 = obj.check(number);
 * obj.release(number);
 */