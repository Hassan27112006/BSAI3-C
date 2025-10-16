# app.py
import streamlit as st
import random
from logic import FizzBuzz
from gamemanager import manager

st.title("🎮 FizzBuzz Quiz Game")
st.write("Click the correct answer!")

game = manager()
fizzbuzz = FizzBuzz()

if not st.session_state.game_over:
    Number = st.session_state.number
    correct_answer = fizzbuzz.get_value(Number)

    # ✅ Fix reshuffling issue by storing options
    if "options" not in st.session_state or st.session_state.last_number != Number:
        options = [correct_answer]
        while len(options) < 3:
            wrong = random.choice(["Fizz", "Buzz", "Fizz Buzz", str(random.randint(1, 20))])
            if wrong not in options:
                options.append(wrong)

        random.shuffle(options)
        st.session_state.options = options
        st.session_state.last_number = Number

    options = st.session_state.options  # use saved options

    st.subheader(f"👉 Number: {Number}")

    # Buttons for each option
    cols = st.columns(len(options))
    for i, opt in enumerate(options):
        if cols[i].button(opt, key=f"btn_{Number}_{i}"):
            if opt == correct_answer:
                st.success("✅ Correct!")
                st.session_state.score += 1
                st.session_state.history.append((Number, opt, "✅ Correct"))
                st.session_state.number += 1
                if "options" in st.session_state:
                    del st.session_state.options
                st.rerun()
            else:
                st.error(f"❌ Wrong! Correct was: {correct_answer}")
                st.session_state.history.append((Number, opt, f"❌ Wrong (Correct: {correct_answer})"))
                st.session_state.game_over = True
                st.rerun()

# Show stats
st.subheader("📊 Game Stats")
st.write(f"**Score:** {st.session_state.score}")


if st.session_state.history:
    st.write("### History")
    for num, ans, result in st.session_state.history:
        st.write(f"Number {num}: You said `{ans}` → {result}")

# Restart button
if st.session_state.game_over:
    if st.button("Restart Game"):
        game.Reset()
        if "options" in st.session_state:
            del st.session_state.options
        st.rerun()
