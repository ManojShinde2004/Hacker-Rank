class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ones = []
        answer = ""

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

                if len(ones) >= k:
                    left = ones[-k]

                    while left < i and s[left] == '0':
                        left += 1

                    current = s[left:i+1]

                    if answer == "" or len(current) < len(answer) or (len(current) == len(answer) and current < answer):
                        answer = current

        return answer