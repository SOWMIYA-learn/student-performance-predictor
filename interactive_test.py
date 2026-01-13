import pandas as pd
import pickle  # because your model was saved with pickle

# Load the trained model
model = pickle.load(open("model/student_model.pkl", "rb"))

# Ask user for student details
hours_studied = float(input("Enter hours studied: "))
attendance = float(input("Enter attendance percentage: "))
internal_marks = float(input("Enter internal marks: "))
previous_grade = float(input("Enter previous grade: "))

# Create a DataFrame for the model
student_data = pd.DataFrame({
    'attendance': [attendance],
    'internal_marks': [internal_marks],
    'study_hours': [hours_studied],
    'previous_grade': [previous_grade]
})

# Make prediction
prediction = model.predict(student_data)

# Show the result
if prediction[0] == 1:  # change based on your labels: 1 = Pass, 0 = Fail
    print("Predicted Result: Pass ✅")
else:
    print("Predicted Result: Fail ❌")

