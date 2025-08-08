students={
    "hiral":99,
    "pooja":90,
    "niyati":85,
    "jeetu":100
}
name=input("Enter the student's name: ").strip()
if name in students:
    print(f"{name}'s marks: ",students[name])
else:
    print("Student not found!")
    