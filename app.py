import streamlit as st
from RPS import player

# --- Page Configuration ---
st.set_page_config(page_title="AI Rock-Paper-Scissors", page_icon="🤖")

# --- Title Only (No Bangla) ---
st.title("AI Rock-Paper-Scissors")

# --- Session State Management ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'patterns' not in st.session_state:
    st.session_state.patterns = {}
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'ai_score' not in st.session_state:
    st.session_state.ai_score = 0

# --- Game Logic ---
def play_game(user_move):
    prev_play = st.session_state.history[-1] if st.session_state.history else ""
    ai_move = player(prev_play, st.session_state.history, st.session_state.patterns)
    
    winning_rules = {'R': 'S', 'S': 'P', 'P': 'R'}
    
    if user_move == ai_move:
        result = "Tie! 🤝"
    elif winning_rules[user_move] == ai_move:
        result = "You Win! 🎉"
        st.session_state.user_score += 1
    else:
        result = "AI Wins! 🤖"
        st.session_state.ai_score += 1
        
    return ai_move, result

# --- UI Buttons ---
st.write("Choose your move:")
col1, col2, col3 = st.columns(3)
user_input = None

with col1:
    if st.button("Rock ✊", use_container_width=True):
        user_input = "R"
with col2:
    if st.button("Paper 🖐️", use_container_width=True):
        user_input = "P"
with col3:
    if st.button("Scissors ✌️", use_container_width=True):
        user_input = "S"

# --- Display Results ---
if user_input:
    ai_move, result = play_game(user_input)
    
    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("Your Move", user_input)
    c2.metric("AI Move", ai_move)
    
    st.subheader(f"Result: {result}")
    st.divider()

# --- Sidebar Scoreboard ---
st.sidebar.title("Scoreboard")
st.sidebar.write(f"👤 You: {st.session_state.user_score}")
st.sidebar.write(f"🤖 AI: {st.session_state.ai_score}")

if st.sidebar.button("Reset Game"):
    st.session_state.history.clear()
    st.session_state.patterns.clear()
    st.session_state.user_score = 0
    st.session_state.ai_score = 0
    st.rerun()