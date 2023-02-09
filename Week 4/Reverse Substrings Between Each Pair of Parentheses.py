class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for n in s:
            if n == ")":
                x = []
                while not stack[-1] == '(':
                    x.append(stack.pop())
                stack.pop()
                stack = stack + x
            else:
                stack.append(n)
        return "".join(stack)