from app import extract_text_and_headings, create_ppt
import io

print("Extracting...")
content = extract_text_and_headings("test.docx")
# print("Content:", content)

print("Creating PPT...")
prs = create_ppt(content)
prs.save("output_test.pptx")
print("Success! output_test.pptx created.")
