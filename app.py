def generate_app_from_string(description):
    """
    Genereert de app architectuur met zichtbaar denkproces.
    """
    try:
        # We maken een visuele container voor het denkproces
        thought_container = st.expander("🧠 Bekijk het denkproces van GPT-5", expanded=True)
        
        with thought_container:
            st.write("Analyseren van input...")
            st.write(f"Context: {description}")

        # STAP 1: Vraag om een plan (Chain of Thought)
        # We instrueren de AI om hardop te denken
        response = client.chat.completions.create(
            model="gpt-5", 
            messages=[
                {"role": "system", "content": """
                 Je bent een Senior Software Architect. 
                 Je antwoord moet bestaan uit twee delen:
                 1. [REDENERING]: Leg uit welke keuzes je maakt (tech stack, database, structuur) en waarom.
                 2. [ONTWERP]: De uiteindelijke technische specificatie.
                 """},
                {"role": "user", "content": f"Ontwerp de volgende app: {description}"}
            ],
            temperature=0.5,
            stream=True # We streamen het antwoord voor een 'live' effect
        )

        # Variabelen om de stream op te vangen
        full_response = ""
        placeholder_reasoning = thought_container.empty()
        placeholder_result = st.empty()
        
        # Live weergave van de tokens
        accumulated_reasoning = ""
        is_reasoning = True # We nemen aan dat hij begint met redeneren door onze prompt
        
        for chunk in response:
            if chunk.choices[0].delta.content:
                text_chunk = chunk.choices[0].delta.content
                full_response += text_chunk
                
                # Simpele logica om te zien of we nog aan het redeneren zijn
                # (In een echte productie-app zou je JSON mode gebruiken voor strikte scheiding)
                if "[ONTWERP]" in text_chunk:
                    is_reasoning = False
                
                if is_reasoning:
                    accumulated_reasoning += text_chunk
                    placeholder_reasoning.info(accumulated_reasoning)
                else:
                    # Toon het uiteindelijke resultaat in het hoofdvenster
                    placeholder_result.markdown(full_response.split("[ONTWERP]")[-1])

        return full_response.split("[ONTWERP]")[-1]
        
    except Exception as e:
        return f"Error: {str(e)}"
