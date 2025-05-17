# GPA calculator with credit units and grade points for 6 courses
def calculate_gpa():
    # Grade to point conversion (assuming a 5.0 scale)
    grade_points = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'F': 0.0}
    
    total_grade_points = 0
    total_credit_units = 0
    
    # Get user input for 6 courses
    for i in range(1, 7):
        print(f"\nCourse {i}:")
        grade = input("Enter grade (A, B, C, D, F): ").upper()
        credit_units = float(input("Enter credit units for this course: "))
        
        # Ensure valid grade input
        if grade not in grade_points:
            print("Invalid grade entered. Assuming grade F.")
            grade = 'F'
        
        # Calculate grade points for the course
        grade_point = grade_points[grade]
        total_grade_points += grade_point * credit_units
        total_credit_units += credit_units
    
    # Calculate GPA
    if total_credit_units > 0:
        gpa = total_grade_points / total_credit_units
    else:
        gpa = 0.0  # Handle the case of no credit units, just in case
    
    # Print the GPA
    print(f"\nYour GPA is: {round(gpa, 2)}")

# Call the function to calculate GPA
calculate_gpa()
