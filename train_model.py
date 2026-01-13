import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Step 1: Load the dataset
data = pd.read_csv("student_data.csv")

# Step 2: Separate input (X) and output (y)
X = data[['attendance', 'internal_marks', 'study_hours', 'previous_grade']]
y = data['result']

# Step 3: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Save the trained model
pickle.dump(model, open("model/student_model.pkl", "wb"))

print("✅ Model trained and saved successfully!")
