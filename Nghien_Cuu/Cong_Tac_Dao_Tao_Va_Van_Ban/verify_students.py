import docx

doc = docx.Document(r"C:\Users\Admin\.gemini\antigravity\scratch\student_transfer\student_list.docx")
table = doc.tables[0]

print(f"Total rows in table: {len(table.rows)}")

students = []
for i in range(1, len(table.rows)):
    row = table.rows[i]
    stt = row.cells[0].text.strip()
    name = row.cells[1].text.strip()
    dob = row.cells[2].text.strip()
    gender_f = row.cells[3].text.strip()
    khoi = row.cells[4].text.strip()
    parent = row.cells[7].text.strip()
    phone = row.cells[8].text.strip()
    students.append({
        'stt': stt,
        'name': name,
        'dob': dob,
        'female': gender_f,
        'khoi': khoi,
        'parent': parent,
        'phone': phone
    })

print(f"Loaded {len(students)} students.")
for s in students:
    print(f"STT: {s['stt']:>2} | Name: {s['name']:<28} | DOB: {s['dob']} | Female: {s['female']:<2} | Parent: {s['parent']:<22} | Phone: {s['phone']}")
