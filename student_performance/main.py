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


def report_cards_to_list():
    report_cards = []

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(JSON_DIRECTORY, student_number)
        report_cards.append(report_card)

    return report_cards

# Avg student mark
def get_student_avg(report_card):
    total_marks = 0

    for subject in SUBJECTS:
        mark = report_card[subject]
        total_marks += mark

    avg_marks = total_marks / len(SUBJECTS)

    return avg_marks

def get_all_students_avg(report_cards):
    all_marks = 0

    for card in report_cards:
        student_avg = get_student_avg(card)
        all_marks += student_avg

    avg_total_marks = round(all_marks / NUM_STUDENTS, 2)

    return avg_total_marks


def get_avg_subject(report_cards):
    subject_marks = {}

    for card in report_cards:
        for subject in SUBJECTS:
            mark = card[subject]
            subject_marks[subject] = subject_marks.get(subject, 0) + mark

    avg_subject_marks = {}

    for key, val in subject_marks.items():
        avg_subject_marks[key] = val / len(report_cards)

    return avg_subject_marks


def return_subject_hardest(avg_subject_marks):
    key = filter(lambda x: avg_subject_marks[x] == min(avg_subject_marks.values()), avg_subject_marks)

    return list(key)[0]


def return_subject_easiest(avg_subject_marks):
    key = filter(lambda x: avg_subject_marks[x] == max(avg_subject_marks.values()), avg_subject_marks)

    return list(key)[0]


# Best performing grade
def get_best_performing_grade(report_cards):
    d = []
    for grade in GRADES:
        f = {}

        for card in report_cards:
            if card["grade"] == grade:
                for subject in SUBJECTS:
                    mark = card[subject]
                    f[subject] = f.get(subject, 0) + mark

        avg_subject_marks = {}

        for key, val in f.items():
            avg_subject_marks[key] = val / len(report_cards)

        avg_subject_marks["grade"] = grade

        d.append(avg_subject_marks)

    return d














# Worst performing grade
def get_worst_performing_grade():
    pass

# Best student ID
def get_best_student_id():
    pass

# Worst student ID
def get_worst_student_id():
    pass