# Import necessary libraries
import streamlit as st
from ai_builder import AIAgent

# Initialize the AI Agent
agent = AIAgent()

# Streamlit UI
st.title('Autonomous Application Builder')

# Input from the user
user_input = st.text_input('Enter your app description:')

# Start and stop buttons
if st.button('Start'):
    if user_input:
        agent.process(user_input)
        st.success('Processing...')
    else:
        st.warning('Please provide a description.')

if st.button('Stop'):
    agent.stop_process()
    st.info('Process stopped')

# Chat function to show agent's thought process
st.subheader('Agent Process Log')
for message in agent.get_process_log():
    st.write(message)

# Function buttons
st.subheader('Agent Controls')
if st.button('Kill Switch'):
    agent.kill_switch()
    st.error('Agent terminated')

# Display deployment status
st.subheader('Deployment Status')
deployment_status = agent.get_deployment_status()
st.write(deployment_status)