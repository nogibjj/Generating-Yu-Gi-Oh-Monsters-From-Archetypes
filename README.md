# Generating Yu-Gi-Oh Monster Images and Text Using GAN, Stable Diffusion, and GIT Models
We initiated a machine learning experiment aimed at generating card images and text inspired by the iconic card game created by Kazuki Takahashi, characterized by themes of grace, power, and peace.

## Background / Objective 
Our project builds upon the diverse visual landscape offered by Yu-Gi-Oh! cards, featuring vibrant color schemes and distinct archetypes. In contrast to the uniform designs of Pokémon cards, this diversity provides an excellent dataset for refining image generation techniques.

We aim to push the boundaries of Generative Adversarial Network (GAN) technology, exploring its potential to produce intricate and varied visual elements. Through this exploration, we seek to contribute to advancements in both the AI sector and the gaming industry. While GANs have shown effectiveness in generating detailed images, there remains room for improvement, particularly in handling complex visual data like Yu-Gi-Oh! cards.

Our objective is to enhance text-to-image and image captioning models to generate images closely resembling those in our training dataset, with a focus on realism and naturalness.

## Flowchart 
![image](https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/assets/141780408/8dad15a3-ea10-4d5a-ad13-6ce41aa06f5d)

## Research Questions
**1. Refining Yu-Gi-Oh! Card Image Generation via GAN Model Optimization**

How can we adjust GAN model parameters to enhance image generation quality for Yu-Gi-Oh! cards by strategically manipulating the dataset?

**2. Influence of Archetypes on Generation Quality**
   
To what extent does integrating archetype control mechanisms into the training dataset improve the fidelity of generated images and accompanying textual content?

**3. Precision Enhancement through Targeted Data Categorization**

Can precise categorization of card attributes, particularly by archetype, in both image and textual datasets empower existing GAN and Natural Language Processing (NLP) models to produce more accurate and comprehensive outputs?

## Experimental Design
### Data
We initially sourced a total of 10,763 English Yu-Gi-Oh! cards using their official API, ensuring fair use. This dataset included original card images along with associated details such as card ID, name, description, and related information. Additionally, cropped images from within cards were obtained to train our GAN and stable diffusion models. Focusing on archetype testing, we finalized our dataset to include 4,252 training images and 1,064 testing images. While refraining from publicly sharing this data due to potential ownership concerns, we have made these images accessible on the Hugging Face dataset to facilitate research in image generation challenges using GANs, particularly within the context of Yu-Gi-Oh! cards.

### Stable Diffusion Model Image Generation Example
![Stable Diffusion Model Image Generation Example](https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/assets/141780408/46949cd7-d554-4915-8934-813e64c674e9)

### GIT Model Image Captioning Example
![GIT Model Image Captioning Example](https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/assets/141780408/be2b1419-8215-42d5-b282-842dfd2aa91c)

### Streamlit App
Leveraging insights gained from exploratory data analysis (EDA) on both image and text data, as well as our understanding of GAN and stable diffusion models, we developed a Streamlit app to evaluate the performance of our fine-tuned models.

![image](https://github.com/nogibjj/Generating-Yu-Gi-Oh-Monsters-From-Archetypes/assets/141780408/14ae9d07-9ab9-4e4c-91cb-f28325099fb7)

## Setup

```
$ conda init 
$ pip install -r requirements.txt
$ streamlit run app.py
```
