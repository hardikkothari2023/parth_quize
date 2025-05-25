import streamlit as st
import random

st.set_page_config(page_title="🎉 Operator Quiz for Parth", layout="centered")

# Stylish UI
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

questions = [
    ("What is the output of: 7 + 3 * 2", ["13", "20", "17", "10"], "13"),
    ("What does 'a = 10; a //= 3; print(a)' output?", ["3", "3.3", "4", "Error"], "3"),
    ("Result of: print(5 == 5 and 7 > 3)", ["True", "False", "Error", "None"], "True"),
    ("Output of: x=4; x **= 2; print(x)", ["16", "8", "4", "Error"], "16"),
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
    ("What does this print? x=3; x *= 4; print(x)", ["12", "7", "3", "Error"], "12"),
    ("Output: print( not False and True )", ["True", "False", "Error", "None"], "True"),
    ("What is printed by 'print(5 != 5)'?", ["False", "True", "None", "Error"], "False"),
    ("Result of: print(8 > 3 and 3 < 2)", ["False", "True", "Error", "None"], "False"),
    ("Output of: a=10; a /= 2; print(a)", ["5.0", "5", "2", "Error"], "5.0")
]

# Shuffle questions once
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = questions.copy()
    random.shuffle(st.session_state.shuffled_questions)

total_questions = len(st.session_state.shuffled_questions)

# Store user answers persistently in session_state
if "answers" not in st.session_state:
    st.session_state.answers = [None] * total_questions

# Show progress bar
answered_count = sum([1 for ans in st.session_state.answers if ans is not None])
progress = answered_count / total_questions
st.markdown("## 📊 Progress")
progress_bar = st.progress(progress)

# Quiz form
with st.form("quiz_form"):

    for i, (q, opts, _) in enumerate(st.session_state.shuffled_questions):
        # Shuffle options for each question to avoid pattern, but fix shuffle so it's stable per session
        # For that, shuffle options once per question in session_state
        if f"opts_{i}" not in st.session_state:
            opts_shuffled = opts.copy()
            random.shuffle(opts_shuffled)
            st.session_state[f"opts_{i}"] = opts_shuffled
        else:
            opts_shuffled = st.session_state[f"opts_{i}"]

        # Default index for radio to keep selection stable
        default_index = None
        if st.session_state.answers[i] in opts_shuffled:
            default_index = opts_shuffled.index(st.session_state.answers[i])

        answer = st.radio(f"Q{i+1}: {q}", opts_shuffled, index=default_index, key=f"q{i}")

        st.session_state.answers[i] = answer

    submitted = st.form_submit_button("🚀 Submit Quiz")

if submitted:
    # Check if all questions answered
    if None in st.session_state.answers:
        st.warning("⚠️ Please answer all questions before submitting!")
    else:
        score = 0
        st.markdown("---")
        st.subheader("📢 Result Breakdown")

        for i, (selected, (_, _, correct)) in enumerate(zip(st.session_state.answers, st.session_state.shuffled_questions)):
            if selected == correct:
                st.success(f"Q{i+1} ✅ Correct (+1)")
                score += 1
            else:
                st.error(f"Q{i+1} ❌ Wrong! Correct answer: {correct}")

        st.markdown("---")
        st.subheader(f"🎯 Final Score: **{score}/{total_questions}**")
        st.session_state.score = score

        if score == total_questions:
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
