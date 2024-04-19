# Generating-Yu-Gi-Oh-Monsters-From-Archetypes
Machine Learning Experiment to generate card images and text from the titular card game by Kazuki Takahashi, rest in grace, power and peace.

## What are Archetypes? Why make this project?

## Research Questions

### Hypothesis
Current solutions for generating yu-gi-oh cards are insufficient and lacking in the field because they mix cards from multiple different archetypes. That is our hypothesis. To solve this, we propose that the way to artificially generate better cards is to use the already pre-existing General Adversarial Networks (GANs) with more wisely chosen data. In other words, the idea is to choose cards from one consistent archetype; don't mix dragons with humanoid warriors if one wants to make an archetypically consistent card. Otherwise, the model is receiving tons of inconsistent data and making tons of inconsistent cards. In short, our hypothesis is that better artifical cards can be generated with more wisely selected data.

1. What are some famous tools in this space?
2. If we control for archetypes in the training data, can some current GAN models serve to generate better images? What does it mean to isolate cards by archetype and can it be done? (CV)
3. Can we train models to produce archetype specific descriptions for the cards? (NLP)
4. Can we identify pixel distributions for the archetype's training data?
5. If found, do they vary much across different and popular archetypes?
6. Do we need near-wise archetypes for data augmentation for generating believable images and text?
7. What role does stable diffusion play in this space? What is it? Why does it do some tasks incredibly well?
8. What would well defined sentiment analysis and other NLP specific metric evaluations tell us about out archetype's text data?
9. Is there a better approach than using an archetype to define the training data? What about monster cards, card types, card series' origins, pixel similarities?

**Note to Eric and Jiwon** : Divide these questions by domain questions and experimental research questions, remember to research the space well to know what people are doing. The research is two fold : how do people generate fake cards (Pok'emon is the most famous) and what techniques from machine learning (Text and CV) are most app for this problem?
