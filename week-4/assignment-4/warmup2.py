# Output
# name Mauricio Nunez
# grade 12
# subjects ['math', 'science', 'art']
# {'name': 'Mauricio Nunez', 'grade': '12', 'subjects': ['math', 'science', 'art'], 'graduated': False}
mauricio = {
    "name": "Mauricio Nunez",
    "grade" : "12",
    "subjects": ["math","science","art"]
}
for key, val in mauricio.items():
    print(key, val)
mauricio["graduated"] = False
print(mauricio)