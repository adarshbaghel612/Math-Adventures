import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# ---------------- Generate Question ----------------
def generate_question(level):
    if level == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"{a} + {b}"
        answer = a + b
    elif level == "Medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
        question = f"{a} - {b}"
        answer = a - b
    else:
        a, b = random.randint(2, 10), random.randint(2, 10)
        question = f"{a} × {b}"
        answer = a * b
    return question, answer


# ---------------- Streamlit UI Setup ----------------
st.set_page_config(page_title="🧮 Adaptive Math Quiz", layout="centered")
st.title("🧮 Adaptive Math Quiz")
st.caption("AI-powered quiz that adapts difficulty and tracks your performance!")

# ---------------- Session State ----------------
if "started" not in st.session_state:
    st.session_state.started = False
if "student_name" not in st.session_state:
    st.session_state.student_name = ""
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"
if "score" not in st.session_state:
    st.session_state.score = 0
if "correct" not in st.session_state:
    st.session_state.correct = 0
if "incorrect" not in st.session_state:
    st.session_state.incorrect = 0
if "accuracy_trend" not in st.session_state:
    st.session_state.accuracy_trend = []
if "question" not in st.session_state:
    st.session_state.question, st.session_state.answer = generate_question(st.session_state.difficulty)
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "feedback" not in st.session_state:
    st.session_state.feedback = ""


# ---------------- Start Screen ----------------
if not st.session_state.started and "show_summary" not in st.session_state:
    st.session_state.student_name = st.text_input("Enter Your Name:")
    st.session_state.difficulty = st.selectbox("Choose Difficulty:", ["Easy", "Medium", "Hard"])
    if st.button("🎯 Start Quiz"):
        if st.session_state.student_name.strip():
            st.session_state.started = True
            st.rerun()
        else:
            st.warning("Please enter your name to start.")


# ---------------- Quiz Screen ----------------
elif st.session_state.started:
    st.subheader(f"Welcome, {st.session_state.student_name} 👋")
    st.markdown(f"### Current Difficulty: **{st.session_state.difficulty}**")
    st.markdown(f"#### Question: `{st.session_state.question}`")

    if st.session_state.feedback:
        st.info(st.session_state.feedback)
        st.session_state.feedback = ""

    student_answer = st.text_input("Your Answer (enter 000 to quit):")

    col1, col2, col3 = st.columns(3)
    with col1:
        submit = st.button("✅ Submit Answer")
    with col2:
        next_q = st.button("➡️ Next Question")
    with col3:
        view_summary = st.button("📊 View Summary")

    # ---------- Submit ----------
    if submit:
        try:
            student_answer = int(student_answer)
            end_time = time.time()
            time_taken = round(end_time - st.session_state.start_time, 2)

            if student_answer == 000:
                st.session_state.started = False
                st.session_state.show_summary = True
                st.rerun()

            elif student_answer == st.session_state.answer:
                st.session_state.feedback = f"✅ Correct Answer! (⏱ {time_taken}s)"
                st.session_state.score += 1
                st.session_state.correct += 1
            else:
                st.session_state.feedback = f"❌ Incorrect. Correct answer was {st.session_state.answer}. (⏱ {time_taken}s)"
                st.session_state.score -= 1
                st.session_state.incorrect += 1

            # Update accuracy trend
            total_q = st.session_state.correct + st.session_state.incorrect
            accuracy = (st.session_state.correct / total_q) * 100 if total_q > 0 else 0
            st.session_state.accuracy_trend.append(accuracy)

            # ---------- Adaptive Difficulty ----------
            if st.session_state.score >= 2 and st.session_state.difficulty != "Hard":
                levels = ["Easy", "Medium", "Hard"]
                st.session_state.difficulty = levels[levels.index(st.session_state.difficulty) + 1]
                st.session_state.score = 0
                st.session_state.feedback += f"\n🎉 Difficulty Increased to {st.session_state.difficulty}!"

            elif st.session_state.score <= -2 and st.session_state.difficulty != "Easy":
                levels = ["Easy", "Medium", "Hard"]
                st.session_state.difficulty = levels[levels.index(st.session_state.difficulty) - 1]
                st.session_state.score = 0
                st.session_state.feedback += f"\n⚙️ Difficulty Decreased to {st.session_state.difficulty}!"

            # Generate next question
            st.session_state.question, st.session_state.answer = generate_question(st.session_state.difficulty)
            st.session_state.start_time = time.time()
            st.rerun()

        except ValueError:
            st.warning("Please enter a valid number.")

    # ---------- Next Question ----------
    if next_q:
        st.session_state.feedback = "➡️ New question generated!"
        st.session_state.question, st.session_state.answer = generate_question(st.session_state.difficulty)
        st.session_state.start_time = time.time()
        st.rerun()

    # ---------- View Summary ----------
    if view_summary:
        st.session_state.started = False
        st.session_state.show_summary = True
        st.rerun()


# ---------------- Summary Screen ----------------
if "show_summary" in st.session_state and st.session_state.show_summary:
    st.title("📊 Quiz Summary")

    total_q = st.session_state.correct + st.session_state.incorrect
    accuracy = (st.session_state.correct / total_q) * 100 if total_q > 0 else 0

    st.write(f"**Total Questions Attempted:** {total_q}")
    st.write(f"✅ **Correct Answers:** {st.session_state.correct}")
    st.write(f"❌ **Incorrect Answers:** {st.session_state.incorrect}")
    st.write(f"🎯 **Final Accuracy:** {accuracy:.2f}%")

    if accuracy > 70:
        st.success("🌟 You’re doing great! Keep it up!")
    else:
        st.info("💪 Keep practicing — you’ll improve soon!")

    # -------- Accuracy Trend Chart --------
    if st.session_state.accuracy_trend:
        st.subheader("📈 Accuracy Trend Over Time")
        fig, ax = plt.subplots()
        ax.plot(range(1, len(st.session_state.accuracy_trend) + 1),
                st.session_state.accuracy_trend, marker='o', linewidth=2)
        ax.set_xlabel("Question Number")
        ax.set_ylabel("Accuracy (%)")
        ax.set_title("Performance Trend")
        ax.grid(True)
        st.pyplot(fig)

    if st.button("🔁 Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
