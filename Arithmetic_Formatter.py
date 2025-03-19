def validate_problems(problems):
    """Validates the list of arithmetic problems based on given constraints."""
    
    # Limit the number of problems to 5
    if len(problems) > 5:
        return "Error: Too many problems."
        
    for string in problems: 
        split = string.split()  # Split problem into components (e.g., "32 + 8" -> ["32", "+", "8"])
      
        if len(split) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = split 
        
        # Check if operator is either + or -
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        # Ensure both operands are digits
        elif not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Ensure numbers are not more than four digits
        elif int(num1) > 9999 or int(num2) > 9999:
            return "Error: Numbers cannot be more than four digits."
    
    return None  # No errors found

def parse_problem(problem):
    """Parses a single problem into its components."""
    num1, operator, num2 = problem.split()
    return num1, operator, num2

def format_problem(num1, operator, num2, show_answer=False):
    """Formats a single arithmetic problem for display."""
   
    width = max(len(num1), len(num2)) + 2  # Determine width of formatted problem
    
    top_row = num1.rjust(width)  # Right-align first number
    mid_row = operator + num2.rjust(width - 1)  # Align operator and second number
    dash_row = "-" * width  # Create separator line
    
    # If show_answer is True, calculate and format the result
    if show_answer:
        result = str(int(num1) + int(num2)) if operator == "+" else str(int(num1) - int(num2))
        last_row = result.rjust(width)
        return top_row, mid_row, dash_row, last_row
    
    return top_row, mid_row, dash_row

def arithmetic_arranger(problems, show_answers=False):
    """Arranges multiple arithmetic problems in a structured format."""
    
    top = []
    middle = []
    dashes = []
    answers = []
    
    # Validate input problems
    error = validate_problems(problems)
    if error:
        return error
    
    for problem in problems:
        num1, operator, num2 = parse_problem(problem)
        formatted = format_problem(num1, operator, num2, show_answers)

        if show_answers:
            top_row, mid_row, dash_row, last_row = formatted
            answers.append(last_row)
        else:
            top_row, mid_row, dash_row = formatted

        top.append(top_row)
        middle.append(mid_row)
        dashes.append(dash_row)
    
    # Combine rows with proper spacing
    arranged_problems = "\n".join([
        "    ".join(top),
        "    ".join(middle),
        "    ".join(dashes),
    ])
    
    # If answers need to be displayed, add the last row
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)
    
    return arranged_problems

# Example test cases
print(arithmetic_arranger(["32 + 8", "1 + 3801", "9999 + 2", "523 - 49"], show_answers=False))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], show_answers=True))