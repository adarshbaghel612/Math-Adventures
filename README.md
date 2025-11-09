🧮 Adaptive Math Quiz

An AI-inspired rule-based quiz system that adapts question difficulty based on user performance.

🚀 Overview

The Adaptive Math Quiz is an interactive web-based application built using Python and Streamlit.
It challenges users with dynamically generated math questions, automatically adjusting difficulty levels (Easy, Medium, Hard) based on performance.

The goal is to create a fun, intelligent, and educational experience that helps learners stay motivated and improve progressively.

🧠 Features

✅ Adaptive Difficulty — Questions become harder or easier depending on how well you perform.
✅ Real-Time Feedback — Instant correctness and time feedback after every answer.
✅ Accuracy Trend Chart — Visualizes performance over time with a line chart.
✅ Rule-Based Adaptive Logic — Lightweight and transparent difficulty control.
✅ Session Persistence — Quiz state maintained across interactions using Streamlit session state.
✅ Summary Dashboard — View performance summary and restart quiz anytime.

🏗️ Architecture
System Components
Layer	Description
User Interface	Built using Streamlit; collects input and displays questions, feedback, and charts.
Logic Engine	Generates math questions and evaluates correctness.
Session Manager	Tracks current difficulty, score, accuracy, and performance trends.
Visualization Layer	Uses Matplotlib to display accuracy trends graphically.
🔄 Flow Diagram

Explanation:

User enters name and chooses difficulty.

System generates a question based on level.

User submits an answer → checked for correctness.

Score and accuracy are updated.

Difficulty is increased or decreased based on performance.

Summary (with accuracy chart) can be viewed anytime.

⚙️ Adaptive Logic

The quiz uses rule-based adaptation instead of ML for simplicity and interpretability.

Rules Applied:

If user answers 2 consecutive questions correctly, difficulty → increases.

If user answers 2 consecutive questions incorrectly, difficulty → decreases.

Otherwise, difficulty remains constant.

This ensures a continuous and personalized challenge curve.

📊 Key Metrics Tracked
Metric	Description	Impact
Score	Incremented/decremented based on correct/incorrect answers	Used to trigger difficulty change
Correct/Incorrect Count	Tracks number of right/wrong attempts	Used for accuracy calculation
Accuracy (%)	(Correct ÷ Total) × 100	Visualized in trend chart
Time Taken (s)	Duration to answer a question	Used in feedback message
💻 Technologies Used

Python 3.10+

Streamlit — UI framework for interactive web apps

Matplotlib — Charting library for performance visualization

Random & Time — Core logic for question generation and timing

📂 Project Structure
─ README.md
├─ requirements.txt
├─ mathadventurers/
 ├─ main.py
 ├─ puzzle_generator.py
 ├─ tracker.py
 ├─ StreamlitUI.py
 ├─ Mathadventures.ipynb
 └─ adaptive_engine.py 



📄 requirements.txt
# Core framework
streamlit==1.38.0

# Visualization
matplotlib==3.9.2


🧮 Example Question Flow
Welcome, Adarsh 👋  
Current Difficulty: Easy  
Question: 5 + 8  
Your Answer: 13  
✅ Correct Answer! (⏱ 3.42s)
🎉 Difficulty Increased to Medium!

📈 Output Summary

After quiz ends or when “View Summary” is clicked:

📊 Quiz Summary
✅ Correct Answers: 7
❌ Incorrect Answers: 3
🎯 Final Accuracy: 70%
🌟 You’re doing great! Keep it up!

👨‍💻 Author

Adarsh Baghel
Department of Computer Science & Engineering (AI)
Bachelor of Technology
📧 Email: adarshreigns76626@gmail.com
