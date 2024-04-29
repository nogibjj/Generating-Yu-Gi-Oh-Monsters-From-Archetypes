import streamlit as st
import numpy as np
from PIL import Image
import time
from pipeline import scrape_archetypes
import pandas as pd 
import os
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
    
    # If provided, EDA will be available
    # ARCHETYPE_PROVIDED = False 
    
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
        Under Generator Builder, provide the keyword(s), separated by commas, and press "Get Archetype". \n
        """
    )
    card_database = pd.read_csv("lib/training_cards.csv")
    with st.sidebar:
        
        st.title("Generator Builder")
        st.write("""Please enter the keyword(s) of the archetype you would like to generate. 
                 Here are some examples to get you started. Scroll below and to the right to see them.
                 
                 1) Dark Magician  2) 'Blue-Eyes, Harpie Lady'""")

        user_input = st.text_input("Enter Archetype Here")
                    
        if st.button("Get Archetype"):

            if user_input == "" or user_input == None or len(user_input) < 3:
                st.warning("Please enter an archetype.")

            else:
                # ARCHETYPE_PROVIDED = True

                with st.spinner(f"Getting data for {user_input}..."):
                    scrape_archetypes(user_input, data_path="training_images")
                    st.write(f"Here is the archetype for {user_input}")
                    st.success("Done")
                    card_database = pd.read_csv("training_cards.csv")

    # Button to generate random text
    
    if st.button("Generate Text"):
        random_text = generate_text()
        st.write(f"Random Text: {random_text}")
        # choose a random card from the card_database
        random_card = card_database.sample()
        st.write(random_card["name"].values[0])

    # Button to generate random image
    if st.button("Generate Image"):
        random_image = generate_image()
        # choose a random card from the card_database
        random_card = card_database.sample()
        path = "training_images" + os.path.sep + str(random_card["id"].values[0]) + ".jpg"
        st.write("Random Image: " + path)
        st.image(path, caption=random_card["name"].values[0], use_column_width=True)

    st.title("Data Analysis for Archetype(s) Provided", anchor="data-analysis")
    st.markdown(
        """
        Here you can see various descriptive statistics regarding the archetypes provided.. \n
        Description. \n 
        """
    )
    st.write("Data Analysis for Archetype(s) Provided")
    st.write(f"Archetype(s): {user_input}")


if __name__ == '__main__':
    main()
