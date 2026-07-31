class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for strng in strs: 
            letter_freq = [0] * 26
            for char in strng:
                letter_freq[ord(char) - ord('a')] += 1
            
            mapping[tuple(letter_freq)].append(strng)
        
        return list(mapping.values())