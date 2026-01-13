const toggle = document.getElementById("themeToggle");
const body = document.body;

toggle.addEventListener("click", () => {
  body.classList.toggle("dark");
  toggle.textContent = body.classList.contains("dark") ? "☀️" : "🌙";
});

function generateFeedback(study, attendance, internal) {
  let feedback = [];

  if (attendance >= 85) feedback.push("✔ Strong attendance improves consistency");
  else feedback.push("⚠ Attendance needs improvement");

  if (study >= 6) feedback.push("✔ Study hours are sufficient");
  else feedback.push("⚠ Increase daily study hours");

  if (internal >= 70) feedback.push("✔ Internal marks are good");
  else feedback.push("⚠ Internal marks need improvement");

  return feedback;
}


document.addEventListener("DOMContentLoaded", () => {

  const study = parseFloat(document.getElementById("studyHidden")?.value);
  const attendance = parseFloat(document.getElementById("attendanceHidden")?.value);
  const internal = parseFloat(document.getElementById("internalHidden")?.value);

  if (!isNaN(study) && !isNaN(attendance) && !isNaN(internal)) {
    const feedback = generateFeedback(study, attendance, internal);

    const list = document.getElementById("feedbackList");
    list.innerHTML = "";

    feedback.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      list.appendChild(li);
    });
  }
});
