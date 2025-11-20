# -*- coding: utf-8 -*-
# Multi-Purpose Problem Solver
# A comprehensive solution for various coding challenges including sports calculations,
# game rules, health assessments, and mathematical operations.

class ProblemSolver:
    # A multi-purpose problem solver that handles various coding challenges
    # from sports calculations to game rules and health assessments.
    
    def calculate_sports_score(self):
        # Calculate the final score based on time remaining and current score.
        # Used in sports games where points are awarded every 5 minutes.
        # Input format: time score (e.g., "45 2")
        # Get input values for time and current score
        a, b = input().split()
        # Convert inputs to integers
        a = int(a)
        b = int(b)
        
        # Check if current time is a multiple of 10
        if a % 10 == 0:
            # If time is multiple of 10, calculate exact additional points
            # Points are awarded every 5 minutes until 90 minutes
            c = b + int((90 - a) / 5)
        else:
            # If time is not multiple of 10, add one extra point for partial period
            c = b + int((90 - a) / 5) + 1
        
        # Print the final calculated score
        print(c)

    def check_win_condition(self):
        # Check if a number meets win conditions:
        # - Between 50 and 70 (inclusive)
        # - Divisible by 6
        # Otherwise, it's a loss.
        # Get input number from user
        a = int(input())
        
        # Check win conditions
        if 50 <= a <= 70:
            # Number is between 50 and 70 inclusive
            print('win')
        elif a % 6 == 0:
            # Number is divisible by 6
            print('win')
        else:
            # Number doesn't meet any win condition
            print('lose')

    def check_lucky_calculation(self):
        # Check if (a - b + c) is divisible by 10.
        # If divisible, print 'Lucky', otherwise 'So-so'.
        # Input format: three numbers separated by spaces
        # Get three input numbers
        a, b, c = map(int, input().split())
        
        # Check if the calculation result is divisible by 10
        if (a - b + c) % 10 == 0:
            print('Lucky')
        else:
            print('So-so')

    def check_height_safety(self):
        # Check if all three heights are above 170.
        # If any height is 170 or below, print 'CRASH', otherwise 'PASS'.
        # Input format: three heights separated by spaces
        # Get three height values
        a, b, c = map(int, input().split())
        
        # Check if any height is 170 or less
        if a <= 170 or b <= 170 or c <= 170:
            print('CRASH')
        else:
            print('PASS')

    def check_even_odd(self):
        # Check if a number is even or odd.
        # Simple even/odd determination using modulo operator.
        # Get input number
        n = int(input())
        
        # Check if number is even (divisible by 2)
        if n % 2 == 0:
            print('even')
        else:
            print('odd')

    def calculate_obesity_level_simple(self):
        # Calculate obesity level using simple formula:
        # Standard weight = (height - 100) × 0.9
        # Obesity rate = (current weight - standard weight) × 100 / standard weight
        # Categories: Normal (≤10%), Overweight (10-20%), Obese (>20%)
        # Get height and weight inputs
        a, b = map(float, input().split())
        
        # Calculate standard weight using simple formula
        c = (a - 100) * 0.9
        # Calculate obesity rate as percentage
        d = (b - c) * 100 / c
        
        # Determine obesity category based on percentage
        if d <= 10:
            print('Normal')
        elif 10 < d <= 20:
            print('Overweight')
        else:
            print('Obese')

    def calculate_obesity_level_detailed(self):
        # Calculate obesity level with detailed height-based standard weight calculation.
        # Different formulas for different height ranges:
        # - Under 150cm: height - 100
        # - 150-159cm: (height - 150)/2 + 50
        # - 160cm and above: (height - 100) × 0.9
        # Get height and weight inputs
        h, w = map(float, input().split())
        s = 0  # Initialize standard weight variable
        
        # Calculate standard weight based on height range
        if h < 150:
            # Formula for heights under 150cm
            s = h - 100
        elif 150 <= h < 160:
            # Formula for heights between 150-159cm
            s = ((h - 150) / 2) + 50
        else:
            # Formula for heights 160cm and above
            s = (h - 100) * 0.9
        
        # Calculate obesity rate percentage
        o = ((w - s) * 100) / s
        
        # Determine obesity category
        if o <= 10:
            print("Normal")
        elif 10 < o <= 20:
            print("Overweight")
        else:
            print("Obese")

    def add_two_numbers(self):
        # Simple addition of two numbers.
        # Basic arithmetic operation demonstrating input handling.
        # Get first number
        a = int(input())
        # Get second number
        b = int(input())
        # Calculate and print sum
        print(a + b)

    def display_menu(self):
        # Display the main menu options to the user.
        # Shows all available problem-solving functions.
        print("\n" + "=" * 50)
        print("MULTI-PURPOSE PROBLEM SOLVER")
        print("=" * 50)
        print("1. Calculate Sports Score")
        print("2. Check Win Condition")
        print("3. Check Lucky Calculation")
        print("4. Check Height Safety")
        print("5. Check Even/Odd")
        print("6. Calculate Obesity Level (Simple)")
        print("7. Calculate Obesity Level (Detailed)")
        print("8. Add Two Numbers")
        print("9. Exit")
        print("=" * 50)

    def run_example(self, choice):
        # Execute the selected problem-solving function based on user choice.
        # Provides appropriate prompts and calls the corresponding method.
        if choice == 1:
            print("\nSports Score Calculation")
            print("-" * 30)
            print("Enter time and score (e.g., '45 2'): ")
            self.calculate_sports_score()
        elif choice == 2:
            print("\nWin Condition Check")
            print("-" * 30)
            print("Enter a number: ")
            self.check_win_condition()
        elif choice == 3:
            print("\nLucky Calculation")
            print("-" * 30)
            print("Enter three numbers (e.g., '15 5 10'): ")
            self.check_lucky_calculation()
        elif choice == 4:
            print("\nHeight Safety Check")
            print("-" * 30)
            print("Enter three heights (e.g., '175 180 165'): ")
            self.check_height_safety()
        elif choice == 5:
            print("\nEven/Odd Check")
            print("-" * 30)
            print("Enter a number: ")
            self.check_even_odd()
        elif choice == 6:
            print("\nObesity Calculation (Simple)")
            print("-" * 30)
            print("Enter height and weight (e.g., '170 65'): ")
            self.calculate_obesity_level_simple()
        elif choice == 7:
            print("\nObesity Calculation (Detailed)")
            print("-" * 30)
            print("Enter height and weight (e.g., '155 50'): ")
            self.calculate_obesity_level_detailed()
        elif choice == 8:
            print("\nAdd Two Numbers")
            print("-" * 30)
            print("Enter first number: ")
            print("Enter second number: ")
            self.add_two_numbers()

def main():
    # Main function to run the problem solver application.
    # Handles the main program loop and user interaction.
    # Create problem solver instance
    solver = ProblemSolver()
    
    # Display welcome message
    print("Welcome to Multi-Purpose Problem Solver!")
    print("This program solves various coding problems including:")
    print("- Sports score calculations")
    print("- Game win conditions")
    print("- Health assessments")
    print("- Mathematical operations")
    
    # Main program loop
    while True:
        # Display menu options
        solver.display_menu()
        
        try:
            # Get user choice
            choice = input("Enter your choice (1-9): ").strip()
            
            # Check for exit condition
            if choice == '9':
                print("Thank you for using Multi-Purpose Problem Solver!")
                print("Goodbye!")
                break
            # Validate and execute chosen function
            elif choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                solver.run_example(int(choice))
            else:
                print("Invalid choice! Please enter a number between 1 and 9.")
                
            # Pause before showing menu again
            input("\nPress Enter to continue...")
            
        except ValueError:
            # Handle non-numeric input errors
            print("Error: Please enter a valid number!")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {e}")
            print("Please try again.")

# Program entry point
if __name__ == "__main__":
    main()