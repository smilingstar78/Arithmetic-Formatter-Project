def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    answers = []

    for problem in problems:
        parts = problem.split()  # corrected variable name
        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]

        # Validation checks
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)

        # Calculate answers within the loop
        if operator == '+':
            answers.append(str(int(first_operand) + int(second_operand)))
        else:
            answers.append(str(int(first_operand) - int(second_operand)))

    first_line = ""
    second_line = ""
    third_line = ""
    answer_line = ""

    # Loop to format each problem
    for i in range(len(problems)):
        first = first_operands[i]
        second = second_operands[i]
        operator = operators[i]
        answer = answers[i]

        width = max(len(first), len(second)) + 2  # width for alignment

        first_line += first.rjust(width)
        second_line += operator + second.rjust(width - 1)
        third_line += '-' * width
        if show_answers:
            answer_line += answer.rjust(width)

        # Add spacing between problems except for the last one
        if i < len(problems) - 1:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            if show_answers:
                answer_line += "    "

    # Assemble the final arranged string
    if show_answers:
        arranged_problems = f"{first_line}\n{second_line}\n{third_line}\n{answer_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{third_line}"

    return arranged_problems

# Test the function
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
