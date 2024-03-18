def is_student(name):
    # Add your student checking logic here
    return name.lower() in ['student1', 'student2', 'student3']

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    if is_student(user_name):
        print(f"Hello {user_name}, welcome to the student area.")
    else:
        print(f"Sorry, {user_name}, you are not a student.")