import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]
GRADES = [1, 2, 3, 4, 5, 6, 7, 8]
JSON_DIRECTORY = "students"

def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

def get_student_avg(report_card):
    total_marks = 0

    for subject in SUBJECTS:
        mark = report_card[subject]
        total_marks += mark

    avg_marks = round(total_marks / len(SUBJECTS), 2)
    report_card["avg_marks"] = avg_marks

    return report_card

def report_cards_to_list():
    report_cards = []

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(JSON_DIRECTORY, student_number)
        report_card = get_student_avg(report_card)
        report_cards.append(report_card)

    return report_cards

def average_student_marks(report_cards):
    total_marks = 0

    for card in report_cards:
        avg_marks = card["avg_marks"]
        total_marks += avg_marks

    avg_total_marks = round(total_marks / len(report_cards), 2)

    return avg_total_marks

def total_subject_marks(report_cards):
    total_subject_marks = {}
    for subject in SUBJECTS:
        for card in report_cards:
            mark = card[subject]
            total_subject_marks[subject] = total_subject_marks.get(subject, 0) + mark

    return total_subject_marks

def avg_subject_marks(total_subject_marks):
    avg_subject_marks = {}
    for subject in SUBJECTS:
        avg_subject_marks[subject] = round(total_subject_marks[subject] / len(cards), 2)

    return avg_subject_marks

def hardest_subject(avg_subject_marks):
    return min(avg_subject_marks, key=avg_subject_marks.get)

def easiest_subject(avg_subject_marks):
    return max(avg_subject_marks, key=avg_subject_marks.get)

def get_best_avg_grades(report_cards):
    best_avg_grades = []

    for grade in GRADES:
        d = {}
        for card in report_cards:
            if card["grade"] == grade:
                marks = card["avg_marks"]
                d["avg_marks"] = d.get("avg_marks", 0) + marks

        d["grade"] = grade
        d["avg_marks"] = round(d["avg_marks"] / 250, 2)
        best_avg_grades.append(d)

    return best_avg_grades

def best_grade(best_avg_grades):
    best_grade_dict = max(best_avg_grades, key=lambda x: x["avg_marks"])
    return best_grade_dict["grade"]

def worst_grade(best_avg_grades):
   worst_grade_dict = min(best_avg_grades, key=lambda x: x["avg_marks"])
   return worst_grade_dict["grade"]

def best_student(report_cards):
    best_student_dict = max(report_cards, key=lambda x: x["avg_marks"])
    return best_student_dict["id"]

def worst_student(report_cards):
    worst_student_dict = min(report_cards, key=lambda x: x["avg_marks"])
    return worst_student_dict["id"]

cards = report_cards_to_list()

best_avg_grades = get_best_avg_grades(cards)

best_student = best_student(cards)
worst_student = worst_student(cards)
print(best_student)
print(worst_student)

best_grade = best_grade(best_avg_grades)
worst_grade = worst_grade(best_avg_grades)

sub_marks = total_subject_marks(cards)

avg_subject_marks = avg_subject_marks(sub_marks)

hardest_subject = hardest_subject(avg_subject_marks)
easiest_subject = easiest_subject(avg_subject_marks)










