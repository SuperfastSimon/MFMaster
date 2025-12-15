
import streamlit as st
import openai
from autonomous_app_builder import AutonomousAppBuilder

# Initialiseer de AutonomousAppBuilder met OpenAI GPT-4 APIs
app_builder = AutonomousAppBuilder(api_key='your-openai-api-key')

# Streamlit interface
st.title('Autonome Applicatie Bouwer')

# Gebruikersinput
user_input = st.text_input('Beschrijf de applicatie die je wilt bouwen:')

# Start/Stop en Kill switches
if st.button('Start Bouwen'):
    st.session_state['building'] = True
if st.button('Stop Bouwen'):
    st.session_state['building'] = False
if st.button('Kill Process'):
    app_builder.kill_process()

# Bouwproces
if st.session_state.get('building', False):
    st.write('Applicatie aan het bouwen...')
    app_url, build_log = app_builder.build_from_description(user_input)
    st.write(f'Voltooide Applicatie: [Bezoek hier]({app_url})')
    st.write(build_log)

# Chat functie
st.subheader('Communicatie met de AI')
if st.session_state.get('building', False):
    for thought in app_builder.get_thoughts():
        st.write(thought)
