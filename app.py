# Import necessary libraries
import streamlit as st

# Import AutoGPT functionality and other backend functions
from autogpt_engine import AutoGPT
from ci_cd_pipeline import deploy_application

# Initialize AutoGPT Engine
engine = AutoGPT()

# Streamlit UI for interaction
st.title('AutoDev-Deploy')

if 'process_running' not in st.session_state:
    st.session_state.process_running = False

# User input for application request
user_input = st.text_input('Describe your application:', 'I want a todo app with a dark mode')

# Start process button
if st.button('Start Process'):
    st.session_state.process_running = True
    st.write('Processing...')
    # Use AutoGPT to begin the development process
    engine.start(user_input)
    st.write('Process started, check logs for progress.')

# Display logs and chat messages
process_chat = engine.get_chat_logs()
for message in process_chat:
    st.text(message)

# Stop process button
if st.button('Stop Process'):
    if st.session_state.process_running:
        engine.stop()
        st.session_state.process_running = False
        st.write('Process has been stopped.')

# Display manual controls and kill switch
st.header('Manual Controls')
manual_controls = st.radio('Choose an action:', ('None', 'Pause', 'Resume', 'Terminate'))

if manual_controls == 'Pause':
    engine.pause()
    st.write('Process paused.')
elif manual_controls == 'Resume':
    engine.resume()
    st.write('Process resumed.')
elif manual_controls == 'Terminate':
    engine.terminate()
    st.session_state.process_running = False
    st.write('Process terminated.')

# Deployment button
if st.button('Deploy Application'):
    if st.session_state.process_running:
        st.write('Please stop the process before deploying.')
    else:
        deploy_logs = deploy_application()
        st.text(deploy_logs)
        st.write('Application deployed successfully.')
