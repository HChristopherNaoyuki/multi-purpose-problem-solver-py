# coding: utf-8
"""
Multi-Purpose Problem Solver
A comprehensive solution for various coding challenges including sports calculations,
game rules, health assessments, and mathematical operations.
"""

class ProblemSolver:
    def calculate_sports_score(self):
        """
        Calculate the final score based on time remaining and current score.
        Used in sports games where points are awarded every 5 minutes.
        """
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a % 10 == 0:
            c = b + int((90 - a) / 5)
        else:
            c = b + int((90 - a) / 5) + 1
        print(c)

    def check_win_condition(self):
        """
        Check if a number meets win conditions:
        - Between 50 and 70 (inclusive)
        - Divisible by 6
        Otherwise, it's a loss.
        """
        a = int(input())
        if 50 <= a <= 70:
            print('win')
        elif a % 6 == 0:
            print('win')
        else:
            print('lose')

    def check_lucky_calculation(self):
        """
        Check if (a - b + c) is divisible by 10.
        If divisible, print 'Lucky', otherwise 'So-so'.
        """
        a, b, c = map(int, input().split())
        if (a - b + c) % 10 == 0:
            print('Lucky')
        else:
            print('So-so')

    def check_height_safety(self):
        """
        Check if all three heights are above 170.
        If any height is 170 or below, print 'CRASH', otherwise 'PASS'.
        """
        a, b, c = map(int, input().split())
        if a <= 170 or b <= 170 or c <= 170:
            print('CRASH')
        else:
            print('PASS')

    def check_even_odd(self):
        """Check if a number is even or odd."""
        n = int(input())
        if n % 2 == 0:
            print('even')
        else:
            print('odd')

    def calculate_obesity_level_simple(self):
        """
        Calculate obesity level using simple formula:
        Standard weight = (height - 100) × 0.9
        Obesity rate = (current weight - standard weight) × 100 / standard weight
        """
        a, b = map(float, input().split())
        c = (a - 100) * 0.9
        d = (b - c) * 100 / c
        if d <= 10:
            print('Normal')
        elif 10 < d <= 20:
            print('Overweight')
        else:
            print('Obese')

    def calculate_obesity_level_detailed(self):
        """
        Calculate obesity level with detailed height-based standard weight calculation.
        Different formulas for different height ranges.
        """
        h, w = map(float, input().split())
        s = 0
        if h < 150:
            s = h - 100
        elif 150 <= h < 160:
            s = ((h - 150) / 2) + 50
        else:
            s = (h - 100) * 0.9
        o = ((w - s) * 100) / s
        if o <= 10:
            print("Normal")
        elif 10 < o <= 20:
            print("Overweight")
        else:
            print("Obese")

    def add_two_numbers(self):
        """Simple addition of two numbers."""
        a = int(input())
        b = int(input())
        print(a + b)

    def display_menu(self):
        """Display the main menu options."""
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
        """Run a specific example based on user choice."""
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
    """Main function to run the problem solver application."""
    solver = ProblemSolver()
    
    print("Welcome to Multi-Purpose Problem Solver!")
    print("This program solves various coding problems including:")
    print("- Sports score calculations")
    print("- Game win conditions")
    print("- Health assessments")
    print("- Mathematical operations")
    
    while True:
        solver.display_menu()
        
        try:
            choice = input("Enter your choice (1-9): ").strip()
            
            if choice == '9':
                print("Thank you for using Multi-Purpose Problem Solver!")
                print("Goodbye!")
                break
            elif choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                solver.run_example(int(choice))
            else:
                print("Invalid choice! Please enter a number between 1 and 9.")
                
            input("\nPress Enter to continue...")
            
        except ValueError:
            print("Error: Please enter a valid number!")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()