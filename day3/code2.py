# Import necessary libraries
from pydantic import BaseModel
from typing import List
import streamlit as st
from helpers import structured_generator

# Define the Pydantic BaseModel for input validation
class Titles(BaseModel):
    titles: List[str]

# Streamlit UI code
def main():
    # Set the page title
    st.title("Blog Title Generator")

    # Get user input for the topic
    input_topic = st.text_input("Enter the topic for your video", "digital marketing")

    # Create a prompt based on user input
    prompt = f"generate 5 blog titles for a video about {input_topic}"

    # Display the prompt to the user
    st.text("Generated titles for the prompt:")
    st.code(prompt, language="python")

    # Create a button for the user to initiate title generation
    if st.button("Generate Titles"):
        # Call the structured_generator function to get generated titles
        result = structured_generator("gpt-3.5-turbo", prompt, Titles)

        # Display the generated titles
        st.text("Generated Blog Titles:")
        for title in result.titles:
            st.write(f"- {title}")

# Run the Streamlit app
if __name__ == "__main__":
    main()