class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        window_start = 0
        max_length = 0
        fruit_count = {}
        for window_end in range(len(fruits)):
            fruit = fruits[window_end]
            if fruit not in fruit_count:
                fruit_count[fruit] = 0
            fruit_count[fruit] += 1
            while len(fruit_count) > 2:
                fruit = fruits[window_start]
                fruit_count[fruit] -= 1
                if fruit_count[fruit] == 0:
                    del fruit_count[fruit]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
        