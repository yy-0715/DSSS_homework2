import random


def get_random_integer(min, max):
    """
    Generate a random integer in the range.

    Args:
        min (int): The minimum value for the random integer.
        max (int): The maximum value for the random integer.

    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(min, max)


def get_random_operater():
    """
    Select a random mathmetical operater from '+', '-' and '*'.

    Returns:
        str: A random operater within '+', '-' and '*'.
    """
    return random.choice(['+', '-', '*'])


def calculate_expression(number1, number2, operater):
    """
    Get and calculate the expression based on the provided numbers and operater.
    """
    expression = f"{number1} {operater} {number2}"
    try:
        if operater == '+':
            answer = number1 + number2
        elif operater == '-':
            answer = number1 - number2
        elif operater == '*':
            answer = number1 * number2
        else:
            raise ValueError("Invalid operator. Choose from '+', '-', or '*'.")
    except ValueError as e:
        print(f"Error: {e}")
        answer = None
    return expression, answer

def math_quiz():
    """
    A math quiz game where the player is asked to solve math problems.
    """
    score = 0
    total_question = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question):
        # Get two random numbers and an operator
        number1 = get_random_integer(1, 10)
        number2 = get_random_integer(-10, 5)
        operater = get_random_operater()

        problem, correct_answer = calculate_expression(number1, number2, operater)
        print(f"\nQuestion: {problem}")

        try:
            # Get user input and convert it to integer
            useranswer = int(input("Your answer: "))
        
            # Check if the user's answer is correct
            if useranswer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_question}")

if __name__ == "__main__":
    math_quiz()
