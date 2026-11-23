subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))
subject5 = float(input("Enter marks for Subject 5: "))

total = subject1 + subject2 + subject3 + subject4 + subject5
maximum_marks = 500  
percentage = (total / maximum_marks) * 100

print("\n--- Student Result ---")
print(f"Total marks: {total} / {maximum_marks}")
print(f"Percentage: {percentage:.2f}%")
