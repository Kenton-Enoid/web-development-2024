# First we need to create a main function

def recursive_expression(expression):
    # Make sure we remove the spaces between the expression
    expression = expression.replace(" ", "")

    # Define a function: Checks if string expression is a valid number
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
    # Define a function: Recursive helper function to evaluate the expression
    def evaluate_helper(expr):
        if is_number(expr):
            return expr
        
        #If not a single number then break it down into pieces using a while loop
        while "(" in expr:
            start = expr.rfind("(")
            end = expr.find(")", start)
            inner_expr = expr[start + 1:end]
            result = evaluate_helper(inner_expr)
            expr = expr[:start] + result + expr[end + 1:]

        
        # Evaluate multiplication and division 
        for op in ["*", "/"]:
            if op in expr:
                sides = expr.split(op, 1)
                if len(expr) == 2:
                    left_side, right_side = sides
                    left_result = evaluate_helper(left_side)
                    right_result = evaluate_helper(right_side)

                # Checks for invalid expression
                if left_result == "Invalid Expression" or right_result == "Invalid Expression":
                    return "Invalid Expression"
                
                # Checks for division by 0
                if op == "/" and float(right_result) == 0:
                    return "Invalid Expression"

                # Multiplication
                if op == "*":
                    result = str(float(left_result) * float(right_result))
                else:
                    result = str(float(left_result) / float(right_result))

                return evaluate_helper(result)


        # # Evaluate addition and subtraction
        # for op in ["+", "-"]:
        #     if op in expr:
        #         sides = expr.split(op, 1)
            
        return "Invalid Expression"
        
    return recursive_expression(expression)





        

