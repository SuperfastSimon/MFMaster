import streamlit as st
import openai
import subprocess
import os

# Set up OpenAI credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize long-term memory store
def initialize_memory():
    if not os.path.exists('memory.txt'):
        open('memory.txt', 'w').close()

# Save memory
def save_memory(data):
    with open('memory.txt', 'a') as f:
        f.write(data + '\n')

# Read from memory
def read_memory():
    with open('memory.txt', 'r') as f:
        return f.read().splitlines()

# Function to create an app idea to application process
def process_idea(idea):
    # Example of recursive thought process
    save_memory(f"Received idea: {idea}")
    steps = [
        "Convert idea to requirements specification",
        "Generate code for frontend/backend",
        "Run tests on the application",
        "Deploy the application to hosting service",
        "Monitor application for issues"
    ]
    results = []
    for step in steps:
        # Simulated response from an AI-driven process
        result = openai.Completion.create(
            model="text-davinci-005",
            prompt=f"{step} for: {idea}",
            temperature=0.3
        )
        output = result.choices[0].text.strip()
        save_memory(f"{step}: {output}")
        results.append(output)
        if "error" in output.lower():
            save_memory("Encountered an error, stopping the process.")
            return results, False
    return results, True

# Deploy using CI/CD pipeline (mock function)
def deploy_app(code):
    try:
        # In a real scenario, this would involve pushing code to a repo, triggering a build, etc.
        subprocess.run(["echo", "Deploying application..."], check=True)
        return "https://deployed.todolistapp.com"
    except subprocess.CalledProcessError as e:
        save_memory(f"Deployment failed: {str(e)}")
        return None

# Streamlit interface
st.title("Autonomous App Creator")

initialize_memory()  # Ensure memory is set up

idea = st.text_input("Enter your app idea:", "I want a todo app with a dark mode.")

if st.button("Start Process"):
    st.write("Processing your idea... Please wait.")
    results, successful = process_idea(idea)
    if successful:
        st.success("Idea processed successfully!")
        code = results[-1]  # Assuming final step returns code
        url = deploy_app(code)
        if url:
            st.write(f"Application deployed successfully! [View here]({url})")
        else:
            st.error("Deployment failed.")
    else:
        st.error("Process encountered an error.")

if st.button("View Process Memory"):
    memory = read_memory()
    st.write(memory)

if st.button("Kill Process"):
    st.warning("Process killed! Resetting the state.")
    open('memory.txt', 'w').close()  # Clearing memory