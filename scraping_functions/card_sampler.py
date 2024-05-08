"""Functions to help sample all the cards to comply with Fair Use Policy."""
import pandas as pd
import os

def classifier_type(card):
    """Classifies the type of card in a simplified output.
        Args:
            card (str): The card to be classified.
        Returns:
            str: The type of card.
    """

    if "spell" in card.lower():
        return "spell"
    elif "trap" in card.lower():
        return "trap"
    elif "effect" in card.lower():
        return "effect monster"
    elif "monster" in card.lower():
        return "monster"
    else:
        return "unknown" 
    
def sample_from_cards_csv(csv_path, random_state=42):
    """Samples from a csv file with all cards.
        Args:
            img_path (str): The path to the image folder.
            csv_path (str): The path to the csv file.
        Returns:
            pd.DataFrame: The sampled data.
    """
    # Step 1: Group your data by the strata you want to sample from
    df = pd.read_csv(csv_path)

    groups = df.groupby('type')

    # Step 2: Define a sampling function
    def stratified_sample(group):
         # You can adjust the fraction and other parameters as needed
        return group.sample(frac=0.5, replace=False, random_state = random_state) 

    # Step 3: Apply the sampling function to each group
    sampled_groups = groups.apply(stratified_sample)

    # Step 4: Concatenate the sampled groups back together
    sampled_data = sampled_groups.reset_index(drop=True)

    # Now 'sampled_data' contains your stratified sample

    return sampled_data

def extract_image_id(image_path):
    """Extracts card image file name from path"""
    return image_path.split("/")[-1]
 
def build_sample(img_path, csv_path, random_state=42):
    """Builds a sample from a csv file with all cards.
        Args:
            img_path (str): The path to the image folder.
            csv_path (str): The path to the csv file.
            random_state (int): The random state for reproducibility.
        Returns:
            None
    """

    sampled_csv = sample_from_cards_csv(csv_path, random_state=random_state)

    sampled_csv["image_id"] = sampled_csv["image_path"].apply(extract_image_id)
    allowed_images = sampled_csv["image_id"].values
    print("CHECK" , len(allowed_images), len(sampled_csv["image_id"].values))
    for image in os.listdir(img_path):
        if image not in allowed_images:
            os.remove(os.path.join(img_path, image))

    sampled_csv.to_csv(csv_path, index=False)

    return 


if __name__ == "__main__":
    img_path = "training_data_final/training_images"
    csv_path = "training_data_final/all_training_cards.csv"
    build_sample(img_path, csv_path, random_state=42)
    
    print("Sampled data created!")

