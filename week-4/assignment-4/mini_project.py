# Output
# Top scorer:       Priya (95)
# Class average:    81.25
# Subjects offered: {'Python', 'Data', 'Web'}
# High scorers:     ['Jazmine', 'Sara', 'Priya', 'Mia', 'Eli']
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_scorer = ""
top_score = 0
class_avg = 0
unique_subjects = set()
high_scorers = []
for student in students:
    if student["score"] > top_score:
        top_scorer = student["name"]
        top_score = student["score"]
    if student["score"] > 75:
        high_scorers.append(student["name"])
    class_avg += student["score"]
    unique_subjects.add(student["subject"])
class_avg /= len(students)

print(f"""
Top scorer:       {top_scorer} ({top_score})
Class average:    {class_avg}
Subjects offered: {unique_subjects}
High scorers:     {high_scorers}
""")