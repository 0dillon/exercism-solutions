"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    list = []
    for student in student_scores:
        list.append(round(student))
    return list

def count_failed_students(student_scores):
    failed_student = 0
    for item in student_scores:
        if item <= 40:
            failed_student += 1
    return failed_student

def above_threshold(student_scores, threshold):
    above = []
    for score in student_scores:
        if score >= threshold:
            above.append(score)
    return above

def letter_grades(highest):
    output = []
    gap = round((highest-41)/4)
    for i in range(4):
        output.append(41+gap*i)
    return output

def student_ranking(student_scores, student_names):
    ranking = []
    for i in range(len(student_scores)):
        ranking.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return ranking
    
def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []

