#students =  [{"name" : "Alice", 
            "age" : 12,
          "class" : "6A",
           "math_marks" : 84,
           "science_marks" : 90,
            "parent_password" : "1243"
            },
{"name" : "sara",
"age" : 12,
"class" : "6B",
"math_marks" : 84,
"science_marks" : 97,
"parent_password" : "7843"},
            ]
teachers = [{"name" : "Mr.John", "subject" : "science"},
            {"name" : "Ms.Jane", "subject" : "math"}]
adminpass = 1853
assignments = {}
def main_menu() :
  while True :
    print("\n=== School Mangement System ===")
    print("1. Student")
    print("2. Teacher")
    print("3. Parent")
    print("4. Admin")
    print("5. Exit")
    choice = input("Choose 1-5")
    if choice == 1 :
      student_menu()
    elif choice == 2 :
      teacher_menu()
    elif choice == 3 :
      parent_menu()
    elif choice == 4 :
      admin_menu()
    elif choice == 5 :
      break
    else :
      print("Not valid option")
def student_menu() :
  print("\n---Student Menu---")
  name = input("Enter your name")
  found = False
  for student in  students :
    if student["name"].lower() == name.lower() :
      found = True
      print("\nWelcome", student["name"] + "!" )
      print("Class:", student["class"])
      print("MArks:")
      print("Math Marks:", student["math marks"])
      print("Science Marks:", student["science marks"])
      print("\nAssignments")
      if assignments :
        for subject, info in assignments.items() :
          print(subject, "-", info["question"], "(by", info["teacher"] + ")")
      else :
        print("No assignments avalible.")
      break
  if not found :
    print("Student Not found!")
def teacher_menu() :
   print("\n----Teacher Menu----")
   name = input("Enter your name")
   found = False
  for teacher in teachers :
    if teacher["name"].lower() == name.lower() :
      found = True
      print("\nWelcome", teacher["name"])
      print("1. Update Student Marks")
      print("2. Add assignments")
      choice = input("Enter your choice.")
      if choice == "1" :
        update_marks(teacher["subject"])
      elif choice == "2" :
        add_assignment(teacher["subject"], teacher["name"])
      else :
        print("Invalid choice")
      break

  if not found :
    print("Teacher not found.")
def add_assignments(subject, teacher_name) :
  question = input("Enter assignment question for ", + subject + ":")
  assignments[subject] = {"question" : question, "teacher" : teacher_name}
  print("Assignment added successfully for", subject)


def update_marks():
  print("\n---Updating Marks---")
  name = input("Enter Student's name.")
  for student in student :
    if student["name"].lower() == name.lower() :
      new_mark = int(input("enter new marks for", + subject + ":"))
      if subject.lower() == "math" :
        student["math_marks"] = new_mark
        print("math marks updated")
      elif subject.lower() == "science" :
        student["science_marks"] = new_mark
        print("Science Marks have been updated.")
      else :
        print("Subject not found.")
        return
      print("Marks successfully updated for", student["name"] + "!")
      return
  print("Student not found.")
def parent_menu():
  print("\n---Parent Menu")
  child_name = input("Enter your child's name")
  password = int(input("Enter your parent pass."))
  found = False
  for student in students :
    if student["name"].lower() == child_name.lower() :
      if student["parent_password"] == password :
      found = True
      print("\n--Parent Acccount for ---", student["name"])
      print("Class :", student["class"])
      print("Age :", student["age"])
      print("Performance :")
      print("Math Marks :", student["math_marks"])
      print("Science Marks :"), student["math_marks"]
      avg = (student["math_marks"] + student["science_marks"]) / 2
      if avg >= 85 :
        print("Overall, Excellent Performance!")
      elif avg >= 70 :
        print("Overall, Good but can Improve.")
      else :
        print("You are failing. Get a tutor.")
    else :
      print("Incorrect password")
  break
def admin_menu() :
  print("\n---Admin Menu---")
  password = int(input("Enter Admin PAssword"))
  if adminpass != password:
        print("Incorrect")
        return
  while True :
        print("\n1. View All Students")
        print("2. Add Student")
        print("3. Remove Student")
        print("4. View Teachers")
        print("5. Add Teacher")
        print("6. Go Back")
        choice = input("Enter cchoice")
        if choice == "1" :
          print("\n---All Students---")
          for s in students :
             print(s["name"], "- Class", s["class"], "-Age", s["age"], "-Science" s["science_marks"], "-Math", s["math_marks"])
        elif choice == "2" :
            name = input("Enter name")
            age = int(input("Enter Age"))
            class_name = input("Enter Class")
            math_marks = input("Enter Math MArks scores")
            "science_marks": science
            })
            print("Student", name, "added successfully!")

        elif choice == "3":
            name = input("Enter student name to remove: ")
            for s in students:
                if s["name"].lower() == name.lower():
                    students.remove(s)
                    print("Student", name, "removed successfully!")
                    break
            else:
                print("Student not found!")

        elif choice == "4":
            print("\n--- All Teachers ---")
            for t in teachers:
                print(t["name"], "- Subject:", t["subject"])

        elif choice == "5":
            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")
            teachers.append({"name": name, "subject": subject})
            print("Teacher", name, "added successfully!")

        elif choice == "6":
            break
        else:
            print("Invalid choice! Try again.")
main_menu()

