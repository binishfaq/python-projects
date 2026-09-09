def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"



def STUMARKS():
    name = input("Enter your name: ")
    Eng = float(input("Enter marks of English: "))
    Urdu = float(input("Enter marks of Urdu: "))
    Math = float(input("Enter marks of Math: "))
    Phy = float(input("Enter marks of Physics: "))
    Comp = float(input("Enter marks of Computer: "))

    totalMarks = [Eng, Urdu, Math, Phy, Comp]
    marks = sum(totalMarks)

    percentage = (marks / 500) * 100


    print("Student:", name)
    print("Total Marks:", marks)
    print("Percentage:", percentage)
    print("English Grade:", calculate_grade(Eng))
    print("Urdu Grade:", calculate_grade(Urdu))
    print("Math Grade:", calculate_grade(Math))
    print("Physics Grade:", calculate_grade(Phy))
    print("Computer Grade:", calculate_grade(Comp))

STUMARKS()

