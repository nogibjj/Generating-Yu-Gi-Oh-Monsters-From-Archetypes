import streamlit as st
import numpy as np
from PIL import Image
# import requests

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

    st.set_page_config(
    page_title="Yu-Gi-Oh! Card Generator",
    page_icon="https://upload.wikimedia.org/wikipedia/en/2/2b/Yugioh_Card_Back.jpg",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
    'Get help': 'https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/',
    'Report a bug': "https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/",
    'About': "# Made by Eric Rios and Shin Jiwon. This is an *extremely* cool app! Our repository is https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/"
    }
    )

    image = Image.open("logo.jpg")
    resized_image = image.resize((500, 500))
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(image)  # Set the width to the desired value

    st.title("Welcome to the Yu-Gi-Oh! Card Archetype Generator")
    st.markdown(
        """
        Welcome to the Yu-Gi-Oh! Card Archetype Generator. \n
        Here you can generate cards by providing the keywords of the archetype that you are interested in generating. 
        Provide the keyword(s), separated by commas, and press "get archetype". \n

        Example Inputs : "Blue-Eyes" or "Dark Magician, Swordswoman" \n
        """
    )
        
    # st.title("Generate Random Content")



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
