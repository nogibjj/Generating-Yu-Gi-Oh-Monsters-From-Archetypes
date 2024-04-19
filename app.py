import streamlit as st
import numpy as np
from PIL import Image
import requests

# Function to generate random text
def generate_text():
    text = np.random.choice(['Hello!', 'How are you?', 'Streamlit is fun!', 'Random text generator.'])
    return text

# Function to generate a random image
def generate_image():
    # Generate a random image using numpy (for demo purposes)
    random_image = np.random.randint(0, 255, size=(300, 300, 3), dtype=np.uint8)
    return random_image

# Main function to run the Streamlit app
def main():
    st.title("Generate Random Content")

    # Button to generate random text
    if st.button("Generate Text"):
        random_text = generate_text()
        st.write(f"Random Text: {random_text}")

    # Button to generate random image
    if st.button("Generate Image"):
        random_image = generate_image()
        st.image(random_image, caption='Random Image', use_column_width=True)

if __name__ == '__main__':
    main()
