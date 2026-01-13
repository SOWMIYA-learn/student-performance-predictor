from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("model/student_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    message_type = None
    message_text = None
    hours_studied = None
    attendance = None
    internal_marks = None
    previous_grade = None

    if request.method == "POST":
        hours_studied = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        internal_marks = float(request.form["internal_marks"])
        previous_grade = float(request.form["previous_grade"])

        student_data = pd.DataFrame({
            'attendance': [attendance],
            'internal_marks': [internal_marks],
            'study_hours': [hours_studied],
            'previous_grade': [previous_grade]
        })

        prediction = model.predict(student_data)

        if prediction[0] == 1:
            result = "Pass ✅"
            message_type = "pass"
            message_text = "Great job! Keep up the hard work! 🌟"
        else:
            result = "Fail ❌"
            message_type = "fail"
            message_text = "Don’t give up! You can improve! 💪"

    return render_template(
        "index.html",
        result=result,
        message_type=message_type,
        message_text=message_text,
        study_hours=hours_studied,
        attendance=attendance,
        internal_marks=internal_marks,
        previous_grade=previous_grade
    )

if __name__ == "__main__":
    app.run(debug=True)
