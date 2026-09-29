#Dictionary of students (id > details)
student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_intergration": "english"},
    "id2": {"name": "David", "class": "V", "subject_intergration": "english"},
    "id3": {"name": "Sara", "class": "V", "subject_intergration": "english"},
    "id4": {"name": "Surya", "class" : "V", "subject_intergration": "english"}

}

result = {}
seen_keys = [] #using a list rather than a set

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_intergration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

#print output line by line
for k, v in result.items():
    print(k, ":", v)
