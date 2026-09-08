class Solution:
    def commonChars(self, words):
        common = list(words[0])

        for word in words[1:]:
            temp = []

            for ch in word:
                if ch in common:
                    temp.append(ch)
                    common.remove(ch)

            common = temp

        return common