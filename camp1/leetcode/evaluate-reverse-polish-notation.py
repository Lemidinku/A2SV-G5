class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expression = []
        for token in tokens:
            if token in ("*","+", "-", "/"):
                value2 = expression.pop()
                value1 = expression.pop()
                match token:
                    case "*": expression.append(value1*value2)
                    case "/": expression.append(int(value1/value2))
                    case "+": expression.append(value1+value2)
                    case "-": expression.append(value1-value2)

            else:
                expression.append(int(token))
        return expression[-1]

