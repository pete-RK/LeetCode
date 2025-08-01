class MedianFinder {
    private PriorityQueue<Integer> small;
    private PriorityQueue<Integer> large;
    private int length;

    public MedianFinder() {
        small = new PriorityQueue<>((a, b) -> b - a);
        large = new PriorityQueue<>();
        length = 0;
    }
    
    public void addNum(int num) {
        if (length == 0 || num < small.peek()) {
            small.offer(num);
        } else {
            large.offer(num);
        }
        
        if (small.size() > large.size() + 1) {
            large.offer(small.poll());
        } else if (large.size() > small.size()) {
            small.offer(large.poll());
        }
        
        length++;
    }
    
    public double findMedian() {
        if (length % 2 == 1) {
            return (double) small.peek();
        } else {
            return (small.peek() + large.peek()) / 2.0;
        }
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */