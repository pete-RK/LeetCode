class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if not set(s2).issubset(set(s1)):
            return 0
        
        s1_count, s2_count = 0, 0
        s1_len, s2_len = len(s1), len(s2)
        
        index_s1, index_s2 = 0, 0
        index_map = {}

        while s1_count < n1:
            if s1[index_s1] == s2[index_s2]:
                index_s2 += 1
                if index_s2 == s2_len:
                    s2_count += 1
                    index_s2 = 0
            index_s1 += 1
            if index_s1 == s1_len:
                s1_count += 1
                index_s1 = 0
                
                if (index_s1, index_s2) in index_map:
                    prev_s1_count, prev_s2_count = index_map[(index_s1, index_s2)]
                    cycle_len = s1_count - prev_s1_count
                    cycle_count = (n1 - s1_count) // cycle_len
                    s1_count += cycle_count * cycle_len
                    s2_count += cycle_count * (s2_count - prev_s2_count)
                
                index_map[(index_s1, index_s2)] = (s1_count, s2_count)
        
        return s2_count // n2