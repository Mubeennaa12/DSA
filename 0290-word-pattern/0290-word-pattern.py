class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for ch, word in zip(pattern, words):
            if ch not in char_to_word:
                char_to_word[ch] = word
            if word not in word_to_char:
                word_to_char[word] = ch
            if char_to_word[ch] != word or word_to_char[word] != ch:
                return False
        return True