class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        # Initialize variables
        first_person = -1  # Index of first person
        last_person = -1   # Index of last person
        max_distance = 0   # Maximum distance to closest person
        
        # Find all people and compute distances
        for i in range(n):
            if seats[i] == 1:
                if first_person == -1:
                    # Distance from start to first person
                    first_person = i
                    max_distance = first_person
                else:
                    # Distance between consecutive people
                    max_distance = max(max_distance, (i - last_person) // 2)
                last_person = i
        
        # Distance from last person to end
        if last_person != n - 1:
            max_distance = max(max_distance, n - 1 - last_person)
        
        return max_distance
                
                