class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        track = set()
        maxl = 0
        counter = 0 
        index = 0
        for i in range(len(fruits)):
            if fruits[i] not in track and len(track) < 2:
                track.add(fruits[i])
                counter += 1
                index = i
            elif fruits[i] in track:
                counter += 1
                if fruits[i] != fruits[i-1]:
                    index = i
            else:
                track.clear()
                track.add(fruits[index])
                track.add(fruits[i])
                counter = i - index +1
                index = i
            maxl = max(maxl,counter)
        return maxl

