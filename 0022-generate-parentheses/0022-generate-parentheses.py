class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(current, left, right, result):
            if left == 0 and right == 0:
                result.append(current)
                return
            if left > 0:
                generate(current + '(', left - 1, right, result)
            if right > left:
                generate(current + ')', left, right - 1, result)

        result = []
        generate('', n, n, result)
        return result