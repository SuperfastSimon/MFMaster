import streamlit as st
import openai

# Configuratie
openai.api_key = 'YOUR_API_KEY'

def main():
    st.title('Autonome Applicatie Generator')
    
    # Input voor gebruikers
    user_input = st.text_input('Voer een beschrijving van je app in:')
    if st.button('Genereer App'):
        with st.spinner('Bezig met genereren...'):
            app_definition = generate_app_from_string(user_input)
            st.success('App gegenereerd!')
            st.code(app_definition)

    # Start/Stop knoppen
    if st.button('Start Chatfunctie'):
        chat_mode()
    if st.button('Stop Chatfunctie'):
        st.stop()
        
    # Kill switch
    if st.button('Kill Switch'):
        # Placeholder functie voor de kill switch
        st.warning('Process gestopt.')
        st.stop()


def generate_app_from_string(description):
    # OpenAI API-aanroep met promts om AI volledige stappen te laten maken
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Autonome app-ontwikkeling: {description}",
      temperature=0.5,
      max_tokens=1500
    )
    return response['choices'][0]['text'].strip()


def chat_mode():
    st.write("Chat functie gestart...")
    # Simpele loop voor chatfunctie
    input_text = st.text_input('Stel een vraag aan de app')
    if input_text:
        response = openai.Completion.create(
            model="gpt-4o",
            prompt=input_text,
            temperature=0.5,
            max_tokens=150
        )
        st.write('AI:', response['choices'][0]['text'].strip())


if __name__ == "__main__":
    main()
