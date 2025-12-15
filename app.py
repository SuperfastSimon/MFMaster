# Import necessary libraries
import streamlit as st
from autonomous_agent import AutoDevAgent

# Instantiate the autonomous agent
agent = AutoDevAgent()

# Streamlit UI setup
st.title('AutoDev-Deploy')
st.markdown('### Autonome Applicatie Bouwer')

# User input for application request
user_input = st.text_input('Beschrijving van de gewenste applicatie:', '')

# Start, stop, kill process options
col1, col2, col3 = st.columns([1, 1, 1])

start_btn = col1.button('Start')
stop_btn = col2.button('Stop')
kill_btn = col3.button('Kill')

# Functionality buttons to show process or interaction
show_process = st.checkbox('Toon processen')
interact_toggle = st.checkbox('Interactie toestaan')

# Initiating process based on user input
if start_btn and user_input:
    agent.set_goal(user_input)
    agent.start_process()

# Option to stop the current process
if stop_btn:
    agent.stop_process()

# Kill the process in case of hanging
if kill_btn:
    agent.emergency_stop()

# Display ongoing processes when checkbox is ticked
if show_process:
    for update in agent.get_updates():
        st.write(update)

# Allow for dynamic user interaction if the option is toggled
if interact_toggle:
    interaction_input = st.text_input('Interactie:', '')
    if st.button('Interactie verstuur'):
        agent.user_interaction(interaction_input)

