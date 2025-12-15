import streamlit as st
import subprocess
import tempfile

# Chat interface setup
st.title('Autonome App Bouwer')

if 'process_log' not in st.session_state:
    st.session_state['process_log'] = []

# Function to append logs
def log_event(event):
    st.session_state['process_log'].append(event)

# Kill switch function
def kill_process(process):
    process.terminate()
    log_event('Process terminated')

# Autonome werking starten
user_input = st.text_input('Geef een opdracht:')

start_button = st.button('Start')
stop_button = st.button('Stop')

if start_button and user_input:
    log_event(f'Starting process with input: {user_input}')
    # Simulate the autonomous process
    with tempfile.TemporaryDirectory() as dirpath:
        try:
            # Emulate backend process calling
            process = subprocess.Popen(['python', 'auto_builder.py', user_input, dirpath])
            log_event('Process started')
        except Exception as e:
            log_event(f'Error starting process: {str(e)}')

        # Allow user to stop the process
        if stop_button:
            kill_process(process)

# Display process logs
st.header('Process Log')
for log in st.session_state['process_log']:
    st.text(log)
