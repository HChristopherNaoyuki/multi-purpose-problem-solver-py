class ProblemSolver:
    """
    A multi-purpose problem solver that handles various coding challenges
    from sports calculations to game rules and health assessments.
    """
    
    def calculate_sports_score(self):
        """
        Calculate the final score based on time remaining and current score.
        Used in sports games where points are awarded every 5 minutes.
        """
        # Get input: current time and current score
        time_str, score_str = input().split()
        current_time = int(time_str)
        current_score = int(score_str)
        
        # Calculate remaining time and additional points
        # Points are awarded every 5 minutes, with special handling for exact multiples
        if current_time % 10 == 0:
            # If current time is multiple of 10, calculate exact additional points
            final_score = current_score + int((90 - current_time) / 5)
        else:
            # Otherwise, add one extra point for partial time period
            final_score = current_score + int((90 - current_time) / 5) + 1
        
        print(final_score)
    
    def check_win_condition(self):
        """
        Check if a number meets win conditions:
        - Between 50 and 70 (inclusive)
        - Divisible by 6
        Otherwise, it's a loss.
        """
        number = int(input())
        
        if 50 <= number <= 70 or number % 6 == 0:
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
        height, weight = map(float, input().split())
        
        # Calculate standard weight
        standard_weight = (height - 100) * 0.9
        # Calculate obesity rate percentage
        obesity_rate = (weight - standard_weight) * 100 / standard_weight
        
        if obesity_rate <= 10:
            print('Normal')
        elif 10 < obesity_rate <= 20:
            print('Overweight')
        else:
            print('Obese')
    
    def calculate_obesity_level_detailed(self):
        """
        Calculate obesity level with detailed height-based standard weight calculation.
        Different formulas for different height ranges.
        """
        height, weight = map(float, input().split())
        standard_weight = 0
        
        # Calculate standard weight based on height range
        if height < 150:
            standard_weight = height - 100
        elif 150 <= height < 160:
            standard_weight = ((height - 150) / 2) + 50
        else:
            standard_weight = (height - 100) * 0.9
        
        # Calculate obesity rate percentage
        obesity_rate = ((weight - standard_weight) * 100) / standard_weight
        
        if obesity_rate <= 10:
            print("Normal")
        elif 10 < obesity_rate <= 20:
            print("Overweight")
        else:
            print("Obese")
    
    def add_two_numbers(self):
        """Simple addition of two numbers."""
        a = int(input())
        b = int(input())
        print(a + b)
    
    def run_all_examples(self):
        """
        Run examples of all methods to demonstrate functionality.
        This method provides sample inputs for testing.
        """
        print("=== Sports Score Calculation ===")
        print("Example input: 45 2")
        self.calculate_sports_score()
        
        print("\n=== Win Condition Check ===")
        print("Example input: 60")
        self.check_win_condition()
        
        print("\n=== Lucky Calculation ===")
        print("Example input: 15 5 10")
        self.check_lucky_calculation()
        
        print("\n=== Height Safety Check ===")
        print("Example input: 175 180 165")
        self.check_height_safety()
        
        print("\n=== Even/Odd Check ===")
        print("Example input: 7")
        self.check_even_odd()
        
        print("\n=== Simple Obesity Calculation ===")
        print("Example input: 170 65")
        self.calculate_obesity_level_simple()
        
        print("\n=== Detailed Obesity Calculation ===")
        print("Example input: 155 50")
        self.calculate_obesity_level_detailed()
        
        print("\n=== Add Two Numbers ===")
        print("Example inputs: 5 and 3")
        self.add_two_numbers()


# Example usage:
if __name__ == "__main__":
    solver = ProblemSolver()
    
    # Uncomment the method you want to test individually:
    # solver.calculate_sports_score()
    # solver.check_win_condition()
    # solver.check_lucky_calculation()
    # solver.check_height_safety()
    # solver.check_even_odd()
    # solver.calculate_obesity_level_simple()
    # solver.calculate_obesity_level_detailed()
    # solver.add_two_numbers()
    
    # Or run all examples at once:
    # solver.run_all_examples()
    
    # Interactive menu for user selection
    print("Select a function to run:")
    print("1. Calculate Sports Score")
    print("2. Check Win Condition")
    print("3. Check Lucky Calculation")
    print("4. Check Height Safety")
    print("5. Check Even/Odd")
    print("6. Calculate Obesity Level (Simple)")
    print("7. Calculate Obesity Level (Detailed)")
    print("8. Add Two Numbers")
    print("9. Run All Examples")
    
    try:
        choice = int(input("Enter your choice (1-9): "))
        
        if choice == 1:
            solver.calculate_sports_score()
        elif choice == 2:
            solver.check_win_condition()
        elif choice == 3:
            solver.check_lucky_calculation()
        elif choice == 4:
            solver.check_height_safety()
        elif choice == 5:
            solver.check_even_odd()
        elif choice == 6:
            solver.calculate_obesity_level_simple()
        elif choice == 7:
            solver.calculate_obesity_level_detailed()
        elif choice == 8:
            solver.add_two_numbers()
        elif choice == 9:
            solver.run_all_examples()
        else:
            print("Invalid choice. Please run the program again and select 1-9.")
    except ValueError:
        print("Please enter a valid number.")