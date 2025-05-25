import streamlit as st
import random

st.set_page_config(page_title="🎉 Operator Quiz for Parth", layout="centered")

# 💅 Stylish UI
st.markdown("""
<style>
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(135deg, #e0f7fa 0%, #fff3e0 100%);
    padding: 2rem;
    border-radius: 12px;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.stRadio > div > label {
    font-weight: bold;
}
.stButton > button {
    background-color: #ff6f00;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Operator Quiz for Parth")
st.write("""
Welcome! This quiz tests your knowledge on **Arithmetic**, **Comparison**, **Assignment**, and **Logical** operators in Python.

🟢 Each correct answer: **1 mark**  
🔴 No negative marks for wrong answers.  
🎯 Try to score at least **18** for a treat or **20** for a FreeFire bonus!
""")

# Quiz Questions
questions = [
    ("What is the output of: 7 + 3 * 2", ["20", "13", "17", "10"], "13"),
    ("What does 'a = 10; a //= 3; print(a)' output?", ["3", "3.3", "4", "Error"], "3"),
    ("Result of: print(5 == 5 and 7 > 3)", ["False", "True", "Error", "None"], "True"),
    ("Output of: x=4; x **= 2; print(x)", ["8", "16", "4", "Error"], "16"),
    ("What will print: print(not (5 > 3))", ["False", "True", "None", "Error"], "False"),
    ("Output: print(8 % 3)", ["2", "1", "3", "0"], "2"),
    ("What does 'a = 5; a += 3; print(a)' output?", ["8", "53", "5", "3"], "8"),
    ("Output: print(10 <= 10)", ["True", "False", "Error", "None"], "True"),
    ("What is the result of 'print(True or False and False)'?", ["True", "False", "Error", "None"], "True"),
    ("What will print: print(2 * (3 + 4))", ["14", "10", "20", "9"], "14"),
    ("Output: print(9 // 4)", ["2", "2.25", "3", "Error"], "2"),
    ("What does 'a = 7; a -= 2; print(a)' output?", ["5", "9", "72", "Error"], "5"),
    ("Result of: print(4 > 5 or 5 < 6)", ["True", "False", "Error", "None"], "True"),
    ("What is output: print(6 == 6 or 2 != 2)", ["True", "False", "Error", "None"], "True"),
    ("Output: print(15 % 4)", ["3", "4", "2", "1"], "3"),
    ("What does this print? x=3; x *= 4; print(x)", ["7", "12", "3", "Error"], "12"),
    ("Output: print( not False and True )", ["True", "False", "Error", "None"], "True"),
    ("What is printed by 'print(5 != 5)'?", ["False", "True", "None", "Error"], "False"),
    ("Result of: print(8 > 3 and 3 < 2)", ["False", "True", "Error", "None"], "False"),
    ("Output of: a=10; a /= 2; print(a)", ["5.0", "5", "2", "Error"], "5.0")
]

# Shuffle once per session
if "questions" not in st.session_state:
    st.session_state.questions = questions.copy()
    random.shuffle(st.session_state.questions)

with st.form("quiz_form"):
    answers = []
    total_qs = 20
    answered = 0

    st.markdown("## 📊 Progress")
    progress_bar = st.progress(0)

    for i, (question, options, correct) in enumerate(st.session_state.questions[:total_qs]):
        st.markdown(f"### Q{i+1}")
        shuffled_options = options.copy()
        random.shuffle(shuffled_options)
        selected = st.radio(question, shuffled_options, key=f"q{i}", index=None)

        if selected:  # If user picked an option
            answered += 1
        progress_bar.progress(answered / total_qs)
        answers.append((selected, correct))

    submitted = st.form_submit_button("🚀 Submit Quiz")

if submitted:
    score = 0
    st.markdown("---")
    st.subheader("📢 Result Breakdown")

    for i, (selected, correct) in enumerate(answers):
        if selected == correct:
            st.success(f"Q{i+1} ✅ Correct (+1)")
            score += 1
        else:
            st.error(f"Q{i+1} ❌ Wrong! Correct answer: {correct}")

    st.markdown("---")
    st.subheader(f"🎯 Final Score: **{score}/20**")
    st.session_state.score = score

    # 🎉 Rewards with confetti + emoji
    if score == 20:
        st.balloons()
        st.success("🏆 Perfect score! You can play FreeFire for 1:30 hours! 🔥🎮")
        st.markdown("🎊🎊🎊 **GOD LEVEL!** 🎊🎊🎊")
    elif score >= 18:
        st.balloons()
        st.success("🎉 Great job! You get a special treat from Papa! 🍫🥳")
        st.markdown("🎉 🎉 Keep it up! 🎉 🎉")
    elif score >= 15:
        st.info("👏 Nice! You’re close to mastery. Keep practicing!")
        st.markdown("💪💪 You're doing great!")
    elif score >= 10:
        st.info("👍 Good effort! Keep practicing.")
        st.markdown("🌱 Practice makes perfect!")
    else:
        st.warning("📚 Keep learning! Try again after some revision.")
        st.markdown("😅 Better luck next time!")
