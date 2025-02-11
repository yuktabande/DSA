def groupAnagrams(strs):
    anagram_dict = {} 
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    return list(anagram_dict.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
