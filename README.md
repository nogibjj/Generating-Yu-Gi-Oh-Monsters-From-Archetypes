# Generating Yu-Gi-Oh Monster Images and Text Using GAN, Stable Diffusion, and GIT Models
## Machine Learning Experiment 
We embarked on a machine learning experiment aimed at generating card images and text inspired by the titular card game created by Kazuki Takahashi, which embodies themes of grace, power, and peace.

## Background / Objective 
Our endeavor builds upon the diverse visual landscape presented by *Yu-Gi-Oh!* cards, which feature vibrant color schemes and distinct archetypes. Contrasting with the more uniform designs of Pokémon cards, this diversity offers an ideal dataset for testing and refining image generation techniques. 

Our project endeavors to push the boundaries of Generative Adversarial Network (GAN) technology, exploring its potential to generate intricate and varied visual elements. By doing so, we aim to contribute to advancements in both the AI sector and the gaming industry. While GANs have proven effective in producing detailed and diverse images, there remains room for improvement, especially in handling complex visual data such as Yu-Gi-Oh! cards.

Through our unique research inquiries and experimental framework, our objective is to enhance text-to-image and image captioning models to generate images closely resembling those in our training dataset, with a particular emphasis on realism and naturalness.

## Research Questions
**1. Refining Yu-Gi-Oh! Card Image Generation via GAN Model Optimization**

How can we adjust GAN model parameters to enhance image generation quality for Yu-Gi-Oh! cards by strategically manipulating the dataset?

**2. Influence of Archetypes on Generation Quality**
   
To what extent does integrating archetype control mechanisms into the training dataset improve the fidelity of generated images and accompanying textual content?

**3. Precision Enhancement through Targeted Data Categorization**

Can precise categorization of card attributes, particularly by archetype, in both image and textual datasets empower existing GAN and Natural Language Processing (NLP) models to produce more accurate and comprehensive outputs?

## Experimental Design
### Data
Initially, we sourced a total of 10,763 English Yu-Gi-Oh! cards using their official API, ensuring fair use. This dataset comprised original card images along with associated details such as card ID, name, description, and related information. Additionally, we acquired cropped images from within cards to train our GAN and stable diffusion models. Focusing on archetype testing, we finalized our dataset to include 4,252 training images and 1,064 testing images. While we refrain from publicly sharing this data due to potential ownership concerns, we have made these images accessible on the Hugging Face dataset to facilitate research in image generation challenges using GANs, particularly within the context of Yu-Gi-Oh! cards.

### Streamlit App
Leveraging insights garnered from exploratory data analysis (EDA) on both image and text data, as well as our understanding of GAN and stable diffusion models, we developed a Streamlit app to evaluate the performance of our fine-tuned models.

#### Illustrative Examples of Stable Diffusion Model Image Generation
![image](https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/assets/141780408/46949cd7-d554-4915-8934-813e64c674e9)

#### Exemplary Results from GIT Model Image Captioning
![image](https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/assets/141780408/be2b1419-8215-42d5-b282-842dfd2aa91c)

## setup
```
$ conda init 
$ pip install -r requirements.txt
$ streamlit run app.py
```
