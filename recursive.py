# def evaluate_expression(expression):
#     def is_valid(expr):
#         # Function to check if an expression is valid
#         stack = []
#         for char in expr:
#             if char == '(':
#                 stack.append(char)
#             elif char == ')':
#                 if not stack:
#                     return False
#                 stack.pop()
#         return not stack

#     def evaluate_helper(expr):
#         # Helper function for recursive evaluation
#         if is_valid(expr):
#             # Base case: if the expression is a single number, return it
#             if expr.isdigit() or (expr[0] == '-' and expr[1:].isdigit()):
#                 return expr

#             # Evaluate expressions within parentheses first
#             while '(' in expr:
#                 start = expr.rfind('(')
#                 end = expr.find(')', start)
#                 inner_expr = expr[start + 1:end]
#                 result = evaluate_helper(inner_expr)
#                 expr = expr[:start] + result + expr[end + 1:]

#             # Evaluate multiplication and division
#             for op in ['*', '/']:
#                 operator_index = expr.find(op)
#                 while operator_index != -1:
#                     left_operand = evaluate_helper(expr[:operator_index])
#                     right_operand = evaluate_helper(expr[operator_index + 1:])
#                     if op == '*':
#                         result = str(float(left_operand) * float(right_operand))
#                     else:
#                         result = str(float(left_operand) / float(right_operand))
#                     expr = expr[:operator_index - len(left_operand)] + result + expr[operator_index + 1 + len(right_operand):]
#                     operator_index = expr.find(op)

#             # Evaluate addition and subtraction
#             for op in ['+', '-']:
#                 operator_index = expr.rfind(op)
#                 if operator_index != -1:
#                     left_operand = evaluate_helper(expr[:operator_index])
#                     right_operand = evaluate_helper(expr[operator_index + 1:])
#                     if op == '+':
#                         result = str(float(left_operand) + float(right_operand))
#                     else:
#                         result = str(float(left_operand) - float(right_operand))
#                     return result

#         return "Invalid Expression"

#     # Remove spaces from the expression
#     expression = expression.replace(" ", "")

#     # Call the helper function to start the recursive evaluation
#     return evaluate_helper(expression)

# # Test cases
# print(evaluate_expression("3 + 12 * 3 / 12"))  # Output: 6.0
# print(evaluate_expression("(3 + 3) * 42 / (6 + 12)"))  # Output: 14.0
# print(evaluate_expression("4 (12E)"))  # Output: Invalid Expression
# print(evaluate_expression("4 (41)"))  # Output: Invalid Expression
# print(evaluate_expression("42+43**271"))  # Output: Invalid Expression



# Certainly! Let's break down the code and discuss each part:

# is_valid(expr): This function checks the validity of the expression by ensuring that the parentheses are balanced. It uses a stack to keep track of open parentheses and verifies that each closing parenthesis has a corresponding open parenthesis.

# evaluate_helper(expr): This is a recursive helper function that performs the actual evaluation of the expression. It has the following steps:

# a. If the expression is a single number (integer or float), it returns the expression as is.

# b. It iteratively evaluates expressions within parentheses, starting from the innermost parentheses and working outward.

# c. It then evaluates multiplication and division, and finally addition and subtraction, considering the order of operations.

# d. The function returns the result as a string.

# e. If at any point the expression becomes invalid (due to division by zero or other errors), it returns "Invalid Expression."

# The main function evaluate_expression(expression) first removes any spaces from the input expression and then calls the evaluate_helper function with the cleaned expression.

# Test cases demonstrate the usage of the algorithm with different expressions.

# Now, let's consider an alternative approach using the eval function. While using eval has some security concerns because it can execute arbitrary code, it simplifies the implementation for simple mathematical expressions:



# For beginner level:

def evaluate_expression(expression):
    # Remove spaces from the expression
    expression = expression.replace(" ", "")

    # Define a function to check if a string represents a valid number
    def is_number(s):
        if s[0] == '-' and s[1:].isdigit():
            return True
        return s.isdigit()

    # Recursive helper function to evaluate the expression
    def evaluate_helper(expr):
        # Base case: if the expression is a number, return it
        if is_number(expr):
            return expr

        # Evaluate expressions within parentheses first
        while '(' in expr:
            start = expr.rfind('(')
            end = expr.find(')', start)
            inner_expr = expr[start + 1:end]
            result = evaluate_helper(inner_expr)
            expr = expr[:start] + result + expr[end + 1:]

        # Evaluate multiplication and division
        for op in ['*', '/']:
            if op in expr:
                parts = expr.split(op, 1)
                if len(parts) == 2:
                    left_operand, right_operand = parts
                    left_result = evaluate_helper(left_operand)
                    right_result = evaluate_helper(right_operand)

                    # Check for 'Invalid Expression' in operands
                    if left_result == 'Invalid Expression' or right_result == 'Invalid Expression':
                        return 'Invalid Expression'

                    # Check for division by zero
                    if op == '/' and float(right_result) == 0:
                        return 'Invalid Expression'

                    # Perform the operation
                    if op == '*':
                        result = str(float(left_result) * float(right_result))
                    else:
                        result = str(float(left_result) / float(right_result))

                    return evaluate_helper(result)

        # Evaluate addition and subtraction
        for op in ['+', '-']:
            if op in expr:
                parts = expr.rsplit(op, 1)
                if len(parts) == 2:
                    left_operand, right_operand = parts
                    left_result = evaluate_helper(left_operand)
                    right_result = evaluate_helper(right_operand)

                    # Check for 'Invalid Expression' in operands
                    if left_result == 'Invalid Expression' or right_result == 'Invalid Expression':
                        return 'Invalid Expression'

                    # Perform the operation
                    if op == '+':
                        result = str(float(left_result) + float(right_result))
                    else:
                        result = str(float(left_result) - float(right_result))

                    return evaluate_helper(result)

        return "Invalid Expression"

    return evaluate_helper(expression)

# Test cases
print(evaluate_expression("3 + 12 * 3 / 12"))  # Output: 6.0
print(evaluate_expression("(3 + 3) * 42 / (6 + 12)"))  # Output: 14.0
print(evaluate_expression("4 (12E)"))  # Output: Invalid Expression
print(evaluate_expression("4 (41)"))  # Output: Invalid Expression
print(evaluate_expression("42+43**271"))  # Output: Invalid Expression



expr = "2 * (3 + 4)"
start = expr.rfind('(')  # Returns the index of '(' in "2 * (3 + 4)", which is 4
end = expr.find(')', start)  # Returns the index of ')' in "2 * (3 + 4)", which is 9
inner_expr = expr[start + 1:end]  # Extracts the inner expression "3 + 4"
result = "7"  # Suppose this is the evaluated result of "3 + 4"

# Now, the line of code replaces the inner expression with its result:
expr = expr[:start] + result + expr[end + 1:]
